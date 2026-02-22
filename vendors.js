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
  const container = document.getElementById('vendors-grid');
  container.innerHTML = '';

  list.forEach(vendor => {
    const card = document.createElement('div');
    card.classList.add('guide-card');

    card.innerHTML = `
      <div class="card-content">
        <h3>${vendor.vendor}</h3>
        <p><strong>Category:</strong> ${vendor.category}</p>

        <p><strong>Phone:</strong> ${vendor.phone || 'N/A'}</p>
        <p><strong>Email:</strong> ${vendor.email || 'N/A'}</p>
        <p><strong>Website:</strong> <a href="${vendor.website}" target="_blank">${vendor.website}</a></p>
        <p><strong>Repair Portal:</strong> <a href="${vendor.portal}" target="_blank">${vendor.portal}</a></p>

        <p><strong>Notes:</strong> ${vendor.notes}</p>
        <p><strong>Related / Former Vendors:</strong> ${vendor.relatedVendors}</p>
      </div>
    `;

    container.appendChild(card);
  });
}

const form = document.getElementById('vendor-search-form');
form.addEventListener('submit', e => {
  e.preventDefault();
  const term = document.getElementById('vendor-search-input').value.toLowerCase();

  const filtered = vendors.filter(v =>
    v.vendor.toLowerCase().includes(term) ||
    v.category.toLowerCase().includes(term) ||
    v.notes.toLowerCase().includes(term) ||
    v.relatedVendors.toLowerCase().includes(term)
  );

  displayVendors(filtered);
});
