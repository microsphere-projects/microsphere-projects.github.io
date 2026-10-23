<script setup>
import { computed } from 'vue'
import data from '../data/projects.json'

const projects = data.projects
const layers = data.layers

const stats = computed(() => {
  const stars = projects.reduce((n, p) => n + p.stars, 0)
  const forks = projects.reduce((n, p) => n + p.forks, 0)
  const feats = projects.reduce((n, p) => n + p.features.length, 0)
  const mods = projects.reduce((n, p) => n + p.modules.length, 0)
  return [
    { k: '36', label: 'GitHub 仓库', sub: '32 个已建档子项目' },
    { k: String(stars), label: 'Stars', sub: `Forks ${forks}` },
    { k: String(feats), label: '项特性', sub: `${mods} 个 Maven 模块` },
    { k: '5', label: '架构分层', sub: '基座 → 框架 → 生态' },
  ]
})

const top = computed(() => [...projects].sort((a, b) => b.stars - a.stars).slice(0, 6))

const pillars = [
  {
    icon: 'M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5',
    title: '自下而上的分层地基',
    desc: 'microsphere-java 提供字符串、反射、类型转换、事件分发等零框架依赖的基础能力，全生态共享同一套语义。',
  },
  {
    icon: 'M13 2L3 14h9l-1 8 10-12h-9l1-8z',
    title: '免重启的运行时动态性',
    desc: '配置变更驱动 Feign 组件热刷新、属性源自动重载、i18n 消息在线更新——变更生效不依赖应用重启。',
  },
  {
    icon: 'M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z M12 9a3 3 0 100 6 3 3 0 000-6z',
    title: '非侵入的可观测性',
    desc: 'SQL、Redis、Feign 调用链通过拦截管道接入 Micrometer 与 Prometheus，无需改动一行业务代码。',
  },
  {
    icon: 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z',
    title: '面向生产的韧性',
    desc: 'Sentinel 与 Resilience4j 以统一编程模型覆盖 Web、数据库与缓存，流控与熔断渐进式接入。',
  },
  {
    icon: 'M4 4h16v16H4z M9 9h6v6H9z',
    title: '严谨的工程治理',
    desc: '统一父 POM 覆盖 Java 8–25 五个 TLS 版本，六套 Maven profile 管理构建、签名、覆盖率与发布。',
  },
  {
    icon: 'M21 12a9 9 0 11-18 0 9 9 0 0118 0z M12 7v5l3 2',
    title: '长周期版本兼容',
    desc: 'main 与 1.x 双线并行，同一套代码横跨 Spring Boot 2.x–4.x、Spring Cloud Hoxton–2025.x。',
  },
]
</script>

