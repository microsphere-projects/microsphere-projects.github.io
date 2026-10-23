import { computed } from 'vue'
import { useData } from 'vitepress'

/**
 * Locale helpers shared by every custom component.
 * English is the primary locale (root), Chinese lives under /zh/.
 */
export function useLocale() {
  const { lang } = useData()
  const isZh = computed(() => String(lang.value || 'en').toLowerCase().startsWith('zh'))

  /** Pick a string by locale: L('English', '中文') */
  const L = (en, zh) => (isZh.value ? zh : en)

  /** Pick a {en, zh} data object's field by locale */
  const tx = (obj) => (obj ? (isZh.value ? obj.zh : obj.en) : '')

  /** Locale path prefix, e.g. '' or '/zh' */
  const base = computed(() => (isZh.value ? '/zh' : ''))

  /** Build an in-site link honouring the locale prefix */
  const link = (path) => `${base.value}${path}`

  return { isZh, L, tx, base, link }
}

/** Shared UI strings that appear in more than one component. */
export const UI = {
  projects: { en: 'Projects', zh: '子项目' },
  prev: { en: 'Previous', zh: '上一个' },
  next: { en: 'Next', zh: '下一个' },
  viewProject: { en: 'View full profile', zh: '查看完整介绍' },
  clear: { en: 'Clear selection', zh: '清除选中' },
  hint: {
    en: 'Hover or click any module to see where it sits in the ecosystem',
    zh: '悬停或点击任一模块，查看它在生态中的位置',
  },
  stars: { en: 'Stars', zh: 'Stars' },
  forks: { en: 'Forks', zh: 'Forks' },
  latest: { en: 'latest', zh: '最新' },
  repo: { en: 'GitHub Repository', zh: 'GitHub 仓库' },
  deepwiki: { en: 'DeepWiki Docs', zh: 'DeepWiki 文档' },
  issues: { en: 'Report an Issue', zh: '反馈问题' },
}
