<script setup>
import { ref, computed } from 'vue'
import data from '../data/projects.json'
import { useLocale, UI } from '../composables/useLocale'

const { L, isZh, base } = useLocale()

const layers = data.layers
const projects = data.projects

const active = ref(null)
const hovered = ref(null)

const focus = computed(() => hovered.value || active.value)

const bands = computed(() =>
  layers.map((l) => ({
    ...l,
    label: l[isZh.value ? 'zh' : 'en'],
    items: projects.filter((p) => p.layer === l.id),
  }))
)

function isDim(p) {
  if (!focus.value || p.slug === focus.value) return false
  const p0 = projects.find((x) => x.slug === focus.value)
  return p0 ? p0.layer !== p.layer : false
}

const isHot = (p) => p.slug === focus.value

const focused = computed(() => projects.find((p) => p.slug === focus.value) || null)
const focusedLayer = computed(() =>
  focused.value ? layers.find((l) => l.id === focused.value.layer) : null
)
const focusedFeatures = computed(() => {
  if (!focused.value) return []
  return (isZh.value ? focused.value.zh : focused.value.en).features.slice(0, 5)
})
const detailHref = computed(() => (focused.value ? `${base.value}/projects/${focused.value.slug}` : '#'))
</script>

<template>
  <div class="arch">
    <div class="arch__legend">
      <span class="arch__hint">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="7" />
          <path d="M20 20l-3.5-3.5" stroke-linecap="round" />
        </svg>
        {{ L(UI.hint.en, UI.hint.zh) }}
      </span>
      <button v-if="active" class="arch__clear" @click="active = null">{{ L(UI.clear.en, UI.clear.zh) }}</button>
    </div>

    <div class="arch__stack">
      <div v-for="(band, bi) in bands" :key="band.id" class="band" :class="`band--${band.id}`">
        <div class="band__rail">
          <span class="band__code">{{ 'L' + bi }}</span>
          <span class="band__title">{{ band.label }}</span>
        </div>
        <div class="band__body">
          <a v-for="p in band.items" :key="p.slug" class="chip"
            :class="{ 'chip--hot': isHot(p), 'chip--dim': isDim(p), 'chip--star': p.stars >= 10 }"
            :href="`${base}/projects/${p.slug}`" @mouseenter="hovered = p.slug" @mouseleave="hovered = null"
            @click="active = active === p.slug ? null : p.slug">
            <span class="chip__dot" />
            <span class="chip__name">{{ p.name.replace('Microsphere ', '') }}</span>
            <span v-if="p.stars >= 10" class="chip__star">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2l2.9 6.3 6.9.8-5.1 4.7 1.4 6.8L12 17.3 5.9 20.6l1.4-6.8L2.2 9.1l6.9-.8L12 2z" />
              </svg>
              {{ p.stars }}
            </span>
          </a>
        </div>
        <div v-if="bi < bands.length - 1" class="band__flow" aria-hidden="true">
          <svg width="26" height="34" viewBox="0 0 26 34">
            <path d="M13 2v24" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="3 4" />
            <path d="M7 22l6 7 6-7" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"
              stroke-linejoin="round" />
          </svg>
        </div>
      </div>
    </div>

    <transition name="fade">
      <div v-if="focused" class="arch__detail">
        <div class="arch__detail-head">
          <span class="arch__pill">{{ focused.name }}</span>
          <span class="arch__layer">{{ focusedLayer ? focusedLayer[isZh ? 'zh' : 'en'] : '' }}</span>
        </div>
        <p class="arch__tagline">{{ L(focused.en.tagline, focused.zh.tagline) }}</p>
        <ul class="arch__feats">
          <li v-for="f in focusedFeatures" :key="f[0]">
            <strong>{{ f[0] }}</strong> — {{ f[1] }}
          </li>
        </ul>
        <a class="arch__cta" :href="detailHref">
          {{ L(UI.viewProject.en, UI.viewProject.zh) }}
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">
            <path d="M5 12h13M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </a>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.arch {
  margin: 32px 0 8px;
}

.arch__legend {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 18px;
}

.arch__hint {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 13px;
  color: var(--vp-c-text-2);
}

.arch__clear {
  font-size: 12px;
  color: var(--vp-c-text-2);
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  padding: 4px 12px;
  cursor: pointer;
  transition: all .2s;
}

.arch__clear:hover {
  color: var(--ms-accent);
  border-color: var(--ms-accent);
}

