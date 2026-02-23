let vendors = [];

fetch('data/vendors.json')
  .then(res => {
    if (!res.ok) throw new Error('Could not load vendors.json');
    return res.json();
  })
  .then(data => {
    vendors = data;
    vendors.sort((a, b) => a.vendor.localeCompare(b.vendor));
renderVendors(vendors);
  })
  .catch(err => console.error('Vendor load error:', err));

const searchInput = document.getElementById('vendor-search-input');
const noResults = document.getElementById('no-vendor-results');

function renderVendors(list) {
  const container = document.getElementById('vendors-grid');
  container.innerHTML = '';

  if (list.length === 0) {
    noResults.style.display = 'block';
    return;
  } else {
    noResults.style.display = 'none';
  }

  list.forEach(vendor => {
    const card = document.createElement('div');
    card.classList.add('guide-card', 'vendor-card');

    // Build the inner HTML dynamically, only include fields that exist
    let html = `<div class="card-content">
                  <h3>${vendor.vendor}</h3>`;

    if (vendor.category) html += `<p><strong>Category:</strong> ${vendor.category}</p>`;
    if (vendor.phone) {
      html += `<p><strong>Phone:</strong> <a href="tel:${vendor.phone.replace(/\s+/g, '')}">${vendor.phone}</a></p>`;
      }
    if (vendor.email) html += `<p><strong>Email:</strong> <a href="mailto:${vendor.email}">${vendor.email}</a></p>`;
    if (vendor.website) html += `<p><strong>Website:</strong> <a href="${vendor.website}" target="_blank">${vendor.website}</a></p>`;
    if (vendor.portal) html += `<p><strong>Repair Portal:</strong> <a href="${vendor.portal}" target="_blank">${vendor.portal}</a></p>`;
    if (vendor.notes) html += `<p><strong>Notes:</strong> ${vendor.notes}</p>`;
    if (vendor.relatedVendors) html += `<p><strong>Related / Former Vendors:</strong> ${vendor.relatedVendors}</p>`;

    html += `</div>`; // close card-content

    card.innerHTML = html;
    container.appendChild(card);
  });
}

/* Live search */
searchInput.addEventListener('input', e => {
  const term = e.target.value.toLowerCase();

  const filtered = vendors.filter(v =>
    v.vendor?.toLowerCase().includes(term) ||
    v.category?.toLowerCase().includes(term) ||
    v.notes?.toLowerCase().includes(term) ||
    v.relatedVendors?.toLowerCase().includes(term)
  );

  renderVendors(filtered);
});
