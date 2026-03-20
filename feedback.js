document.addEventListener("DOMContentLoaded", () => {
  // Grab all feedback widgets (you'll have one per page)
  const widgets = document.querySelectorAll(".guide-feedback");

  widgets.forEach(widget => {
    const yesBtn = widget.querySelector(".thumb-btn.yes");
    const noBtn = widget.querySelector(".thumb-btn.no");
    const form = widget.querySelector(".feedback-form");
    const thanks = widget.querySelector(".feedback-thanks");
    const iframe = widget.querySelector(".feedback-iframe");

    // Auto-detect guide name
    let guideName = document.querySelector("h2")?.textContent // pick your main guide heading
                    || document.title
                    || "Unknown Guide";

    const baseFormURL = "https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform?embedded=true";

    yesBtn.addEventListener("click", () => {
      widget.querySelector(".thumb-buttons").style.display = "none";
      thanks.style.display = "block";
      iframe.src = `${baseFormURL}&entry.YOUR_HELPFUL_ENTRY_ID=Yes&entry.YOUR_GUIDE_ENTRY_ID=${encodeURIComponent(guideName)}`;
    });

    noBtn.addEventListener("click", () => {
      widget.querySelector(".thumb-buttons").style.display = "none";
      form.style.display = "block";
      iframe.src = `${baseFormURL}&entry.YOUR_GUIDE_ENTRY_ID=${encodeURIComponent(guideName)}`;
    });
  });
});
