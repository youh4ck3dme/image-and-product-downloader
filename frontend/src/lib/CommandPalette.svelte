<script lang="ts">
  let open = $state(false);
  let query = $state('');

  function focusOnMount(node: HTMLElement) {
    node.focus();
  }

  const commands = [
    { id: 'download-images', label: 'Download Images', description: 'Download images from a URL' },
    { id: 'extract-products', label: 'Extract Products', description: 'Extract product info from a URL' },
    { id: 'download-both', label: 'Download Images & Products', description: 'Download images and extract products' },
  ];

  const filtered = $derived(
    query.trim() === ''
      ? commands
      : commands.filter(
          (c) =>
            c.label.toLowerCase().includes(query.toLowerCase()) ||
            c.description.toLowerCase().includes(query.toLowerCase())
        )
  );

  function toggle() {
    open = !open;
    if (!open) query = '';
  }

  function handleKey(e: KeyboardEvent) {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      toggle();
    }
    if (e.key === 'Escape') {
      open = false;
      query = '';
    }
  }
</script>

<svelte:window onkeydown={handleKey} />

{#if open}
  <!-- backdrop -->
  <div
    class="fixed inset-0 z-40 bg-black/40 backdrop-blur-sm"
    role="button"
    tabindex="-1"
    aria-label="Close command palette"
    onclick={toggle}
    onkeydown={(e) => e.key === 'Enter' && toggle()}
  ></div>

  <!-- palette -->
  <div
    class="fixed left-1/2 top-1/3 z-50 w-full max-w-lg -translate-x-1/2 -translate-y-1/2 rounded-2xl border border-white/10 bg-gray-900 shadow-2xl"
    role="dialog"
    aria-modal="true"
    aria-label="Command palette"
  >
    <div class="flex items-center gap-3 border-b border-white/10 px-4 py-3">
      <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-4.35-4.35M17 11A6 6 0 1 1 5 11a6 6 0 0 1 12 0z" />
      </svg>
      <input
        class="flex-1 bg-transparent text-white placeholder-gray-500 outline-none"
        type="text"
        placeholder="Type a command…"
        bind:value={query}
        use:focusOnMount
      />
      <kbd class="rounded border border-white/20 bg-white/10 px-1.5 py-0.5 text-xs text-gray-400">Esc</kbd>
    </div>

    <ul class="max-h-72 overflow-y-auto py-2">
      {#each filtered as cmd (cmd.id)}
        <li>
          <button
            class="flex w-full flex-col gap-0.5 px-4 py-3 text-left hover:bg-white/10 focus:bg-white/10 focus:outline-none"
            onclick={toggle}
          >
            <span class="font-medium text-white">{cmd.label}</span>
            <span class="text-sm text-gray-400">{cmd.description}</span>
          </button>
        </li>
      {/each}
      {#if filtered.length === 0}
        <li class="px-4 py-6 text-center text-gray-500">No commands found.</li>
      {/if}
    </ul>
  </div>
{/if}
