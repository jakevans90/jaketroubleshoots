document.addEventListener("DOMContentLoaded", () => {
  const widget = document.querySelector(".guide-feedback");
  if (!widget) return;

  const yesBtn = widget.querySelector(".thumb-btn.yes");
  const noBtn = widget.querySelector(".thumb-btn.no");
  const buttons = widget.querySelector(".thumb-buttons");
  const thanks = widget.querySelector(".feedback-thanks");

  // Get guide name automatically
  const guideName =
    document.querySelector(".hero h2")?.textContent ||
    document.title ||
    "Unknown Guide";

  // Your Google Form (KEEP embedded=true — important)
  const formURL =
    "https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform?embedded=true";

  if (!yesBtn || !noBtn) return;

  // 👍 YES
  yesBtn.addEventListener("click", () => {
    buttons.style.display = "none";
    thanks.style.display = "block";

    // (Optional future upgrade: send "Yes" silently)
    console.log("Helpful:", guideName);
  });

  // 👎 NO
  noBtn.addEventListener("click", () => {
    // Open form in new tab (works reliably)
    window.open(formURL, "_blank");

    // Optional: hide buttons after click
    buttons.style.display = "none";
  });
});
