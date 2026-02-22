<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Vendors | Jake Troubleshoots</title>
  <link rel="stylesheet" href="style.css">

  <!-- Favicon -->
  <link rel="icon" type="image/x-icon" href="images/favicon.ico">
  <link rel="icon" type="image/png" href="images/favicon.png">

  <style>
    #vendor-search-form {
      margin-top: 20px;
      display: flex;
      justify-content: center;
      gap: 5px;
      flex-wrap: wrap;
    }

    #vendor-search-input {
      padding: 12px 16px;
      font-size: 16px;
      border-radius: 6px;
      border: 1px solid #ccc;
      width: 300px;
      min-width: 200px;
      box-sizing: border-box;
    }

    #vendor-search-form button {
      padding: 12px 16px;
      font-size: 16px;
      border-radius: 6px;
      border: none;
      background: #111;
      color: white;
      cursor: pointer;
      transition: background 0.2s;
    }

    #vendor-search-form button:hover {
      background: #333;
    }
  </style>
</head>
<body>

<header>
  <a href="index.html" class="site-logo">
    <img src="images/logo.png" alt="Jake Troubleshoots Logo" class="site-icon">
    <span class="logo-text">Jake Troubleshoots</span>
  </a>

  <nav>
    <a href="index.html">Home</a>
    <a href="guides.html">Guides</a>
    <a href="search.html">Search</a>
    <a href="vendors.html">Vendors</a>
    <a href="contact.html">Contact</a>
  </nav>
</header>

<section class="hero">
  <h2>Vendors</h2>
  <p>A growing rolodex of vendor tech support contact information.</p>

  <form id="vendor-search-form">
    <input type="text" id="vendor-search-input" placeholder="Search vendors...">
    <button type="submit">Search</button>
  </form>
</section>

<section style="padding:40px; text-align:center;">
  <div id="vendors-grid" class="guides-grid" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:20px; justify-items:center;">
    <!-- Vendor cards injected here -->
  </div>
</section>

<footer>
  <p>Contact: <a href="mailto:contact@jaketroubleshoots.com" style="color:#8fff00;">contact@jaketroubleshoots.com</a></p>
  <p>Guides intended for trained personnel only.</p>
  <p>© 2026 Jake Troubleshoots</p>
</footer>

<script src="vendors.js"></script>

</body>
</html>