<template>
  <div class="hero">
    <div class="ms-grid-bg" />
    <div class="hero__glow" />
    <div class="hero__inner">
      <div class="hero__badge">
        <span class="hero__dot" />
        Apache-2.0 · Java 生态基础设施
      </div>

      <h1 class="hero__title">
        <span class="hero__title-a">Microsphere</span>
        <span class="hero__title-b">Projects</span>
      </h1>

      <p class="hero__lead">
        一套围绕 <strong>Java / Spring 生态</strong> 构建的分层增强体系。从零框架的运行时基座出发，
        逐层扩展到 Spring、Spring Boot、Spring Cloud 增强，再向外连接注册中心、数据访问、缓存、RPC 与容错组件，
        并由可观测性、国际化、多活等横向能力贯穿始终。
      </p>

      <div class="hero__cta">
        <a class="btn btn--primary" href="/architecture.html">
          查看架构大图
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">
            <path d="M5 12h13M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </a>
        <a class="btn" href="/projects/">浏览全部子项目</a>
        <a class="btn btn--ghost" href="https://github.com/microsphere-projects" target="_blank" rel="noreferrer">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M12 .5A11.5 11.5 0 00.5 12c0 5.1 3.3 9.4 7.9 10.9.6.1.8-.3.8-.6v-2c-3.2.7-3.9-1.5-3.9-1.5-.5-1.3-1.3-1.7-1.3-1.7-1-.7.1-.7.1-.7 1.1.1 1.7 1.2 1.7 1.2 1 1.7 2.6 1.2 3.2.9.1-.7.4-1.2.7-1.5-2.6-.3-5.3-1.3-5.3-5.7 0-1.3.4-2.3 1.1-3.1-.1-.3-.5-1.5.1-3 0 0 1.1-.4 3.6 1.4a12.3 12.3 0 016.4 0c2.5-1.8 3.6-1.4 3.6-1.4.6 1.5.2 2.7.1 3 .7.8 1.1 1.8 1.1 3.1 0 4.4-2.7 5.4-5.3 5.7.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A11.5 11.5 0 0023.5 12A11.5 11.5 0 0012 .5z" />
          </svg>
          GitHub 组织
        </a>
      </div>

      <div class="stats">
        <div v-for="s in stats" :key="s.label" class="stats__item">
          <div class="stats__k">{{ s.k }}</div>
          <div class="stats__label">{{ s.label }}</div>
          <div class="stats__sub">{{ s.sub }}</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ---------- layer rail ---------- -->
  <div class="rail">
    <div class="rail__head">
      <h2>五层架构</h2>
      <p>自下而上构建，每一层只依赖它下面的层。点击任一层查看其中的子项目。</p>
    </div>
    <div class="rail__stack">
      <a v-for="l in layers" :key="l.id" class="lane" :class="`lane--${l.id}`" :href="`/projects/?layer=${l.id}`">
        <div class="lane__side">
          <span class="lane__code">{{ l.en }}</span>
          <span class="lane__title">{{ l.title }}</span>
        </div>
        <p class="lane__desc">{{ l.desc }}</p>
        <div class="lane__count">{{ projects.filter((p) => p.layer === l.id).length }}</div>
      </a>
    </div>
  </div>

  <!-- ---------- pillars ---------- -->
  <div class="sec">
    <div class="sec__head">
      <h2>设计取向</h2>
      <p>六条贯穿全部 32 个子项目的工程原则。</p>
    </div>
    <div class="pillars">
      <div v-for="p in pillars" :key="p.title" class="pillar">
        <div class="pillar__icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
            stroke-linecap="round" stroke-linejoin="round">
            <path :d="p.icon" />
          </svg>
        </div>
        <h3>{{ p.title }}</h3>
        <p>{{ p.desc }}</p>
      </div>
    </div>
  </div>

  <!-- ---------- featured ---------- -->
  <div class="sec">
    <div class="sec__head">
      <h2>核心项目</h2>
      <p>按社区关注度排序的六个入口项目。</p>
    </div>
    <div class="feat">
      <a v-for="p in top" :key="p.slug" class="feat__item" :href="`/projects/${p.slug}`">
        <div class="feat__top">
          <span class="feat__name">{{ p.name.replace('Microsphere ', '') }}</span>
          <span class="feat__stars">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2l2.9 6.3 6.9.8-5.1 4.7 1.4 6.8L12 17.3 5.9 20.6l1.4-6.8L2.2 9.1l6.9-.8L12 2z" />
            </svg>
            {{ p.stars }}
          </span>
        </div>
        <p class="feat__tag">{{ p.tagline }}</p>
        <div class="feat__mods">{{ p.modules.length }} 个模块 · {{ p.features.length }} 项特性</div>
      </a>
    </div>
  </div>
</template>

<style scoped>
/* ---------------- hero ---------------- */
.hero {
  position: relative;
  margin-inline: calc(50% - 50vw);
  padding: 74px 24px 56px;
  overflow: hidden;
  border-bottom: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
}

.hero__glow {
  position: absolute;
  top: -220px;
  left: 50%;
  width: 900px;
  height: 620px;
  transform: translateX(-50%);
  pointer-events: none;
  background: radial-gradient(ellipse at center, rgba(124, 92, 240, .22), transparent 62%);
  filter: blur(28px);
}

.dark .hero__glow {
  background: radial-gradient(ellipse at center, rgba(139, 109, 245, .28), transparent 62%);
}

.hero__inner {
  position: relative;
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
}

.hero__badge {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: .01em;
  color: var(--vp-c-text-2);
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  border-radius: 999px;
  padding: 5px 14px;
  margin-bottom: 22px;
}

.hero__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, .2);
}

.hero__title {
  margin: 0 0 18px;
  font-size: clamp(38px, 7.4vw, 68px);
  line-height: 1.03;
  font-weight: 800;
  letter-spacing: -0.035em;
}

.hero__title-a {
  background: linear-gradient(100deg, #7c5cf0 0%, #0ea5e9 55%, #10b981 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero__title-b {
  color: var(--vp-c-text-1);
  margin-left: .3em;
}

.hero__lead {
  max-width: 720px;
  margin: 0 auto 30px;
  font-size: 16.5px;
  line-height: 1.8;
  color: var(--vp-c-text-2);
}

.hero__lead strong {
  color: var(--vp-c-text-1);
  font-weight: 650;
}

.hero__cta {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 46px;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 14px;
  font-weight: 640;
  padding: 11px 20px;
  border-radius: 11px;
  text-decoration: none;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  transition: transform .18s cubic-bezier(.2, .8, .3, 1), box-shadow .18s, border-color .18s;
}

.btn:hover {
  transform: translateY(-2px);
}

.btn--primary {
  background: var(--ms-gradient);
  color: #fff;
  border-color: transparent;
  box-shadow: 0 10px 26px -12px #7c5cf0;
}

.btn--primary:hover {
  box-shadow: 0 14px 32px -12px #7c5cf0;
}

.btn--ghost:hover {
  border-color: var(--ms-accent);
}

.stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: var(--vp-c-divider);
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  overflow: hidden;
}

