document.addEventListener("DOMContentLoaded", () => {
  fetch("vendors.json")
    .then(response => response.json())
    .then(data => {
      const grid = document.getElementById("vendorGrid");

      data.forEach(vendor => {
        const card = document.createElement("div");
        card.className = "vendor-card";

        card.innerHTML = `
          <h3>${vendor.name}</h3>
          <p><strong>Equipment:</strong> ${vendor.equipment}</p>
          <p><strong>Phone:</strong> ${vendor.phone}</p>
          <p><strong>Email:</strong> ${vendor.email}</p>
        `;

        grid.appendChild(card);
      });
    })
    .catch(error => {
      console.error("Error loading vendors:", error);
    });
});
