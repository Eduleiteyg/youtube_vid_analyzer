import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# .env file se API key load karein
load_dotenv()

# Check karein ki API key set hai ya nahi
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable not set. Please create a .env file and add it.")

app = Flask(__name__)

# Global variable to store the vector store
vector_store = None

def get_video_id(url):
    """Extracts the video ID from a YouTube URL."""
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]
    if "youtube.com" in url:
        return url.split("v=")[-1].split("&")[0]
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_video', methods=['POST'])
def process_video():
    global vector_store
    data = request.get_json()
    video_url = data.get('video_url')

    if not video_url:
        return jsonify({'error': 'Video URL is required.'}), 400

    video_id = get_video_id(video_url)
    if not video_id:
        return jsonify({'error': 'Invalid YouTube URL.'}), 400

    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.fetch(video_id)
        transcript = " ".join([d.text for d in transcript_list])

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.create_documents([transcript])

        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        vector_store = FAISS.from_documents(chunks, embeddings)

        return jsonify({'message': 'Video processed successfully!'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieved documents ko format karne ke liye helper function
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

@app.route('/ask_question', methods=['POST'])
def ask_question():
    global vector_store
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({'error': 'Question is required.'}), 400

    if not vector_store:
        return jsonify({'error': 'Please process a video first.'}), 400

    try:
        # LangChain Expression Language (LCEL) ka istemal karke chain banayein
        retriever = vector_store.as_retriever()
        
        prompt = PromptTemplate.from_template(
            """
              You are a helpful assistant.
              Answer ONLY from the provided transcript context.
              If the context is insufficient, just say you don't know.

              Context: {context}
              Question: {question}
            """
        )

        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

        # Ye hai aapka naya RAG Chain
        rag_chain = (
            RunnableParallel(
                context=retriever | format_docs,
                question=RunnablePassthrough()
            )
            | prompt
            | llm
            | StrOutputParser()
        )

        # Chain ko invoke karke answer generate karein
        answer = rag_chain.invoke(question)
        return jsonify({'answer': answer})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)