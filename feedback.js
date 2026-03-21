document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".thumb-btn.yes");
  const noBtn = document.querySelector(".thumb-btn.no");
  const buttons = document.querySelector(".thumb-buttons");
  const form = document.querySelector(".feedback-form");
  const thanks = document.querySelector(".feedback-thanks");

  if (!yesBtn || !noBtn) return;

  // 👍 YES
  yesBtn.addEventListener("click", () => {
    buttons.style.display = "none";
    thanks.style.display = "block";
  });

  // 👎 NO
  noBtn.addEventListener("click", () => {
    buttons.style.display = "none";
    form.style.display = "block";
  });
});
