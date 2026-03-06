let questions = [];
let currentIndex = 0;

// Fetch questions from JSON
fetch('data/bmet-questions.json')
  .then(response => response.json())
  .then(data => {
    // Shuffle all questions
    questions = shuffleArray(data);

    // Shuffle each question's options and update correct index
    questions.forEach(q => {
      const shuffled = shuffleArrayWithIndex(q.options, q.answer);
      q.options = shuffled.options;
      q.answer = shuffled.newIndex;
    });

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

    // Button styles (keep your original design)
    btn.style.display = "block";
    btn.style.width = "100%";
    btn.style.margin = "6px 0";
    btn.style.padding = "12px";
    btn.style.borderRadius = "8px";
    btn.style.border = "2px solid #111";
    btn.style.background = "#fff";
    btn.style.color = "#111";
    btn.style.fontWeight = "bold";
    btn.style.cursor = "pointer";
    btn.style.textAlign = "center";
    btn.style.transition = "0.2s";

    // Hover effect
    btn.addEventListener("mouseover", () => {
      btn.style.background = "#f4f4f4";
      btn.style.borderColor = "#111";
    });
    btn.addEventListener("mouseout", () => {
      btn.style.background = "#fff";
      btn.style.borderColor = "#111";
    });

    btn.onclick = () => checkAnswer(idx);
    optionsDiv.appendChild(btn);
  });

  const feedback = document.getElementById("feedback");
  feedback.innerText = "";
  feedback.className = ""; // reset feedback styling
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

  // Move to next question after 3s
  setTimeout(() => {
    currentIndex = (currentIndex + 1) % questions.length;
    showQuestion();
  }, 3000);
}

// ===========================================
// Utility Functions
// ===========================================

// Shuffle array
function shuffleArray(array) {
  return array
    .map(value => ({ value, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .map(({ value }) => value);
}

// Shuffle array and return new index of original correct answer
function shuffleArrayWithIndex(array, correctIndex) {
  const indexed = array.map((value, i) => ({ value, originalIndex: i }));
  const shuffled = shuffleArray(indexed);
  const newIndex = shuffled.findIndex(e => e.originalIndex === correctIndex);
  return {
    options: shuffled.map(e => e.value),
    newIndex
  };
}
