// feedback.js

document.addEventListener("DOMContentLoaded", () => {

  const widgets = document.querySelectorAll(".guide-feedback");

  widgets.forEach(widget => {

    const yesBtn = widget.querySelector(".thumb-btn.yes");
    const noBtn = widget.querySelector(".thumb-btn.no");
    const form = widget.querySelector(".feedback-form");
    const thanks = widget.querySelector(".feedback-thanks");
    const iframe = widget.querySelector(".feedback-iframe");

    const guideName = widget.dataset.guide || "Unknown Guide";

    const baseFormURL = "https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform?embedded=true";

    // 👍 YES
    yesBtn.addEventListener("click", () => {
      widget.querySelector(".thumb-buttons").style.display = "none";
      thanks.style.display = "block";

      iframe.src = `${baseFormURL}&entry.YOUR_HELPFUL_ENTRY_ID=Yes&entry.YOUR_GUIDE_ENTRY_ID=${encodeURIComponent(guideName)}`;
    });

    // 👎 NO
    noBtn.addEventListener("click", () => {
      widget.querySelector(".thumb-buttons").style.display = "none";
      form.style.display = "block";

      iframe.src = `${baseFormURL}&entry.YOUR_GUIDE_ENTRY_ID=${encodeURIComponent(guideName)}`;
    });

  });

});
