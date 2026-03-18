# Image and Product Downloader

A full-stack tool for downloading images and extracting product information from websites.

- **Python CLI / library** — scrape images and product data from any URL
- **Hono.js REST API** (`backend/`) — Node.js backend serving the data over HTTP
- **Svelte frontend** (`frontend/`) — command-palette UI (API-MindBot) to trigger downloads from the browser

---

## Quick start

### Run everything at once

```bash
npm install          # installs root dev deps (concurrently)
npm run dev          # starts backend (port 3000) and frontend (port 5173) in parallel
```

### Python CLI only

```bash
pip install -r requirements.txt

# Download images
python downloader.py --url "https://example.com" --mode images

# Extract products
python downloader.py --url "https://example.com" --mode products

# Download images and extract products
python downloader.py --url "https://example.com" --mode both --output downloads/
```

---

## Project structure

```
image-and-product-downloader/
├── backend/                    # Hono.js REST API (Node.js / TypeScript)
│   ├── src/
│   │   └── index.ts            # Express-like Hono server on port 3000
│   └── package.json
├── frontend/                   # Svelte 5 + Tailwind CSS (Vite)
│   ├── src/
│   │   ├── lib/
│   │   │   └── CommandPalette.svelte  # CMD+K command palette
│   │   ├── App.svelte
│   │   └── main.ts
│   └── package.json
├── downloader.py               # Python scraping library + CLI
├── example_usage.py            # Usage examples for the Python library
├── test_downloader.py          # Unit tests for the Python library
├── test_installation.py        # Dependency verification script
├── requirements.txt            # Python dependencies
├── package.json                # Root workspace (concurrently dev script)
└── README.md
```

---

## Python library

### Installation

```bash
pip install -r requirements.txt
```

Requirements: Python 3.7+, `requests`, `beautifulsoup4`, `lxml`

### Usage as a library

```python
from downloader import ImageDownloader, ProductDownloader

# Download images
downloader = ImageDownloader(output_dir="downloads")
paths = downloader.download_images("https://example.com/products", max_images=20)

# Extract products
product_downloader = ProductDownloader()
products = product_downloader.extract_products("https://example.com/shop")
for p in products:
    print(p)
```

### CLI reference

```
python downloader.py --url URL [--mode images|products|both] [--output DIR] [--max-images N]
```

| Flag | Default | Description |
|------|---------|-------------|
| `--url` | *(required)* | Page URL to scrape |
| `--mode` | `images` | What to download: `images`, `products`, or `both` |
| `--output` | `downloads` | Output directory for images |
| `--max-images` | unlimited | Cap on number of images downloaded |

---

## Backend (Hono.js)

A lightweight REST API built with [Hono](https://hono.dev/) — a fast, edge-compatible web framework for Node.js — served via `@hono/node-server`.

```bash
cd backend
npm install
npm run dev    # http://localhost:3000
```

**Endpoints**

| Method | Path | Response |
|--------|------|----------|
| GET | `/` | `{ "message": "Image and Product Downloader API" }` |

---

## Frontend (Svelte + Tailwind)

Command-palette UI that communicates with the backend.

```bash
cd frontend
npm install
npm run dev    # http://localhost:5173
```

Press **CMD + K** / **Ctrl + K** to open the command palette.

See [`frontend/README.md`](frontend/README.md) for full frontend documentation.

---

## Testing

### Python tests

```bash
# Verify dependencies
python test_installation.py

# Run unit tests
python test_downloader.py
```

---

## License

This project is provided as-is for educational purposes.

