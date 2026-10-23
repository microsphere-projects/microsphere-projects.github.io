import { defineConfig } from 'vitepress'
import { projectsSidebar } from './sidebar.mjs'

const ORG = 'https://github.com/microsphere-projects'

export default defineConfig({
  title: 'Microsphere Projects',
  description:
    'Microsphere Projects —— 面向 Java / Spring 生态的分层增强体系：运行时基座、框架扩展、生态集成与横向能力。',
  lang: 'zh-CN',
  cleanUrls: true,
  lastUpdated: true,
  head: [
    ['meta', { name: 'theme-color', content: '#7c5cf0' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Microsphere Projects' }],
    ['meta', {
      property: 'og:description',
      content: '面向 Java / Spring 生态的分层增强体系，36 个仓库、32 个子项目的统一官方站点。',
    }],
    ['link', { rel: 'icon', href: '/favicon.svg', type: 'image/svg+xml' }],
  ],

  themeConfig: {
    logo: '/logo.svg',
    outline: [2, 3],
    search: { provider: 'local' },

    nav: [
      { text: '首页', link: '/' },
      { text: '架构大图', link: '/architecture' },
      { text: '子项目', link: '/projects/', activeMatch: '/projects/' },
      { text: '指南', link: '/guide/getting-started', activeMatch: '/guide/' },
      { text: '生态', link: '/ecosystem' },
      {
        text: '社区',
        items: [
          { text: '贡献指南', link: '/community' },
          {
            text: 'GitHub 组织',
            link: ORG,
          },
          { text: '问题反馈', link: `${ORG}/microsphere-java/issues` },
        ],
      },
    ],

    sidebar: {
      '/projects/': projectsSidebar,
      '/guide/': [
        {
          text: '入门指南',
          items: [
            { text: '快速开始', link: '/guide/getting-started' },
            { text: '依赖与 BOM', link: '/guide/dependencies' },
            { text: '版本兼容矩阵', link: '/guide/compatibility' },
          ],
        },
      ],
      '/': [
        { text: '概览', link: '/' },
        { text: '架构大图', link: '/architecture' },
        { text: '生态全景', link: '/ecosystem' },
      ],
    },

    socialLinks: [{ icon: 'github', link: ORG }],

    footer: {
      message: '基于 Apache License 2.0 发布',
      copyright: 'Copyright © 2021–2026 Microsphere Projects',
    },

    editLink: {
      pattern: `${ORG}/microsphere-projects.github.io/edit/main/docs/:path`,
      text: '在 GitHub 上编辑此页',
    },

    docFooter: { prev: '上一页', next: '下一页' },
    outlineTitle: '本页目录',
    lastUpdatedText: '最后更新于',
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
    skipToContentLabel: '跳到内容',
  },

  markdown: {
    lineNumbers: false,
    math: false,
  },
})
