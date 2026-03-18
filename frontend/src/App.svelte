<script>
  import CommandPalette from './lib/CommandPalette.svelte'
</script>

<main class="flex min-h-screen flex-col items-center justify-center bg-gray-950 px-4">
  <h1 class="mb-2 bg-gradient-to-r from-violet-400 to-indigo-400 bg-clip-text text-5xl font-extrabold tracking-tight text-transparent">
    API-MindBot
  </h1>
  <p class="text-gray-400">
    Stlač <kbd class="rounded border border-white/20 bg-white/10 px-1.5 py-0.5 text-sm font-medium text-gray-300">CMD + K</kbd>
    <span class="text-gray-600">/</span>
    <kbd class="rounded border border-white/20 bg-white/10 px-1.5 py-0.5 text-sm font-medium text-gray-300">Ctrl + K</kbd>
  </p>
  <CommandPalette />
</main>
