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

  // Default styles
  btn.style.display = "block";
  btn.style.width = "100%";
  btn.style.margin = "6px 0";
  btn.style.padding = "10px";
  btn.style.borderRadius = "10px";
  btn.style.border = "2px solid #ff66cc"; // hotpink border
  btn.style.background = "#111";           // dark background
  btn.style.color = "#fff";                // WHITE text by default
  btn.style.fontWeight = "bold";
  btn.style.cursor = "pointer";
  btn.style.boxShadow = "none";
  btn.style.outline = "none";

  // Hover effect
  btn.addEventListener("mouseover", () => {
    btn.style.background = "#8fff00"; // limegreen
    btn.style.color = "#111";          // BLACK text on hover
    btn.style.border = "2px solid #ff66cc"; // hotpink border
  });
  btn.addEventListener("mouseout", () => {
    btn.style.background = "#111";   // back to dark
    btn.style.color = "#fff";        // WHITE text default
    btn.style.border = "2px solid #ff66cc"; // hotpink border
  });

  btn.onclick = () => checkAnswer(idx);
  optionsDiv.appendChild(btn);
});

  const feedback = document.getElementById("feedback");
  feedback.innerText = "";
  feedback.style.color = "#111"; // black feedback text by default
}

function checkAnswer(selected) {
  const q = questions[currentIndex];
  const feedback = document.getElementById("feedback");
  if (selected === q.answer) {
    feedback.innerText = "✅ Correct!";
    feedback.style.color = "#8fff00"; // limegreen feedback
  } else {
    feedback.innerText = `❌ Wrong! Correct: ${q.options[q.answer]}`;
    feedback.style.color = "#ff66cc"; // hotpink feedback
  }

  // Move to next question after 1.5s
  setTimeout(() => {
    currentIndex = (currentIndex + 1) % questions.length;
    showQuestion();
  }, 1500);
}
