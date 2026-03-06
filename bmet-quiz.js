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
  const questionDiv = document.getElementById("question");
  questionDiv.innerText = q.q;
  questionDiv.style.color = "#111"; // black question text

  const optionsDiv = document.getElementById("options");
  optionsDiv.innerHTML = "";

 q.options.forEach((opt, idx) => {
  const btn = document.createElement("button");
  btn.innerText = opt;

  // Button styles to match content-box / guide cards
  btn.style.display = "block";
  btn.style.width = "100%";
  btn.style.margin = "6px 0";
  btn.style.padding = "12px";
  btn.style.borderRadius = "8px";
  btn.style.border = "2px solid #111"; // black border
  btn.style.background = "#fff";        // white background like cards
  btn.style.color = "#111";             // black text default
  btn.style.fontWeight = "bold";
  btn.style.cursor = "pointer";
  btn.style.textAlign = "center";
  btn.style.transition = "0.2s";

  btn.onclick = () => checkAnswer(idx);
  optionsDiv.appendChild(btn);
});
  
  const feedback = document.getElementById("feedback");
  feedback.innerText = "";
  feedback.style.color = "#111"; // neutral color until answered
}

function showQuestion() {
  if (!questions.length) return;
  const q = questions[currentIndex];
  const questionDiv = document.getElementById("question");
  questionDiv.innerText = q.q;

  const optionsDiv = document.getElementById("options");
  optionsDiv.innerHTML = "";

  q.options.forEach((opt, idx) => {
    const btn = document.createElement("button");
    btn.innerText = opt;
    btn.onclick = () => checkAnswer(idx);
    optionsDiv.appendChild(btn);
  });

  const feedback = document.getElementById("feedback");
  feedback.innerText = "";
  feedback.className = "";
}

function checkAnswer(selected) {
  const q = questions[currentIndex];
  const feedback = document.getElementById("feedback");

  if (selected === q.answer) {
    feedback.innerText = "Correct!";
    feedback.className = "correct";
  } else {
    feedback.innerText = `Wrong! Answer: ${q.options[q.answer]}`;
    feedback.className = "wrong";
  }

  setTimeout(() => {
    currentIndex = (currentIndex + 1) % questions.length;
    showQuestion();
  }, 3000);
}
