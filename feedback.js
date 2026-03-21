document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".thumb-btn.yes");
  const noBtn = document.querySelector(".thumb-btn.no");
  const thanks = document.querySelector(".feedback-thanks");
  const modal = document.getElementById("feedback-modal");
  const iframe = document.getElementById("modal-iframe");
  const closeBtn = document.getElementById("modal-close");

  if (!yesBtn || !noBtn || !modal || !iframe) return;

  // Google Form base URL
  const baseURL = "https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform?usp=pp_url";

  // Encode the guide title for URL
  const guideName = encodeURIComponent(document.title);

  yesBtn.addEventListener("click", () => {
    iframe.src = `${baseURL}&entry.1576705921=%F0%9F%91%8D+Yes&entry.1234567890=${guideName}`;
    modal.style.display = "flex";
    thanks.style.display = "none";
  });

  noBtn.addEventListener("click", () => {
    iframe.src = `${baseURL}&entry.1576705921=%F0%9F%91%8E+No&entry.1234567890=${guideName}`;
    modal.style.display = "flex";
    thanks.style.display = "none";
  });

  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
    iframe.src = ""; // stop form from running in background
    thanks.style.display = "block"; // optional, show thanks after closing
  });

  // Optional: click outside modal content closes it
  modal.addEventListener("click", e => {
    if (e.target === modal) {
      modal.style.display = "none";
      iframe.src = "";
      thanks.style.display = "block";
    }
  });
});
