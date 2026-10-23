<script setup>
import { ref, computed, onMounted } from 'vue'
import data from '../data/projects.json'
import { useLocale } from '../composables/useLocale'

const { L, isZh, base } = useLocale()

const q = ref('')
const layer = ref('all')
const sort = ref('layer')

const layers = data.layers

onMounted(() => {
  const params = new URLSearchParams(window.location.search)
  const l = params.get('layer')
  if (l && layers.some((x) => x.id === l)) layer.value = l
  const s = params.get('sort')
  if (s === 'stars' || s === 'name' || s === 'layer') sort.value = s
})

const filtered = computed(() => {
  const kw = q.value.trim().toLowerCase()
  let list = data.projects.filter((p) => {
    if (layer.value !== 'all' && p.layer !== layer.value) return false
    if (!kw) return true
    const d = isZh.value ? p.zh : p.en
    const hay = [p.name, p.slug, d.tagline, d.summary, p.artifactId || '', p.bom || '',
      ...d.features.map((f) => f[0] + f[1])].join(' ').toLowerCase()
    return hay.includes(kw)
  })
  if (sort.value === 'stars') list = [...list].sort((a, b) => b.stars - a.stars)
  else if (sort.value === 'name') list = [...list].sort((a, b) => a.name.localeCompare(b.name))
  return list
})

const grouped = computed(() => {
  if (sort.value !== 'layer') return [{ id: '_flat', title: '', desc: '', items: filtered.value }]
  return layers
    .map((l) => ({
      id: l.id, title: l[isZh.value ? 'zh' : 'en'], desc: l[isZh.value ? 'zh_desc' : 'en_desc'],
      items: filtered.value.filter((p) => p.layer === l.id),
    }))
    .filter((g) => g.items.length)
})

const total = computed(() => filtered.value.length)
const detail = (p) => `${base.value}/projects/${p.slug}`
const feats = (p) => (isZh.value ? p.zh.features : p.en.features)
</script>

<template>
  <div class="px">
    <div class="px__bar">
      <div class="px__search">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="7" />
          <path d="M20 20l-3.5-3.5" stroke-linecap="round" />
        </svg>
        <input v-model="q" type="search"
          :placeholder="L('Search by name, capability or module — e.g. feign, redis, TTL', '按名称、能力或模块搜索，例如：feign、redis、TTL')" />
      </div>
      <div class="px__sort">
        <button :class="{ on: sort === 'layer' }" @click="sort = 'layer'">{{ L('By layer', '按分层') }}</button>
        <button :class="{ on: sort === 'stars' }" @click="sort = 'stars'">{{ L('Popular', '按热度') }}</button>
        <button :class="{ on: sort === 'name' }" @click="sort = 'name'">{{ L('By name', '按名称') }}</button>
      </div>
    </div>

    <div class="px__filters">
      <button class="px__chip" :class="{ on: layer === 'all' }" @click="layer = 'all'">{{ L('All', '全部') }}</button>
      <button v-for="l in layers" :key="l.id" class="px__chip" :class="[`px__chip--${l.id}`, { on: layer === l.id }]"
        @click="layer = l.id">{{ l[isZh ? 'zh' : 'en'] }}</button>
      <span class="px__count">{{ L(`${total} projects`, `${total} 个项目`) }}</span>
    </div>

    <div v-if="!total" class="px__empty">
      {{ L('No matching projects. Try another keyword.', '没有匹配的项目，试试其它关键词。') }}
    </div>

    <section v-for="g in grouped" :key="g.id" class="px__group">
      <div v-if="g.title" class="px__grouphead">
        <h2>{{ g.title }}</h2>
        <p>{{ g.desc }}</p>
      </div>
      <div class="px__grid">
        <a v-for="p in g.items" :key="p.slug" class="card" :href="detail(p)">
          <div class="card__head">
            <span class="card__badge" :class="`card__badge--${p.layer}`">{{ p.name.replace('Microsphere ', '') }}</span>
            <span v-if="p.stars" class="card__stars">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2l2.9 6.3 6.9.8-5.1 4.7 1.4 6.8L12 17.3 5.9 20.6l1.4-6.8L2.2 9.1l6.9-.8L12 2z" />
              </svg>
              {{ p.stars }}
            </span>
          </div>
          <p class="card__tagline">{{ L(p.en.tagline, p.zh.tagline) }}</p>
          <ul class="card__feats">
            <li v-for="f in feats(p).slice(0, 3)" :key="f[0]" :title="f[0]">{{ f[0] }}</li>
          </ul>
          <div class="card__foot">
            <span class="card__lang">{{ p.lang }}</span>
            <span v-if="feats(p).length > 3" class="card__more">
              {{ L(`+${feats(p).length - 3} more`, `+${feats(p).length - 3} 项特性`) }}
            </span>
            <span class="card__go">
              {{ L('Details', '详情') }}
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6">
                <path d="M5 12h13M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
            </span>
          </div>
        </a>
      </div>
    </section>
  </div>
</template>

<style scoped>
.px {
  margin: 26px 0 8px;
}

.px__bar {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
}

.px__search {
  position: relative;
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1 1 280px;
  min-width: 240px;
  padding: 9px 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 11px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-3);
  transition: border-color .2s, box-shadow .2s;
}

