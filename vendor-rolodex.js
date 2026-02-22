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

    let contactsHTML = '';
    vendor.contacts.forEach(c => {
      contactsHTML += `
        <div class="contact-block">
          <strong>${c.name}</strong> (${c.role})<br>
          📞 ${c.phone}<br>
          ✉️ ${c.email}<br>
          📝 ${c.notes}
        </div>
      `;
    });

    card.innerHTML = `
      <div class="vendor-title">${vendor.vendor}</div>
      <div class="vendor-category">${vendor.category}</div>
      ${contactsHTML}
    `;

    container.appendChild(card);
  });
}

document.getElementById('vendor-search').addEventListener('input', e => {
  const term = e.target.value.toLowerCase();

  const filtered = vendors.filter(v =>
    v.vendor.toLowerCase().includes(term) ||
    v.category.toLowerCase().includes(term) ||
    JSON.stringify(v.contacts).toLowerCase().includes(term)
  );

  displayVendors(filtered);
});