.arch__stack {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.band {
  position: relative;
  width: 100%;
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  background: linear-gradient(135deg, var(--ms-band-from), var(--ms-band-to));
  padding: 16px 18px;
  transition: border-color .25s, box-shadow .25s;
}

.band:hover {
  border-color: var(--ms-band-edge);
}

.band--foundation {
  --ms-band-from: rgba(148, 163, 184, .10);
  --ms-band-to: rgba(148, 163, 184, .02);
  --ms-band-edge: rgba(148, 163, 184, .45);
  --ms-chip: #64748b;
}

.band--runtime {
  --ms-band-from: rgba(56, 189, 248, .12);
  --ms-band-to: rgba(56, 189, 248, .02);
  --ms-band-edge: rgba(56, 189, 248, .5);
  --ms-chip: #0ea5e9;
}

.band--framework {
  --ms-band-from: rgba(129, 110, 245, .14);
  --ms-band-to: rgba(129, 110, 245, .02);
  --ms-band-edge: rgba(129, 110, 245, .55);
  --ms-chip: #7c5cf0;
}

.band--integration {
  --ms-band-from: rgba(16, 185, 129, .12);
  --ms-band-to: rgba(16, 185, 129, .02);
  --ms-band-edge: rgba(16, 185, 129, .5);
  --ms-chip: #10b981;
}

.band--crosscutting {
  --ms-band-from: rgba(245, 158, 11, .12);
  --ms-band-to: rgba(245, 158, 11, .02);
  --ms-band-edge: rgba(245, 158, 11, .5);
  --ms-chip: #f59e0b;
}

.band__rail {
  display: flex;
  align-items: baseline;
  gap: 10px;
  margin-bottom: 12px;
}

.band__code {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--ms-chip);
  border: 1px solid var(--ms-chip);
  border-radius: 5px;
  padding: 2px 6px;
  opacity: .9;
}

.band__title {
  font-size: 14px;
  font-weight: 650;
  color: var(--vp-c-text-1);
  letter-spacing: .01em;
}

.band__body {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.chip {
  --dot: var(--ms-chip);
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 6px 12px 6px 10px;
  border-radius: 10px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  font-size: 13px;
  font-weight: 550;
  color: var(--vp-c-text-1);
  text-decoration: none;
  cursor: pointer;
  transition: transform .18s cubic-bezier(.2, .8, .3, 1), box-shadow .18s, border-color .18s, opacity .18s;
}

.chip:hover {
  transform: translateY(-2px);
  border-color: var(--dot);
  box-shadow: 0 6px 18px -8px var(--dot);
}

.chip--hot {
  border-color: var(--dot);
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--dot) 18%, transparent);
  transform: translateY(-2px);
  opacity: 1 !important;
}

.chip--dim {
  opacity: .32;
}

.chip__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--dot);
  flex: none;
}

.chip--star .chip__dot {
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--dot) 22%, transparent);
}

.chip__star {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 11px;
  font-weight: 600;
  color: var(--vp-c-text-3);
  padding-left: 2px;
}

.band__flow {
  color: var(--vp-c-text-3);
  display: flex;
  justify-content: center;
  padding: 4px 0 2px;
  opacity: .55;
}

.arch__detail {
  margin-top: 20px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 14px;
  padding: 18px 20px;
  background: var(--vp-c-bg-soft);
}

.arch__detail-head {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 8px;
}

.arch__pill {
  font-size: 14px;
  font-weight: 700;
  color: var(--vp-c-text-1);
}

.arch__layer {
  font-size: 11px;
  color: var(--vp-c-text-2);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  padding: 2px 9px;
}

.arch__tagline {
  margin: 0 0 10px;
  font-size: 14px;
  color: var(--vp-c-text-2);
}

.arch__feats {
  margin: 0 0 14px;
  padding-left: 18px;
  font-size: 13px;
  line-height: 1.75;
  color: var(--vp-c-text-2);
}

.arch__feats strong {
  color: var(--vp-c-text-1);
  font-weight: 620;
}

.arch__cta {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 600;
  color: #fff;
  background: linear-gradient(120deg, #7c5cf0, #0ea5e9);
  padding: 8px 15px;
  border-radius: 9px;
  text-decoration: none;
  transition: transform .18s, box-shadow .18s;
}

.arch__cta:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px -8px #7c5cf0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity .2s, transform .2s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(6px);
}

@media (max-width: 640px) {
  .band {
    padding: 14px;
  }

  .chip {
    font-size: 12px;
    padding: 5px 10px 5px 9px;
  }
}
</style>
