# API-MindBot — Frontend

Svelte 5 + TypeScript + Vite + Tailwind CSS frontend for the API-MindBot command palette UI.

## Stack

| Tool | Purpose |
|------|---------|
| [Svelte 5](https://svelte.dev/) | UI framework (uses runes) |
| [TypeScript](https://www.typescriptlang.org/) | Type-safe JavaScript |
| [Vite](https://vitejs.dev/) | Dev server & bundler |
| [Tailwind CSS v3](https://tailwindcss.com/) | Utility-first styling |

## Getting started

```bash
# From the project root (recommended — runs backend + frontend together)
npm run dev

# Or run the frontend alone
cd frontend
npm install
npm run dev        # http://localhost:5173
```

## Available scripts

| Script | Description |
|--------|-------------|
| `npm run dev` | Start Vite dev server with HMR |
| `npm run build` | Type-check and build for production (`dist/`) |
| `npm run preview` | Preview the production build locally |
| `npm run check` | Run `svelte-check` + `tsc` type checks |

## Project layout

```
frontend/
├── public/
│   └── favicon.svg          # App favicon
├── src/
│   ├── lib/
│   │   └── CommandPalette.svelte  # CMD+K modal command palette
│   ├── App.svelte            # Root component
│   ├── app.css               # Tailwind directives + global reset
│   └── main.ts               # Svelte entry point
├── index.html                # HTML shell
├── vite.config.ts
├── tailwind.config.js
└── tsconfig.app.json
```

## Usage

Open the app in the browser and press **CMD + K** (macOS) or **Ctrl + K** (Windows/Linux) to open the command palette. Type to filter commands, press **Esc** to close.
