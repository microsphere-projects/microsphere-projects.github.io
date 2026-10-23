// Bilingual content for the home page "in one minute" block.

export const intro = {
  en: 'Microsphere Projects is an open-source organisation of 36 GitHub repositories that provides layered enhancements for the Java and Spring ecosystem. It is not a single framework but a composable capability matrix — use the utility library alone, add Spring Cloud extensions for restart-free Feign refresh, or stack observability, internationalisation and multi-active routing on top.',
  zh: 'Microsphere Projects 是一个由 36 个 GitHub 仓库组成的开源组织，围绕 Java 与 Spring 生态提供分层增强。它不是一个单一框架，而是一套可以按需组合的能力矩阵：你可以只用最底部的 microsphere-java 作为工具库，也可以引入 Spring Cloud 增强实现免重启的 Feign 配置刷新，再往上叠加可观测性、国际化与多活路由。',
}

export const principles = [
  {
    icon: 'M4 9h16M4 15h16M10 3L8 21M16 3l-2 18',
    code: 'io.github.microsphere-projects',
    en: {
      title: 'One Group ID',
      desc: 'Every artifact resolves under a single namespace on Maven Central.',
    },
    zh: {
      title: '统一 Group ID',
      desc: '所有制品都发布在同一个 Maven Central 命名空间下。',
    },
  },
  {
    icon: 'M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5',
    code: '*-dependencies',
    en: {
      title: 'One BOM convention',
      desc: 'Each sub-project ships its own BOM — import once to align every module version.',
    },
    zh: {
      title: '统一 BOM 治理',
      desc: '每个子项目都提供独立 BOM，导入一次即可对齐全部模块版本。',
    },
  },
  {
    icon: 'M4 17l6-6-6-6M12 19h8',
    code: 'Java 8 / 11 / 17 / 21 / 25',
    en: {
      title: 'One build baseline',
      desc: 'The microsphere-build parent POM keeps all 36 repositories on the same plugins and profiles.',
    },
    zh: {
      title: '统一构建口径',
      desc: 'microsphere-build 父 POM 让 36 个仓库共享同一套插件与 profile。',
    },
  },
  {
    icon: 'M6 3v12M18 9a3 3 0 100-6 3 3 0 000 6zM6 21a3 3 0 100-6 3 3 0 000 6zM18 9a9 9 0 01-9 9',
    code: 'main · 1.x',
    en: {
      title: 'Two release lines',
      desc: 'main targets the current generation; 1.x keeps existing systems running without a fork.',
    },
    zh: {
      title: '双版本线',
      desc: 'main 面向新一代框架，1.x 让存量系统无需分叉即可继续演进。',
    },
  },
]

export const scenarios = [
  {
    layer: 'foundation',
    project: 'microsphere-bom',
    name: 'BOM',
    en: {
      problem: 'Module versions drift apart',
      capability: 'Import one bill of materials and every artifact aligns.',
    },
    zh: {
      problem: '模块版本各写各的，逐渐对不上',
      capability: '导入一份 BOM，全部制品版本自动对齐。',
    },
  },
  {
    layer: 'runtime',
    project: 'microsphere-java',
    name: 'Java',
    en: {
      problem: 'Utility code rewritten in every project',
      capability: 'Null-safe strings, collections, reflection and type conversion out of the box.',
    },
    zh: {
      problem: '工具类在每个项目里重复造一遍',
      capability: '开箱即用的字符串 / 集合 / 反射 / 类型转换工具。',
    },
  },
  {
    layer: 'framework',
    project: 'microsphere-spring',
    name: 'Spring',
    en: {
      problem: 'Slow startup from serial bean creation',
      capability: 'Resolve the dependency graph and build independent singletons concurrently.',
    },
    zh: {
      problem: '启动慢，Bean 初始化串行',
      capability: '解析依赖图，并发生成互不依赖的单例。',
    },
  },
  {
    layer: 'framework',
    project: 'microsphere-spring-cloud',
    name: 'Spring Cloud',
    en: {
      problem: 'Redeploying for every configuration change',
      capability: 'Hot-refresh Feign, property sources and i18n messages on change.',
    },
    zh: {
      problem: '改一次配置就要重启发布',
      capability: '配置变更驱动 Feign / 属性源 / i18n 消息热更新。',
    },
  },
  {
    layer: 'integration',
    project: 'microsphere-alibaba-sentinel',
    name: 'Sentinel',
    en: {
      problem: 'No rate limiting or circuit breaking',
      capability: 'One model across web, database and Redis.',
    },
    zh: {
      problem: '接口需要流控与熔断',
      capability: '统一模型覆盖 Web / DB / Redis。',
    },
  },
  {
    layer: 'integration',
    project: 'microsphere-gateway',
    name: 'Gateway',
    en: {
      problem: 'Gateway routes duplicated per service',
      capability: 'The we:// scheme routes discovered endpoints dynamically.',
    },
    zh: {
      problem: '网关路由不想在每个服务里重复写',
      capability: 'we:// 协议基于服务发现动态路由。',
    },
  },
  {
    layer: 'crosscutting',
    project: 'microsphere-observability',
    name: 'Observability',
    en: {
      problem: 'Not knowing where slow SQL goes',
      capability: 'Intercept SQL non-intrusively and feed Micrometer.',
    },
    zh: {
      problem: '线上想看 SQL 慢在哪',
      capability: '非侵入拦截 SQL 并接入 Micrometer。',
    },
  },
  {
    layer: 'crosscutting',
    project: 'microsphere-i18n',
    name: 'i18n',
    en: {
      problem: 'Messages scattered across locales',
      capability: 'Layered message sources plus a centralised i18n server.',
    },
    zh: {
      problem: '多语言消息要集中管理',
      capability: '分层消息源 + 集中式 i18n Server。',
    },
  },
  {
    layer: 'crosscutting',
    project: 'microsphere-multiactive',
    name: 'Multiactive',
    en: {
      problem: 'Active-active with no zone awareness',
      capability: 'Zone-aware routing with cross-zone fallback.',
    },
    zh: {
      problem: '多活单元化，优先同区调用',
      capability: 'Zone 感知路由与跨区兜底。',
    },
  },
]

export const nextSteps = [
  {
    href: '/architecture',
    en: {
      title: 'Architecture',
      desc: 'The five layers and how every sub-project fits together — fully interactive.',
    },
    zh: {
      title: '架构大图',
      desc: '五层架构与全部子项目的交互关系，可交互查看。',
    },
  },
  {
    href: '/projects/',
    en: {
      title: 'All projects',
      desc: 'The complete catalogue with search, layer filters and sorting.',
    },
    zh: {
      title: '子项目总览',
      desc: '支持搜索、按分层 / 热度 / 名称排序的完整清单。',
    },
  },
  {
    href: '/guide/getting-started',
    en: {
      title: 'Getting started',
      desc: 'From importing a BOM to your first feature.',
    },
    zh: {
      title: '快速开始',
      desc: '从引入 BOM 到跑通第一个特性。',
    },
  },
]
