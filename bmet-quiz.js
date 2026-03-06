let questions = [];
let currentIndex = 0;

// Fetch questions from JSON
fetch('data/bmet-questions.json')
  .then(response => response.json())
  .then(data => {
    questions = data;
    showQuestion();
  })
  .catch(err => console.error("Failed to load questions:", err));

function showQuestion() {
  if (!questions.length) return;
  const q = questions[currentIndex];
  document.getElementById("question").innerText = q.q;
  const optionsDiv = document.getElementById("options");
  optionsDiv.innerHTML = "";
  q.options.forEach((opt, idx) => {
    const btn = document.createElement("button");
    btn.innerText = opt;
    btn.style.display = "block";
    btn.style.width = "100%";
    btn.style.margin = "5px 0";
    btn.style.padding = "8px";
    btn.style.borderRadius = "8px";
    btn.style.border = "1px solid #007bff";
    btn.style.background = "#f8f9fa";
    btn.style.cursor = "pointer";
    btn.onclick = () => checkAnswer(idx);
    optionsDiv.appendChild(btn);
  });
  document.getElementById("feedback").innerText = "";
}

function checkAnswer(selected) {
  const q = questions[currentIndex];
  const feedback = document.getElementById("feedback");
  if (selected === q.answer) {
    feedback.innerText = "✅ Correct!";
    feedback.style.color = "green";
  } else {
    feedback.innerText = `❌ Wrong! Correct: ${q.options[q.answer]}`;
    feedback.style.color = "red";
  }
  // Move to next question after 1.5s
  setTimeout(() => {
    currentIndex = (currentIndex + 1) % questions.length;
    showQuestion();
  }, 1500);
}
