document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".thumb-btn.yes");
  const noBtn = document.querySelector(".thumb-btn.no");
  const buttons = document.querySelector(".thumb-buttons");
  const thanks = document.querySelector(".feedback-thanks");

  if (!yesBtn || !noBtn) return;

  // 👍 YES
  yesBtn.addEventListener("click", () => {
    buttons.style.display = "none";
    thanks.style.display = "block";
  });

  // 👎 NO
  noBtn.addEventListener("click", () => {
    const guideTitle = encodeURIComponent(document.title);
    const formURL = `https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform?usp=pp_url&entry.1576705921=%F0%9F%91%8E+No&entry.1234567890=${guideTitle}`;
    window.open(formURL, "_blank");
  });
});
