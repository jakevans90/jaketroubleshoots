const fs = require("fs");
const path = require("path");

console.log("Script started");

const root = process.cwd();
const baseUrl = "https://jaketroubleshoots.com";
let count = 0;

function walk(dir) {
  for (const file of fs.readdirSync(dir)) {
    const full = path.join(dir, file);
    const stat = fs.statSync(full);

    if (stat.isDirectory()) {
      if (file === ".git" || file === "node_modules") continue;
      walk(full);
    } else if (file.endsWith(".html")) {
      addCanonical(full);
    }
  }
}

function addCanonical(filePath) {
  let html = fs.readFileSync(filePath, "utf8");
  const relative = path.relative(root, filePath).replace(/\\/g, "/");

  const url = relative === "index.html"
    ? `${baseUrl}/`
    : `${baseUrl}/${relative}`;

  const canonical = `<link rel="canonical" href="${url}" />`;

  if (html.includes('rel="canonical"') || html.includes("rel='canonical'")) {
    html = html.replace(/<link\s+rel=["']canonical["'][^>]*>/i, canonical);
  } else if (html.includes("</head>")) {
    html = html.replace("</head>", `  ${canonical}\n</head>`);
  } else {
    console.log(`Skipped no </head>: ${relative}`);
    return;
  }

  fs.writeFileSync(filePath, html);
  count++;
}

walk(root);

console.log(`Done. Updated ${count} HTML files.`);
