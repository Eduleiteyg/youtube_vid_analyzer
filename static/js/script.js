document.addEventListener('DOMContentLoaded', () => {
    const processBtn = document.getElementById('process-btn');
    const askBtn = document.getElementById('ask-btn');
    const videoUrlInput = document.getElementById('video-url');
    const questionInput = document.getElementById('question');
    const statusMessage = document.getElementById('status-message');
    const qaSection = document.getElementById('qa-section');
    const answerP = document.getElementById('answer');

    processBtn.addEventListener('click', async () => {
        const videoUrl = videoUrlInput.value;
        if (!videoUrl) {
            statusMessage.textContent = 'Please enter a YouTube URL.';
            statusMessage.style.color = 'red';
            return;
        }

        statusMessage.textContent = 'Processing video... Please wait.';
        statusMessage.style.color = 'orange';

        try {
            const response = await fetch('/process_video', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ video_url: videoUrl })
            });

            const data = await response.json();

            if (response.ok) {
                statusMessage.textContent = data.message;
                statusMessage.style.color = 'green';
                qaSection.classList.remove('hidden');
            } else {
                statusMessage.textContent = `Error: ${data.error}`;
                statusMessage.style.color = 'red';
            }
        } catch (error) {
            statusMessage.textContent = 'An unexpected error occurred.';
            statusMessage.style.color = 'red';
        }
    });

    askBtn.addEventListener('click', async () => {
        const question = questionInput.value;
        if (!question) {
            answerP.textContent = 'Please enter a question.';
            return;
        }

        answerP.textContent = 'Thinking...';

        try {
            const response = await fetch('/ask_question', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ question: question })
            });

            const data = await response.json();

            if (response.ok) {
                answerP.textContent = data.answer;
            } else {
                answerP.textContent = `Error: ${data.error}`;
            }
        } catch (error) {
            answerP.textContent = 'An unexpected error occurred.';
        }
    });
});