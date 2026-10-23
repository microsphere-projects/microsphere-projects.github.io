import { defineConfig } from 'vitepress'
import { projectsSidebar as projectsEn } from './sidebar.mjs'
import { projectsSidebar as projectsZh } from './sidebar.zh.mjs'

const ORG = 'https://github.com/microsphere-projects'

const guideEn = [
  {
    text: 'Guide',
    items: [
      { text: 'Getting Started', link: '/guide/getting-started' },
      { text: 'Dependencies & BOMs', link: '/guide/dependencies' },
      { text: 'Compatibility Matrix', link: '/guide/compatibility' },
    ],
  },
]

const guideZh = [
  {
    text: '入门指南',
    items: [
      { text: '快速开始', link: '/zh/guide/getting-started' },
      { text: '依赖与 BOM', link: '/zh/guide/dependencies' },
      { text: '版本兼容矩阵', link: '/zh/guide/compatibility' },
    ],
  },
]

const navEn = [
  { text: 'Home', link: '/' },
  { text: 'Architecture', link: '/architecture' },
  { text: 'Projects', link: '/projects/', activeMatch: '/projects/' },
  { text: 'Guide', link: '/guide/getting-started', activeMatch: '/guide/' },
  { text: 'Ecosystem', link: '/ecosystem' },
  { text: 'Community', link: '/community' },
]

const navZh = [
  { text: '首页', link: '/zh/' },
  { text: '架构大图', link: '/zh/architecture' },
  { text: '子项目', link: '/zh/projects/', activeMatch: '/zh/projects/' },
  { text: '指南', link: '/zh/guide/getting-started', activeMatch: '/zh/guide/' },
  { text: '生态', link: '/zh/ecosystem' },
  { text: '社区', link: '/zh/community' },
]

export default defineConfig({
  title: 'Microsphere Projects',
  description:
    'A layered enhancement system for the Java and Spring ecosystem — runtime foundation, framework extensions, ecosystem integrations and cross-cutting capabilities.',
  lang: 'en-US',
  cleanUrls: true,
  lastUpdated: true,

  head: [
    ['meta', { name: 'theme-color', content: '#7c5cf0' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Microsphere Projects' }],
    ['meta', {
      property: 'og:description',
      content: 'A layered enhancement system for the Java and Spring ecosystem. 36 repositories, 32 documented sub-projects.',
    }],
    ['link', { rel: 'icon', href: '/favicon.svg', type: 'image/svg+xml' }],
  ],

  locales: {
    root: {
      label: 'English',
      lang: 'en-US',
      title: 'Microsphere Projects',
      description:
        'A layered enhancement system for the Java and Spring ecosystem — runtime foundation, framework extensions, ecosystem integrations and cross-cutting capabilities.',
      themeConfig: {
        nav: navEn,
        sidebar: {
          '/projects/': projectsEn,
          '/guide/': guideEn,
          '/': [
            { text: 'Overview', items: [{ text: 'Home', link: '/' }, { text: 'Architecture', link: '/architecture' }, { text: 'Ecosystem', link: '/ecosystem' }] },
          ],
        },
        outlineTitle: 'On this page',
        docFooter: { prev: 'Previous', next: 'Next' },
        lastUpdatedText: 'Last updated',
        returnToTopLabel: 'Back to top',
        sidebarMenuLabel: 'Menu',
        darkModeSwitchLabel: 'Appearance',
        lightModeSwitchTitle: 'Switch to light theme',
        darkModeSwitchTitle: 'Switch to dark theme',
        skipToContentLabel: 'Skip to content',
        editLink: {
          pattern: `${ORG}/microsphere-projects.github.io/edit/main/docs/:path`,
          text: 'Edit this page on GitHub',
        },
        footer: {
          message: 'Released under the Apache License 2.0',
          copyright: 'Copyright © 2021–2026 Microsphere Projects',
        },
        search: {
          provider: 'local',
          options: {
            translations: {
              button: { buttonText: 'Search', buttonAriaLabel: 'Search' },
              modal: {
                displayDetails: 'Display detailed list',
                resetButtonTitle: 'Reset search',
                backButtonTitle: 'Close search',
                noResultsText: 'No results for',
                footer: {
                  selectText: 'to select',
                  selectKeyAriaLabel: 'enter',
                  navigateText: 'to navigate',
                  navigateUpKeyAriaLabel: 'up arrow',
                  navigateDownKeyAriaLabel: 'down arrow',
                  closeText: 'to close',
                  closeKeyAriaLabel: 'escape',
                },
              },
            },
          },
        },
      },
    },

    zh: {
      label: '简体中文',
      lang: 'zh-CN',
      link: '/zh/',
      title: 'Microsphere Projects',
      description:
        '面向 Java / Spring 生态的分层增强体系：运行时基座、框架扩展、生态集成与横向能力。',
      themeConfig: {
        nav: navZh,
        sidebar: {
          '/zh/projects/': projectsZh,
          '/zh/guide/': guideZh,
          '/zh/': [
            { text: '概览', items: [{ text: '首页', link: '/zh/' }, { text: '架构大图', link: '/zh/architecture' }, { text: '生态全景', link: '/zh/ecosystem' }] },
          ],
        },
        outlineTitle: '本页目录',
        docFooter: { prev: '上一页', next: '下一页' },
        lastUpdatedText: '最后更新于',
        returnToTopLabel: '回到顶部',
        sidebarMenuLabel: '菜单',
        darkModeSwitchLabel: '主题',
        lightModeSwitchTitle: '切换到浅色模式',
        darkModeSwitchTitle: '切换到深色模式',
        skipToContentLabel: '跳到内容',
        editLink: {
          pattern: `${ORG}/microsphere-projects.github.io/edit/main/docs/:path`,
          text: '在 GitHub 上编辑此页',
        },
        footer: {
          message: '基于 Apache License 2.0 发布',
          copyright: 'Copyright © 2021–2026 Microsphere Projects',
        },
        search: {
          provider: 'local',
          options: {
            translations: {
              button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
              modal: {
                displayDetails: '显示详细列表',
                resetButtonTitle: '重置搜索',
                backButtonTitle: '关闭搜索',
                noResultsText: '没有找到结果：',
                footer: {
                  selectText: '选择',
                  selectKeyAriaLabel: '回车',
                  navigateText: '切换',
                  navigateUpKeyAriaLabel: '上箭头',
                  navigateDownKeyAriaLabel: '下箭头',
                  closeText: '关闭',
                  closeKeyAriaLabel: 'esc',
                },
              },
            },
          },
        },
      },
    },
  },

  themeConfig: {
    logo: '/logo.svg',
    outline: [2, 3],
    socialLinks: [{ icon: 'github', link: ORG }],
  },

  markdown: {
    lineNumbers: false,
    math: false,
  },
})
