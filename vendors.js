let vendors = [];

fetch('data/vendors.json')
  .then(res => {
    if (!res.ok) throw new Error('Could not load vendors.json');
    return res.json();
  })
  .then(data => {
    vendors = data;
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

    card.innerHTML = `
      <div class="card-content">
        <h3>${vendor.vendor}</h3>

        <div class="badges" style="margin:8px 0;">
          <span class="badge asset">${vendor.category}</span>
        </div>

        <p><strong>Phone:</strong> <a href="tel:${vendor.phone}">${vendor.phone || 'N/A'}</a></p>
        <p><strong>Email:</strong> <a href="mailto:${vendor.email}">${vendor.email}</a></p>
        <p><strong>Website:</strong> <a href="${vendor.website}" target="_blank">${vendor.website}</a></p>
        <p><strong>Repair Portal:</strong> <a href="${vendor.portal}" target="_blank">${vendor.portal}</a></p>

        <p style="font-size:14px; color:#444;"><strong>Notes:</strong> ${vendor.notes}</p>
        <p style="font-size:14px; color:#666;"><strong>Related / Former Vendors:</strong> ${vendor.relatedVendors}</p>
      </div>
    `;

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
