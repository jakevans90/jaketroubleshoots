document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".thumb-btn.yes");
  const noBtn = document.querySelector(".thumb-btn.no");
  const buttons = document.querySelector(".thumb-buttons");
  const form = document.querySelector(".feedback-form");
  const iframe = document.querySelector(".feedback-iframe");
  const thanks = document.querySelector(".feedback-thanks");

  const formURL = "https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform?embedded=true";

  if (!yesBtn || !noBtn) return; // prevents script crash

  yesBtn.addEventListener("click", () => {
    buttons.style.display = "none";
    thanks.style.display = "block";

    // OPTIONAL: still loads form silently (can remove if you want)
    iframe.src = formURL;
  });

  noBtn.addEventListener("click", () => {
    buttons.style.display = "none";
    form.style.display = "block";

    // Load form ONLY when needed
    iframe.src = formURL;
  });
});
