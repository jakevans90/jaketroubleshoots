let vendors = [];

fetch('data/vendors.json')
  .then(res => {
    if (!res.ok) throw new Error('Could not load vendors.json');
    return res.json();
  })
  .then(data => {
    vendors = data;
    displayVendors(vendors);
  })
  .catch(err => console.error('Vendor load error:', err));

function displayVendors(list) {
  const container = document.getElementById('vendor-list');
  container.innerHTML = '';

  list.forEach(vendor => {
    const card = document.createElement('div');
    card.className = 'vendor-card';

    card.innerHTML = `
      <div class="vendor-title">${vendor.vendor}</div>
      <div class="vendor-category">${vendor.category}</div>

      <div class="vendor-field"><strong>Phone:</strong> ${vendor.phone || 'N/A'}</div>
      <div class="vendor-field"><strong>Email:</strong> ${vendor.email || 'N/A'}</div>
      <div class="vendor-field"><strong>Website:</strong> <a href="${vendor.website}" target="_blank">${vendor.website}</a></div>
      <div class="vendor-field"><strong>Repair Portal:</strong> <a href="${vendor.portal}" target="_blank">${vendor.portal}</a></div>
      <div class="vendor-field"><strong>Notes:</strong> ${vendor.notes}</div>

      <div class="related-vendors"><strong>Related / Former Vendors:</strong> ${vendor.relatedVendors}</div>
    `;

    container.appendChild(card);
  });
}

document.getElementById('vendor-search').addEventListener('input', e => {
  const term = e.target.value.toLowerCase();

  const filtered = vendors.filter(v =>
    v.vendor.toLowerCase().includes(term) ||
    v.category.toLowerCase().includes(term) ||
    v.notes.toLowerCase().includes(term) ||
    v.relatedVendors.toLowerCase().includes(term)
  );

  displayVendors(filtered);
});
