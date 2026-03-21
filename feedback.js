document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".thumb-btn.yes");
  const noBtn = document.querySelector(".thumb-btn.no");
  const buttons = document.querySelector(".thumb-buttons");
  const thanks = document.querySelector(".feedback-thanks");

  const formURL = "https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform";

  if (!yesBtn || !noBtn) return;

  // 👍 YES (simple)
  yesBtn.addEventListener("click", () => {
    buttons.style.display = "none";
    thanks.style.display = "block";

    // OPTIONAL: log it silently (we can improve this later)
  });

  // 👎 NO (open form properly)
  noBtn.addEventListener("click", () => {
    window.open(formURL, "_blank"); // opens in new tab
  });
});
