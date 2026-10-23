<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import data from '../data/projects.json'

const { frontmatter } = useData()
const p = computed(() => frontmatter.value.project || null)
const layer = computed(() => {
  if (!p.value) return null
  return data.layers.find((l) => l.id === p.value.layer) || null
})
const repo = computed(() => `https://github.com/microsphere-projects/${p.value?.slug}`)
</script>

<template>
  <div v-if="p" class="ph">
    <div class="ph__top">
      <div class="ph__crumb">
        <a href="/projects/">子项目</a>
        <span class="ph__sep">/</span>
        <span v-if="layer" class="ph__layer" :class="`ph__layer--${p.layer}`">{{ layer.title }}</span>
      </div>

      <div class="ph__stats">
        <span class="ph__stat" title="Stars">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2l2.9 6.3 6.9.8-5.1 4.7 1.4 6.8L12 17.3 5.9 20.6l1.4-6.8L2.2 9.1l6.9-.8L12 2z" />
          </svg>
          {{ p.stars }}
        </span>
        <span class="ph__stat" title="Forks">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="6" cy="5" r="2.4" /><circle cx="6" cy="19" r="2.4" /><circle cx="18" cy="12" r="2.4" />
            <path d="M6 7.4v9.2M8.4 5h2.8a2 2 0 012 2v3.2a2 2 0 002 2h1.4" stroke-linecap="round" />
          </svg>
          {{ p.forks }}
        </span>
        <span class="ph__stat ph__stat--lang">{{ p.lang }}</span>
      </div>
    </div>

    <h1 class="ph__title">{{ p.name }}</h1>
    <p class="ph__tagline">{{ p.tagline }}</p>

    <div class="ph__meta">
      <a v-if="p.artifactId" class="ph__coord" :href="`https://central.sonatype.com/artifact/io.github.microsphere-projects/${p.artifactId}`"
        target="_blank" rel="noreferrer">
        <span class="ph__coord-key">io.github.microsphere-projects</span>
        <span class="ph__coord-sep">:</span>
        <span class="ph__coord-art">{{ p.artifactId }}</span>
        <svg class="ph__ext" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor"
          stroke-width="2.2">
          <path d="M7 17L17 7M9 7h8v8" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </a>
      <span v-if="p.version" class="ph__ver">最新 {{ p.version }}</span>
    </div>

    <div class="ph__actions">
      <a class="ph__btn ph__btn--primary" :href="repo" target="_blank" rel="noreferrer">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">
          <path
            d="M12 .5A11.5 11.5 0 00.5 12c0 5.1 3.3 9.4 7.9 10.9.6.1.8-.3.8-.6v-2c-3.2.7-3.9-1.5-3.9-1.5-.5-1.3-1.3-1.7-1.3-1.7-1-.7.1-.7.1-.7 1.1.1 1.7 1.2 1.7 1.2 1 1.7 2.6 1.2 3.2.9.1-.7.4-1.2.7-1.5-2.6-.3-5.3-1.3-5.3-5.7 0-1.3.4-2.3 1.1-3.1-.1-.3-.5-1.5.1-3 0 0 1.1-.4 3.6 1.4a12.3 12.3 0 016.4 0c2.5-1.8 3.6-1.4 3.6-1.4.6 1.5.2 2.7.1 3 .7.8 1.1 1.8 1.1 3.1 0 4.4-2.7 5.4-5.3 5.7.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A11.5 11.5 0 0023.5 12A11.5 11.5 0 0012 .5z" />
        </svg>
        GitHub 仓库
      </a>
      <a class="ph__btn" :href="`https://deepwiki.com/microsphere-projects/${p.slug}`" target="_blank"
        rel="noreferrer">DeepWiki 文档</a>
      <a class="ph__btn" :href="`${repo}/issues`" target="_blank" rel="noreferrer">反馈问题</a>
    </div>
  </div>
</template>

<style scoped>
.ph {
  padding-bottom: 26px;
  margin-bottom: 8px;
  border-bottom: 1px solid var(--vp-c-divider);
}

.ph__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 14px;
}

.ph__crumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: var(--vp-c-text-2);
}

.ph__crumb a {
  color: var(--vp-c-text-2);
  text-decoration: none;
}

.ph__crumb a:hover {
  color: var(--ms-accent);
}

.ph__sep {
  opacity: .45;
}

.ph__layer {
  font-size: 11px;
  font-weight: 650;
  padding: 2px 9px;
  border-radius: 999px;
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-2);
}

.ph__layer--foundation {
  color: #64748b;
  border-color: rgba(100, 116, 139, .5);
}

.ph__layer--runtime {
  color: #0ea5e9;
  border-color: rgba(14, 165, 233, .5);
}

.ph__layer--framework {
  color: #7c5cf0;
  border-color: rgba(124, 92, 240, .5);
}

.ph__layer--integration {
  color: #10b981;
  border-color: rgba(16, 185, 129, .5);
}

.ph__layer--crosscutting {
  color: #f59e0b;
  border-color: rgba(245, 158, 11, .5);
}

.ph__stats {
  display: flex;
  align-items: center;
  gap: 6px;
}

.ph__stat {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-weight: 600;
  color: var(--vp-c-text-2);
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  padding: 3px 10px;
}

.ph__stat--lang {
  color: var(--vp-c-text-3);
}

.ph__title {
  margin: 0 0 6px;
  font-size: clamp(26px, 4vw, 36px);
  line-height: 1.15;
  font-weight: 780;
  letter-spacing: -.02em;
  background: linear-gradient(100deg, var(--vp-c-text-1) 20%, var(--ms-accent));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.ph__tagline {
  margin: 0 0 16px;
  font-size: 16px;
  color: var(--vp-c-text-2);
}

.ph__meta {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 18px;
}

.ph__coord {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-family: var(--vp-font-family-mono);
  font-size: 12.5px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 5px 10px;
  text-decoration: none;
  transition: border-color .2s;
}

.ph__coord:hover {
  border-color: var(--ms-accent);
}

.ph__coord-key {
  color: var(--vp-c-text-3);
}

.ph__coord-sep {
  color: var(--vp-c-text-3);
  opacity: .6;
}

.ph__coord-art {
  color: var(--ms-accent);
  font-weight: 600;
}

.ph__ext {
  margin-left: 3px;
  color: var(--vp-c-text-3);
}

.ph__ver {
  font-size: 12px;
  font-weight: 600;
  color: #10b981;
  background: rgba(16, 185, 129, .10);
  border-radius: 999px;
  padding: 4px 10px;
}

.ph__actions {
  display: flex;
  gap: 9px;
  flex-wrap: wrap;
}

.ph__btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 600;
  padding: 8px 14px;
  border-radius: 9px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  text-decoration: none;
  transition: transform .18s, border-color .18s, box-shadow .18s;
}

.ph__btn:hover {
  transform: translateY(-1px);
  border-color: var(--ms-accent);
}

.ph__btn--primary {
  background: linear-gradient(120deg, #7c5cf0, #0ea5e9);
  color: #fff;
  border-color: transparent;
}

.ph__btn--primary:hover {
  box-shadow: 0 8px 20px -8px #7c5cf0;
}
</style>