.px__search:focus-within {
  border-color: var(--ms-accent);
  box-shadow: 0 0 0 3px rgba(124, 92, 240, .14);
}

.px__search input {
  flex: 1;
  border: 0;
  outline: 0;
  background: transparent;
  font-size: 14px;
  color: var(--vp-c-text-1);
  font-family: inherit;
}

.px__search input::placeholder {
  color: var(--vp-c-text-3);
}

.px__sort {
  display: flex;
  gap: 4px;
  padding: 3px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 11px;
  background: var(--vp-c-bg-soft);
}

.px__sort button {
  border: 0;
  background: transparent;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  color: var(--vp-c-text-2);
  padding: 6px 12px;
  border-radius: 8px;
  cursor: pointer;
  transition: all .18s;
  white-space: nowrap;
}

.px__sort button.on {
  background: var(--vp-c-bg);
  color: var(--ms-accent);
  box-shadow: 0 1px 4px rgba(0, 0, 0, .07);
}

.px__filters {
  display: flex;
  align-items: center;
  gap: 7px;
  flex-wrap: wrap;
  margin: 14px 0 22px;
}

.px__chip {
  --c: var(--vp-c-text-2);
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  font: inherit;
  font-size: 12.5px;
  font-weight: 600;
  padding: 5px 12px;
  border-radius: 999px;
  cursor: pointer;
  transition: all .18s;
  white-space: nowrap;
}

.px__chip:hover {
  color: var(--c);
  border-color: var(--c);
}

.px__chip.on {
  color: #fff;
  border-color: transparent;
}

.px__chip--foundation.on {
  --c: #64748b;
  background: #64748b;
}

.px__chip--runtime.on {
  --c: #0ea5e9;
  background: #0ea5e9;
}

.px__chip--framework.on {
  --c: #7c5cf0;
  background: #7c5cf0;
}

.px__chip--integration.on {
  --c: #10b981;
  background: #10b981;
}

.px__chip--crosscutting.on {
  --c: #f59e0b;
  background: #f59e0b;
}

.px__chip:not(.on).px__chip--foundation {
  --c: #64748b;
}

.px__chip:not(.on).px__chip--runtime {
  --c: #0ea5e9;
}

.px__chip:not(.on).px__chip--framework {
  --c: #7c5cf0;
}

.px__chip:not(.on).px__chip--integration {
  --c: #10b981;
}

.px__chip:not(.on).px__chip--crosscutting {
  --c: #f59e0b;
}

.px__chip:first-child.on {
  background: var(--ms-accent);
}

.px__count {
  margin-left: auto;
  font-size: 12.5px;
  color: var(--vp-c-text-3);
}

.px__empty {
  padding: 40px;
  text-align: center;
  color: var(--vp-c-text-3);
  font-size: 14px;
  border: 1px dashed var(--vp-c-divider);
  border-radius: 14px;
}

.px__group {
  margin-bottom: 34px;
}

.px__grouphead {
  margin-bottom: 14px;
}

.px__grouphead h2 {
  margin: 0 0 4px;
  font-size: 17px;
  font-weight: 720;
  letter-spacing: -.01em;
  border: 0;
  padding: 0;
}

.px__grouphead p {
  margin: 0;
  font-size: 13.5px;
  color: var(--vp-c-text-2);
  line-height: 1.65;
}

.px__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(248px, 1fr));
  gap: 12px;
}

.card {
  display: flex;
  flex-direction: column;
  padding: 15px 16px 13px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 14px;
  background: var(--vp-c-bg-soft);
  text-decoration: none;
  transition: transform .2s cubic-bezier(.2, .8, .3, 1), box-shadow .2s, border-color .2s;
}

.card:hover {
  transform: translateY(-3px);
  border-color: var(--ms-accent);
  box-shadow: 0 14px 30px -18px var(--ms-accent);
}

.card__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 8px;
}

.card__badge {
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: -.005em;
}

.card__badge--foundation {
  color: #64748b;
}

.card__badge--runtime {
  color: #0ea5e9;
}

.card__badge--framework {
  color: #7c5cf0;
}

.card__badge--integration {
  color: #10b981;
}

.card__badge--crosscutting {
  color: #f59e0b;
}

.card__stars {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--vp-c-text-3);
}

.card__tagline {
  margin: 0 0 10px;
  font-size: 13px;
  line-height: 20px;
  color: var(--vp-c-text-2);
  /* 固定占 2 行：单行卡片也能与双行卡片对齐，超过 2 行则省略 */
  min-height: 40px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card__feats {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin: 0 0 12px;
  padding: 0;
  list-style: none;
}

.card__feats li {
  display: block;
  margin: 0; /* 覆盖 .vp-doc li + li 的 margin-top: 8px，否则同一行 chip 会错位 */
  min-width: 0;
  max-width: 100%;
  height: 24px;
  line-height: 22px;
  font-size: 11.5px;
  font-weight: 550;
  color: var(--vp-c-text-2);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  padding: 0 7px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card__foot {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: auto;
  padding-top: 10px;
  border-top: 1px solid var(--vp-c-divider);
  font-size: 11.5px;
  color: var(--vp-c-text-3);
}

.card__go {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  margin-left: auto;
  font-weight: 650;
  color: var(--ms-accent);
}

.card__more {
  margin-left: 4px;
}
</style>
