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

    // Button default styles
    btn.style.display = "block";
    btn.style.width = "100%";
    btn.style.margin = "6px 0";
    btn.style.padding = "10px";
    btn.style.borderRadius = "10px";
    btn.style.border = "2px solid #ff66cc"; // hotpink border
    btn.style.background = "#111";           // dark background
    btn.style.color = "#fff";                // white text default
    btn.style.fontWeight = "bold";
    btn.style.cursor = "pointer";
    btn.style.outline = "none";              // remove browser blue
    btn.style.boxShadow = "none";            // remove browser shadow
    btn.onmousedown = () => btn.style.outline = "none";
    btn.onfocus = () => btn.style.outline = "none";

    // Hover effect
    btn.addEventListener("mouseover", () => {
      btn.style.background = "#8fff00"; // limegreen
      btn.style.color = "#111";          // black text
      btn.style.border = "2px solid #ff66cc"; // hotpink
    });
    btn.addEventListener("mouseout", () => {
      btn.style.background = "#111";   // dark background
      btn.style.color = "#fff";        // white text
      btn.style.border = "2px solid #ff66cc"; // hotpink
    });

    btn.onclick = () => checkAnswer(idx);
    optionsDiv.appendChild(btn);
  });

  const feedback = document.getElementById("feedback");
  feedback.innerText = "";
  feedback.style.color = "#111"; // neutral color until answered
}

function checkAnswer(selected) {
  const q = questions[currentIndex];
  const feedback = document.getElementById("feedback");
  if (selected === q.answer) {
    feedback.innerText = "Correct!";
    feedback.style.color = "#8fff00"; // limegreen for correct
  } else {
    feedback.innerText = `Wrong! Correct: ${q.options[q.answer]}`;
    feedback.style.color = "#ff66cc"; // hotpink for wrong
  }

  // Move to next question after 3s
  setTimeout(() => {
    currentIndex = (currentIndex + 1) % questions.length;
    showQuestion();
  }, 3000);
}
