<script lang="ts">
  let open = $state(false);
  let query = $state('');
  let message = $state('');
  let loading = $state(false);
  let inputEl = $state<HTMLInputElement | null>(null);

  $effect(() => {
    if (open && inputEl) {
      inputEl.focus();
    }
  });

  function close() {
    open = false;
    query = '';
    message = '';
  }

  function handleWindowKey(e: KeyboardEvent) {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      if (open) {
        close();
      } else {
        open = true;
      }
    }
    if (e.key === 'Escape' && open) {
      close();
    }
  }

  async function handleEnter(e: KeyboardEvent) {
    if (e.key !== 'Enter' || !query.trim() || loading) return;
    loading = true;
    message = '';
    try {
      const res = await fetch('http://localhost:3000/api/command', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command: query.trim() }),
      });
      if (res.ok) {
        const data = await res.json();
        message = data.message ?? '';
      } else {
        message = `Error: ${res.status} ${res.statusText}`;
      }
    } catch (err) {
      console.error('[CommandPalette] fetch error:', err);
      message = 'Could not reach the server. Is it running on port 3000?';
    } finally {
      loading = false;
    }
  }
</script>

<svelte:window onkeydown={handleWindowKey} />

{#if open}
  <!-- backdrop -->
  <div
    class="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm"
    role="button"
    tabindex="-1"
    aria-label="Close command palette"
    onclick={close}
    onkeydown={(e) => e.key === 'Enter' && close()}
  ></div>

  <!-- palette -->
  <div
    class="fixed left-1/2 top-1/3 z-50 w-full max-w-lg -translate-x-1/2 -translate-y-1/2 rounded-2xl border border-white/10 bg-gray-900/80 shadow-2xl ring-1 ring-white/5 backdrop-blur-xl"
    role="dialog"
    aria-modal="true"
    aria-label="Command palette"
  >
    <!-- input row -->
    <div class="flex items-center gap-3 px-4 py-3">
      {#if loading}
        <svg class="h-5 w-5 animate-spin text-violet-400" fill="none" viewBox="0 0 24 24" aria-hidden="true">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"></path>
        </svg>
      {:else}
        <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-4.35-4.35M17 11A6 6 0 1 1 5 11a6 6 0 0 1 12 0z" />
        </svg>
      {/if}
      <input
        bind:this={inputEl}
        bind:value={query}
        onkeydown={handleEnter}
        class="flex-1 bg-transparent text-white placeholder-gray-500 outline-none"
        type="text"
        placeholder="Type a command and press Enter…"
        autocomplete="off"
        spellcheck="false"
      />
      <kbd class="rounded border border-white/20 bg-white/10 px-1.5 py-0.5 text-xs text-gray-400">Esc</kbd>
    </div>

    <!-- response message -->
    {#if message}
      <div class="border-t border-white/10 px-4 py-4">
        <p class="whitespace-pre-wrap text-sm leading-relaxed text-gray-200">{message}</p>
      </div>
    {/if}
  </div>
{/if}
