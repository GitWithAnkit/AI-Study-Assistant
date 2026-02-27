from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai
import pdfplumber


load_dotenv()
app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Gemini API Key not found in .env file")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")



@app.route('/')
def home():
    return render_template("index.html")



@app.route('/explain', methods=['POST'])
def explain():
    try:
        data = request.json
        topic = data.get("topic")

        if not topic:
            return jsonify({"response": "Please enter a topic."})

        prompt = f"""
        Explain the topic '{topic}' in simple language.
        Include:
        - Clear explanation
        - Step-by-step breakdown
        - One example
        """

        response = model.generate_content(prompt)

        return jsonify({"response": response.text})

    except Exception as e:
        print("EXPLAIN ERROR:", str(e))
        return jsonify({"response": "Server error occurred while explaining."})



@app.route('/generate-quiz', methods=['POST'])
def generate_quiz():
    try:
        data = request.json
        topic = data.get("topic")
        difficulty = data.get("difficulty")
        num_questions = data.get("numQuestions")

        if not topic:
            return jsonify({"response": "Please enter a topic."})

        prompt = f"""
        Generate {num_questions} multiple choice questions about '{topic}'.
        Difficulty level: {difficulty}.

        Format:
        Q1.
        A)
        B)
        C)
        D)
        Correct Answer:
        Explanation:
        """

        response = model.generate_content(prompt)

        return jsonify({"response": response.text})

    except Exception as e:
        print("QUIZ ERROR:", str(e))
        return jsonify({"response": "Server error occurred while generating quiz."})



@app.route('/summarize-pdf', methods=['POST'])
def summarize_pdf():
    try:
        if 'pdf' not in request.files:
            return jsonify({"response": "No file uploaded."})

        file = request.files['pdf']

        if file.filename == '':
            return jsonify({"response": "No selected file."})

        text = ""

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages[:5]:
                extracted = page.extract_text()
                if extracted:
                    text += extracted

        if not text.strip():
            return jsonify({"response": "Could not extract readable text from PDF."})

        text = text[:5000]

        prompt = f"""
        Summarize the following study notes.
        Provide:
        - Clear summary
        - Key points
        - Important concepts

        Notes:
        {text}
        """

        response = model.generate_content(prompt)

        return jsonify({"response": response.text})

    except Exception as e:
        print("PDF ERROR:", str(e))
        return jsonify({"response": "Server error occurred while processing PDF."})



if __name__ == "__main__":
    app.run(debug=True)