# AI Study Assistant

An AI-powered study companion that helps students understand topics, practice through quizzes, and revise learning material with the help of Google's Gemini API.

## Overview

AI Study Assistant is a Flask-based web application designed to make self-study more interactive. Users can enter a topic to receive a simplified explanation, generate multiple-choice questions at a selected difficulty, or upload a PDF and get a concise summary of its contents.

The application uses **Google Gemini 2.5 Flash** to generate learning content and **pdfplumber** to extract text from uploaded PDF documents.

## Features

- **Topic explanations** – Enter a subject or concept and receive a clear, step-by-step explanation with an example.
- **Quiz generation** – Generate multiple-choice questions for a topic, with a difficulty level and question count.
- **PDF summarization** – Upload a PDF and receive a summary containing key points and important concepts.
- **Web interface** – Access the study tools through a browser-based interface powered by Flask templates.
- **Environment-based configuration** – Keep the Gemini API key outside the source code using a `.env` file.

## Tech Stack

| Area | Technology |
|---|---|
| Backend | Python, Flask |
| Generative AI | Google Gemini API (`gemini-2.5-flash`) |
| PDF text extraction | pdfplumber |
| Configuration | python-dotenv |
| Frontend | HTML, CSS, JavaScript (Flask templates and static assets) |
| Deployment server dependency | Gunicorn |

## Project Structure

```text
AI-Study-Assistant/
├── app.py
├── requirements.txt
├── .gitignore
├── static/          # CSS, JavaScript, images and other static assets
└── templates/       # HTML templates rendered by Flask
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/GitWithAnkit/AI-Study-Assistant.git
cd AI-Study-Assistant
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

** macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a file named `.env` in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get an API key from [Google AI Studio](https://aistudio.google.com/). Do not commit your `.env` file or share your API key publicly.

### 5. Run the application

```bash
python app.py
```

Open the local URL printed by Flask in your browser (typically `http://127.0.0.1:5000`).

## Application Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Loads the study assistant interface |
| `/explain` | POST | Generates an explanation for a topic |
| `/generate-quiz` | POST | Generates topic-based multiple-choice questions |
| `/summarize-pdf` | POST | Extracts and summarizes text from an uploaded PDF |

## How It Works

1. The user selects a study task from the web interface.
2. The frontend sends the relevant input to a Flask endpoint.
3. Flask prepares a prompt and sends it to the Gemini model.
4. For PDF summarization, `pdfplumber` first extracts text from the uploaded document; the extracted content is then passed to Gemini.
5. The generated response is returned to the interface.

## Notes and Limitations

- PDF summarization currently processes text from up to the first **five pages** and limits the extracted text sent to the model.
- The application requires a valid Gemini API key and is subject to the API provider's quotas and usage limits.
- Scanned PDFs that do not contain extractable text may not produce a useful summary.
- AI-generated explanations and quiz answers should be reviewed for accuracy.

## Future Enhancements

- Add chat-based follow-up questions and conversation history.
- Support larger documents and more document formats.
- Add quiz scoring, answer review, and progress tracking.
- Improve input validation, error handling, and usage feedback.
- Add user accounts and personalized study plans.

## Author

**Ankit**  
GitHub: [@GitWithAnkit](https://github.com/GitWithAnkit)

---

If you find this project useful, consider giving the repository a ⭐.