.stats__item {
  background: var(--vp-c-bg);
  padding: 18px 12px;
}

.stats__k {
  font-size: 26px;
  font-weight: 780;
  letter-spacing: -.03em;
  line-height: 1.1;
  background: var(--ms-gradient);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.stats__label {
  font-size: 13px;
  font-weight: 620;
  color: var(--vp-c-text-1);
  margin-top: 2px;
}

.stats__sub {
  font-size: 11.5px;
  color: var(--vp-c-text-3);
  margin-top: 2px;
}

/* ---------------- layer rail ---------------- */
.rail {
  margin: 64px 0 0;
}

.rail__head,
.sec__head {
  margin-bottom: 20px;
}

.rail__head h2,
.sec__head h2 {
  margin: 0 0 5px;
  font-size: 24px;
  font-weight: 760;
  letter-spacing: -.02em;
}

.rail__head p,
.sec__head p {
  margin: 0;
  font-size: 14.5px;
  color: var(--vp-c-text-2);
}

.rail__stack {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.lane {
  --c: var(--vp-c-text-2);
  position: relative;
  display: grid;
  grid-template-columns: 168px 1fr auto;
  align-items: center;
  gap: 16px;
  padding: 14px 18px;
  border: 1px solid var(--vp-c-divider);
  border-left: 3px solid var(--c);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
  text-decoration: none;
  transition: transform .18s cubic-bezier(.2, .8, .3, 1), box-shadow .18s;
}

.lane:hover {
  transform: translateX(4px);
  box-shadow: 0 10px 26px -18px var(--c);
}

.lane--foundation {
  --c: #64748b;
}

.lane--runtime {
  --c: #0ea5e9;
}

.lane--framework {
  --c: #7c5cf0;
}

.lane--integration {
  --c: #10b981;
}

.lane--crosscutting {
  --c: #f59e0b;
}

.lane__side {
  display: flex;
  align-items: baseline;
  gap: 8px;
  min-width: 0;
}

.lane__code {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--c);
}

.lane__title {
  font-size: 13.5px;
  font-weight: 680;
  color: var(--vp-c-text-1);
}

.lane__desc {
  margin: 0;
  font-size: 13px;
  line-height: 1.65;
  color: var(--vp-c-text-2);
}

.lane__count {
  width: 34px;
  height: 34px;
  flex: none;
  display: grid;
  place-items: center;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 720;
  color: var(--c);
  background: color-mix(in srgb, var(--c) 12%, transparent);
}

/* ---------------- sections ---------------- */
.sec {
  margin-top: 64px;
}

.pillars {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(258px, 1fr));
  gap: 12px;
}

.pillar {
  padding: 18px 18px 20px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 14px;
  background: var(--vp-c-bg-soft);
  transition: transform .2s cubic-bezier(.2, .8, .3, 1), border-color .2s, box-shadow .2s;
}

.pillar:hover {
  transform: translateY(-3px);
  border-color: var(--ms-accent);
  box-shadow: 0 16px 34px -22px var(--ms-accent);
}

.pillar__icon {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 11px;
  margin-bottom: 12px;
  color: #fff;
  background: var(--ms-gradient);
}

.pillar h3 {
  margin: 0 0 6px;
  font-size: 14.5px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.pillar p {
  margin: 0;
  font-size: 13.2px;
  line-height: 1.72;
  color: var(--vp-c-text-2);
}

.feat {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(218px, 1fr));
  gap: 10px;
}

.feat__item {
  display: flex;
  flex-direction: column;
  padding: 14px 16px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 13px;
  background: var(--vp-c-bg-soft);
  text-decoration: none;
  transition: transform .2s cubic-bezier(.2, .8, .3, 1), border-color .2s, box-shadow .2s;
}

.feat__item:hover {
  transform: translateY(-3px);
  border-color: var(--ms-accent);
  box-shadow: 0 14px 30px -20px var(--ms-accent);
}

.feat__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 6px;
}

.feat__name {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: var(--vp-c-text-1);
}

.feat__stars {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 11.5px;
  font-weight: 620;
  color: var(--vp-c-text-3);
}

.feat__tag {
  margin: 0 0 10px;
  font-size: 12.8px;
  line-height: 1.6;
  color: var(--vp-c-text-2);
}

.feat__mods {
  margin-top: auto;
  font-size: 11.5px;
  color: var(--vp-c-text-3);
  padding-top: 9px;
  border-top: 1px solid var(--vp-c-divider);
}

@media (max-width: 820px) {
  .stats {
    grid-template-columns: repeat(2, 1fr);
  }

  .lane {
    grid-template-columns: 1fr auto;
  }

  .lane__side {
    grid-column: 1 / -1;
  }
}

@media (max-width: 560px) {
  .hero {
    padding: 54px 20px 44px;
  }

  .hero__lead {
    font-size: 15px;
  }
}
</style>
