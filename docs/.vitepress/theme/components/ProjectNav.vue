<script setup>
import { computed } from 'vue'
import { useRoute } from 'vitepress'
import data from '../data/projects.json'
import { useLocale, UI } from '../composables/useLocale'

const route = useRoute()
const { L, base } = useLocale()
const list = data.projects

const idx = computed(() => {
  const path = route.path.replace(/\.html$/, '').replace(/\/$/, '')
  return list.findIndex((p) => path.endsWith('/' + p.slug))
})
const prev = computed(() => (idx.value > 0 ? list[idx.value - 1] : null))
const next = computed(() => (idx.value >= 0 && idx.value < list.length - 1 ? list[idx.value + 1] : null))

const href = (p) => `${base.value}/projects/${p.slug}`
</script>

<template>
  <div v-if="prev || next" class="pnav">
    <a v-if="prev" class="pnav__item pnav__item--prev" :href="href(prev)">
      <span class="pnav__label">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">
          <path d="M19 12H6M11 6l-6 6 6 6" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        {{ L(UI.prev.en, UI.prev.zh) }}
      </span>
      <span class="pnav__name">{{ prev.name }}</span>
      <span class="pnav__tag">{{ L(prev.en.tagline, prev.zh.tagline) }}</span>
    </a>
    <span v-else class="pnav__spacer" />

    <a v-if="next" class="pnav__item pnav__item--next" :href="href(next)">
      <span class="pnav__label">
        {{ L(UI.next.en, UI.next.zh) }}
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">
          <path d="M5 12h13M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </span>
      <span class="pnav__name">{{ next.name }}</span>
      <span class="pnav__tag">{{ L(next.en.tagline, next.zh.tagline) }}</span>
    </a>
  </div>
</template>

<style scoped>
.pnav {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-top: 44px;
  padding-top: 24px;
  border-top: 1px solid var(--vp-c-divider);
}

.pnav__item {
  display: flex;
  flex-direction: column;
  gap: 3px;
  padding: 14px 16px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  text-decoration: none;
  background: var(--vp-c-bg-soft);
  transition: transform .18s, border-color .18s, box-shadow .18s;
}

.pnav__item:hover {
  transform: translateY(-2px);
  border-color: var(--ms-accent);
  box-shadow: 0 8px 22px -14px var(--ms-accent);
}

.pnav__item--next {
  text-align: right;
  align-items: flex-end;
}

.pnav__label {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 11.5px;
  font-weight: 650;
  color: var(--vp-c-text-3);
  letter-spacing: .02em;
}

.pnav__name {
  font-size: 14.5px;
  font-weight: 680;
  color: var(--vp-c-text-1);
}

.pnav__tag {
  font-size: 12.5px;
  color: var(--vp-c-text-2);
  line-height: 1.5;
}

@media (max-width: 640px) {
  .pnav {
    grid-template-columns: 1fr;
  }

  .pnav__item--next {
    text-align: left;
    align-items: flex-start;
  }

  .pnav__spacer {
    display: none;
  }
}
</style>
