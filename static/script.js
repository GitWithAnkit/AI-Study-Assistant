function explainTopic() {
    const topic = document.getElementById("topicInput").value.trim();
    const resultBox = document.getElementById("explanationResult");

    if (!topic) {
        resultBox.innerText = "Please enter a topic first.";
        return;
    }

    resultBox.innerText = "Generating explanation... ⏳";

    fetch("/explain", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ topic: topic })
    })
    .then(response => response.json())
    .then(data => {
        resultBox.innerText = data.response;
    })
    .catch(error => {
        resultBox.innerText = "Something went wrong. Please try again.";
        console.error(error);
    });
}


function generateQuiz() {
    const topic = document.getElementById("quizTopic").value.trim();
    const difficulty = document.getElementById("difficulty").value;
    const numQuestions = document.getElementById("numQuestions").value;
    const resultBox = document.getElementById("quizResult");

    if (!topic) {
        resultBox.innerText = "Please enter a topic.";
        return;
    }

    resultBox.innerText = "Generating quiz... ⏳";

    fetch("/generate-quiz", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            topic: topic,
            difficulty: difficulty,
            numQuestions: numQuestions
        })
    })
    .then(response => response.json())
    .then(data => {
        resultBox.innerText = data.response;
    })
    .catch(error => {
        resultBox.innerText = "Something went wrong.";
        console.error(error);
    });
}

document.getElementById("pdfForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const resultBox = document.getElementById("summaryResult");

    resultBox.innerText = "Processing PDF... ⏳";

    fetch("/summarize-pdf", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        resultBox.innerText = data.response;
    })
    .catch(error => {
        resultBox.innerText = "Error processing PDF.";
        console.error(error);
    });
});
