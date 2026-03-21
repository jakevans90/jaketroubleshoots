document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".thumb-btn.yes");
  const noBtn = document.querySelector(".thumb-btn.no");

  if (!yesBtn || !noBtn) return;

  // Get guide name automatically
  const guideName =
    document.querySelector(".hero h2")?.textContent ||
    document.title ||
    "Unknown Guide";

  // 🔑 REPLACE THESE with your actual prefill links
  const yesBase =
    "https://docs.google.com/forms/d/e/FORM_ID/viewform?usp=pp_url&entry.HELPFUL=Yes&entry.GUIDE=";

  const noBase =
    "https://docs.google.com/forms/d/e/FORM_ID/viewform?usp=pp_url&entry.HELPFUL=No&entry.GUIDE=";

  yesBtn.addEventListener("click", () => {
    window.open(yesBase + encodeURIComponent(guideName), "_blank");
  });

  noBtn.addEventListener("click", () => {
    window.open(noBase + encodeURIComponent(guideName), "_blank");
  });
});
