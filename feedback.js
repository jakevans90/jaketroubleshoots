document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".thumb-btn.yes");
  const noBtn = document.querySelector(".thumb-btn.no");
  const buttons = document.querySelector(".thumb-buttons");
  const formContainer = document.querySelector(".feedback-form");
  const iframe = document.querySelector(".feedback-iframe");
  const thanks = document.querySelector(".feedback-thanks");

  if (!yesBtn || !noBtn || !iframe) return;

  // Base Google Form URL
  const baseURL = "https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform?embedded=true";

  // Replace these with your actual Google Form field IDs
  const thumbsFieldID = "1576705921";   // Was this guide helpful? (Yes/No)
  const guideNameFieldID = "1234567890"; // Guide Name

  const currentGuide = encodeURIComponent(document.title);

  // 👍 YES
  yesBtn.addEventListener("click", () => {
    buttons.style.display = "none";
    thanks.style.display = "block";

    // Set iframe src so Google receives the thumbs-up feedback
    iframe.src = `${baseURL}&entry.${thumbsFieldID}=%F0%9F%91%8D+Yes&entry.${guideNameFieldID}=${currentGuide}`;
  });

  // 👎 NO
  noBtn.addEventListener("click", () => {
    buttons.style.display = "none";
    formContainer.style.display = "block";

    // Set iframe src so Google receives thumbs-down and current page
    iframe.src = `${baseURL}&entry.${thumbsFieldID}=%F0%9F%91%8E+No&entry.${guideNameFieldID}=${currentGuide}`;
  });
});
