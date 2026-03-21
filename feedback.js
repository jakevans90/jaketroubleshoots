document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".thumb-btn.yes");
  const noBtn = document.querySelector(".thumb-btn.no");

  if (!yesBtn || !noBtn) return;

  const guideName =
    document.querySelector(".hero h2")?.textContent ||
    document.title ||
    "Unknown Guide";

  // 🔑 Your actual working base
  const base =
    "https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform?usp=pp_url";

  const yesBtnHandler = () => {
    const url =
      `${base}&entry.1576705921=👍+Yes&entry.GUIDE_ID=` +
      encodeURIComponent(guideName);

    window.open(url, "_blank");
  };

  const noBtnHandler = () => {
    const url =
      `${base}&entry.1576705921=👎+No&entry.GUIDE_ID=` +
      encodeURIComponent(guideName);

    window.open(url, "_blank");
  };

  yesBtn.addEventListener("click", yesBtnHandler);
  noBtn.addEventListener("click", noBtnHandler);
});
