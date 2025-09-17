# 📺 YouTube Video Analyzer & Chatbot (Flask)

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask) ![LangChain](https://img.shields.io/badge/LangChain-0086CB?style=for-the-badge&logo=langchain) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai) ![FAISS](https://img.shields.io/badge/FAISS-0080FF?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python) ![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube)

Hey there! Welcome to my YouTube Video Analyzer. I built this tool because I wanted a way to quickly understand and "talk to" the content of any YouTube video without having to watch the whole thing. This project is a complete, end-to-end **Retrieval-Augmented Generation (RAG)** application with a friendly web interface built using **Flask** and a bit of custom frontend magic.

You can just paste a YouTube video link, and the app will automatically download the transcript, create a searchable knowledge base, and let you ask any questions about the video's content.

---

### ✨ Core Features

-   **Direct YouTube Transcript Fetching**: Uses the `youtube-transcript-api` library to directly and efficiently fetch the full transcript of any YouTube video using its ID.
-   **Text Chunking**: Intelligently splits the transcript into smaller, overlapping chunks using `RecursiveCharacterTextSplitter` to prepare it for embedding.
-   **In-Memory Vector Store**: Uses `OpenAIEmbeddings` to convert the text chunks into numerical vectors and stores them in a lightning-fast **FAISS** vector store for efficient semantic search.
-   **Conversational Q&A**: Leverages a powerful LangChain `RetrievalQA` chain to answer your questions based on the context retrieved from the video's transcript.
-   **Interactive Web UI**: A clean and simple user interface built with **Flask**, HTML, CSS, and JavaScript, making the whole process easy and intuitive.

---

### 📸 Screenshots

Here's a look at the application in action. You just paste a link, and the app gets to work!

**Main Interface & First Answer:**
![Main application interface showing video URL input and a generated answer]<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/30b838bb-e4e8-49e2-9cd0-31e43061c9b8" />

**Terminal Output while Running:**
![Screenshot of the terminal showing Flask server running and request logs] <img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/2524f263-b1c4-4f97-b91b-519efa761d5f" />

---

### 🛠️ Tech Stack

Based on our `app.py` and `requirements.txt`:

-   **Web Framework**: Flask
-   **Core AI Framework**: LangChain
    -   `langchain`
    -   `langchain-core`
    -   `langchain-openai`
    -   `langchain-community` (for `youtube-transcript-api`)
-   **LLM & Embedding Provider**: OpenAI
    -   `openai`
-   **Vector Store**: FAISS (CPU version)
    -   `faiss-cpu`
-   **Environment Variables**: `python-dotenv`
-   **Frontend**: HTML, CSS, JavaScript (served via Flask)

---

### ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jsonusuman351/youtube_vid_analyzer.git](https://github.com/jsonusuman351/youtube_vid_analyzer.git)
    cd youtube_vid_analyzer
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # It is recommended to use Python 3.10 or higher
    python -m venv venv
    .\venv\Scripts\activate # On Windows
    source venv/bin/activate # On macOS/Linux
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables:**
    -   Create a file named `.env` in the **root directory** of the project (at the same level as `app.py`).
    -   Add your OpenAI API key to this file. The application needs it to function.
        ```env
        OPENAI_API_KEY="your-openai-api-key-here"
        ```

---

### 🚀 How to Run the Application

Once you've completed the setup, running the Flask application is straightforward.

1.  **Open your terminal** in the root project directory (where `app.py` is located).
2.  **Make sure your virtual environment is active.**
3.  **Set the Flask environment variable:**
    ```bash
    # On Windows (Command Prompt)
    set FLASK_APP=app.py
    # On Windows (PowerShell)
    $env:FLASK_APP="app.py"
    # On macOS/Linux
    export FLASK_APP=app.py
    ```
4.  **Run the Flask application:**
    ```bash
    flask run
    ```
    Alternatively, if `FLASK_APP` is set, you can often just run:
    ```bash
    python -m flask run
    ```

    You should see output similar to the second screenshot, indicating the server is running on `http://127.0.0.1:5000`. Open this URL in your web browser.

---

### 🔬 Project Structure

I've organized the project in a standard Flask layout, making it easy to manage the application logic and static assets.

<details>
<summary>Click to view the project layout</summary>

```
youtube_vid_analyzer/
│
├── app.py                      # Main Flask application logic
├── requirements.txt            # List of Python dependencies
├── .env                        # Environment variables (e.g., API keys)
│
├── static/                     # For CSS, JavaScript, images, etc.
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── templates/                  # HTML templates for rendering web pages
    └── index.html              # The main user interface
│
└── venv/                       # (Your Python virtual environment)
│
└── .gitignore                  # Files/folders to ignore in Git
│
└── README.md                   # This README file!
```
</details>

---

---