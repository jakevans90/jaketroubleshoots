document.addEventListener("DOMContentLoaded", () => {
  const yesBtn = document.querySelector(".thumb-btn.yes");
  const noBtn = document.querySelector(".thumb-btn.no");

  if (!yesBtn || !noBtn) return;

  // Grab guide title from <title> tag
  let guideName = document.title;

  // Optional: remove extra description after " - "
  if (guideName.includes(" - ")) {
    guideName = guideName.split(" - ")[0]; // keeps "3M Bair Hugger 775 Series"
  }

  const guideEntryId = "826310226"; // your Google Form Guide Name entry ID

  yesBtn.addEventListener("click", () => {
    const url =
      `https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform?usp=pp_url&entry.1576705921=%F0%9F%91%8D+Yes&entry.${guideEntryId}=${encodeURIComponent(guideName)}`;
    window.open(url, "_blank");
  });

  noBtn.addEventListener("click", () => {
    const url =
      `https://docs.google.com/forms/d/e/1FAIpQLSfcgW_n0cunK0HfeiWh2HjBGCHnhK0QI_V1gak_eQv_9rMfNw/viewform?usp=pp_url&entry.1576705921=%F0%9F%91%8E+No&entry.${guideEntryId}=${encodeURIComponent(guideName)}`;
    window.open(url, "_blank");
  });
});
