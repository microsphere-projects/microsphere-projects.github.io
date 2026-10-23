<script setup>
import { computed } from 'vue'
import { useLocale } from '../composables/useLocale'
import { intro, principles, scenarios, nextSteps } from '../data/home'

const { L, isZh, base } = useLocale()

const t = (obj) => (isZh.value ? obj.zh : obj.en)

const steps = computed(() =>
  nextSteps.map((s) => ({
    href: `${base.value}${s.href}`,
    ...t(s),
  }))
)

const cases = computed(() =>
  scenarios.map((s) => ({
    href: `${base.value}/projects/${s.project}`,
    layer: s.layer,
    name: s.name,
    ...t(s),
  }))
)
</script>

<template>
  <div class="hi">
    <!-- ── section 1: what it is ─────────────────────────── -->
    <section class="hi__sec hi__sec--first">
      <header class="hi__head">
        <span class="hi__eyebrow">{{ L('Overview', '概览') }}</span>
        <h2 class="hi__title">{{ L('Microsphere in one minute', '一分钟了解 Microsphere') }}</h2>
      </header>

      <p class="hi__lead">{{ L(intro.en, intro.zh) }}</p>

      <div class="spec">
        <div v-for="p in principles" :key="p.code" class="spec__row">
          <span class="spec__icon">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9"
              stroke-linecap="round" stroke-linejoin="round">
              <path :d="p.icon" />
            </svg>
          </span>
          <div class="spec__main">
            <h3 class="spec__title">{{ t(p).title }}</h3>
            <p class="spec__desc">{{ t(p).desc }}</p>
          </div>
          <code class="spec__code">{{ p.code }}</code>
        </div>
      </div>
    </section>

    <!-- ── section 2: where it fits ──────────────────────── -->
    <section class="hi__sec">
      <header class="hi__head">
        <span class="hi__eyebrow">{{ L('Use cases', '适用场景') }}</span>
        <h2 class="hi__title">{{ L('Where it fits', '哪些场景适合用它') }}</h2>
        <p class="hi__sub">
          {{ L('Nine common production problems, and the sub-project that solves each one.',
            '九个常见的生产问题，以及各自对应的子项目。') }}
        </p>
      </header>

      <div class="cases">
        <a v-for="c in cases" :key="c.problem" class="case" :class="`case--${c.layer}`" :href="c.href">
          <div class="case__top">
            <span class="case__dot" />
            <span class="case__name">{{ c.name }}</span>
          </div>
          <p class="case__problem">{{ c.problem }}</p>
          <p class="case__cap">{{ c.capability }}</p>
          <span class="case__go">
            {{ L('Explore', '查看项目') }}
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6">
              <path d="M5 12h13M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </span>
        </a>
      </div>
    </section>

    <!-- ── section 3: next steps ─────────────────────────── -->
    <section class="hi__sec">
      <header class="hi__head">
        <span class="hi__eyebrow">{{ L('Next', '接下来') }}</span>
        <h2 class="hi__title">{{ L('Keep going', '继续深入') }}</h2>
      </header>

      <div class="steps">
        <a v-for="s in steps" :key="s.href" class="step" :href="s.href">
          <div class="step__body">
            <h3 class="step__title">{{ s.title }}</h3>
            <p class="step__desc">{{ s.desc }}</p>
          </div>
          <span class="step__arrow">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">
              <path d="M5 12h13M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </span>
        </a>
      </div>
    </section>
  </div>
</template>

<style scoped>
.hi {
  max-width: 1142px;
  margin: 0 auto;
}

.hi__sec {
  margin-top: 68px;
}

.hi__sec--first {
  margin-top: 52px;
}

/* ---------- section header ---------- */
.hi__head {
  margin-bottom: 20px;
}

.hi__eyebrow {
  display: inline-block;
  font-size: 10.5px;
  font-weight: 750;
  letter-spacing: .16em;
  text-transform: uppercase;
  background: var(--ms-gradient);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 8px;
}

.hi__title {
  margin: 0;
  font-size: clamp(21px, 2.6vw, 26px);
  font-weight: 770;
  letter-spacing: -.022em;
  line-height: 1.2;
  color: var(--vp-c-text-1);
  border: 0;
  padding: 0;
}

.hi__sub {
  margin: 7px 0 0;
  font-size: 14px;
  color: var(--vp-c-text-2);
  line-height: 1.6;
}

.hi__lead {
  margin: 0 0 24px;
  max-width: 820px;
  font-size: 16px;
  line-height: 1.82;
  color: var(--vp-c-text-2);
}

/* ---------- engineering contracts spec sheet ---------- */
.spec {
  max-width: 920px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  background: var(--vp-c-bg-soft);
  overflow: hidden;
}

.spec__row {
  position: relative;
  display: grid;
  grid-template-columns: 30px minmax(0, 1fr) auto;
  align-items: center;
  gap: 14px;
  padding: 15px 18px;
  transition: background .18s;
}

.spec__row + .spec__row {
  border-top: 1px solid var(--vp-c-divider);
}

.spec__row::before {
  content: '';
  position: absolute;
  inset: 0 auto 0 0;
  width: 2px;
  background: var(--ms-gradient);
  opacity: 0;
  transition: opacity .18s;
}

.spec__row:hover {
  background: color-mix(in srgb, var(--ms-accent) 4%, transparent);
}

.spec__row:hover::before {
  opacity: 1;
}

.spec__icon {
  width: 30px;
  height: 30px;
  display: grid;
  place-items: center;
  border-radius: 9px;
  color: #fff;
  background: var(--ms-gradient);
  box-shadow: 0 6px 14px -8px var(--ms-accent);
}

.spec__main {
  min-width: 0;
}

.spec__title {
  margin: 0 0 2px;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: -.008em;
  color: var(--vp-c-text-1);
}

.spec__desc {
  margin: 0;
  font-size: 12.8px;
  line-height: 1.6;
  color: var(--vp-c-text-2);
}

.spec__code {
  font-family: var(--vp-font-family-mono);
  font-size: 11.5px;
  font-weight: 550;
  color: var(--ms-accent);
  background: var(--vp-c-brand-soft);
  border-radius: 6px;
  padding: 3px 9px;
  white-space: nowrap;
  justify-self: end;
}

/* ---------- use cases ---------- */
.cases {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 11px;
}

.case {
  --c: var(--ms-accent);
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 15px 16px 13px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 13px;
  background: var(--vp-c-bg-soft);
  text-decoration: none;
  transition: transform .2s cubic-bezier(.2, .8, .3, 1), border-color .2s, box-shadow .2s;
}

.case--foundation {
  --c: #64748b;
}

.case--runtime {
  --c: #0ea5e9;
}

.case--framework {
  --c: #7c5cf0;
}

.case--integration {
  --c: #10b981;
}

.case--crosscutting {
  --c: #f59e0b;
}

.case:hover {
  transform: translateY(-3px);
  border-color: color-mix(in srgb, var(--c) 55%, var(--vp-c-divider));
  box-shadow: 0 16px 32px -24px var(--c);
}

.case__top {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 9px;
}

.case__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--c);
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--c) 16%, transparent);
  flex: none;
}

.case__name {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .02em;
  color: var(--c);
}

.case__problem {
  margin: 0 0 5px;
  font-size: 14px;
  font-weight: 680;
  line-height: 1.45;
  letter-spacing: -.008em;
  color: var(--vp-c-text-1);
}

.case__cap {
  margin: 0 0 12px;
  font-size: 12.8px;
  line-height: 1.62;
  color: var(--vp-c-text-2);
}

.case__go {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  margin-top: auto;
  padding-top: 10px;
  border-top: 1px solid var(--vp-c-divider);
  font-size: 11.5px;
  font-weight: 650;
  color: var(--c);
  opacity: .75;
  transition: opacity .2s, gap .2s;
}

.case:hover .case__go {
  opacity: 1;
  gap: 7px;
}

/* ---------- next steps ---------- */
.steps {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 11px;
}

.step {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 18px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 14px;
  background: linear-gradient(135deg, color-mix(in srgb, var(--ms-accent) 6%, transparent), transparent 70%);
  text-decoration: none;
  transition: transform .2s cubic-bezier(.2, .8, .3, 1), border-color .2s, box-shadow .2s;
}

.step:hover {
  transform: translateY(-2px);
  border-color: var(--ms-accent);
  box-shadow: 0 14px 30px -22px var(--ms-accent);
}

.step__body {
  min-width: 0;
}

.step__title {
  margin: 0 0 3px;
  font-size: 14.5px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: var(--vp-c-text-1);
}

.step__desc {
  margin: 0;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--vp-c-text-2);
}

.step__arrow {
  flex: none;
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  color: var(--ms-accent);
  background: var(--vp-c-brand-soft);
  transition: transform .2s, background .2s, color .2s;
}

.step:hover .step__arrow {
  transform: translateX(3px);
  background: var(--ms-gradient);
  color: #fff;
}

@media (max-width: 980px) {
  .cases {
    grid-template-columns: repeat(2, 1fr);
  }

  .steps {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 760px) {
  .spec__row {
    grid-template-columns: 30px minmax(0, 1fr);
    row-gap: 8px;
    align-items: start;
  }

  .spec__code {
    grid-column: 2;
    justify-self: start;
  }
}

@media (max-width: 640px) {
  .hi__sec {
    margin-top: 52px;
  }

  .hi__lead {
    font-size: 15px;
  }

  .cases {
    grid-template-columns: 1fr;
  }
}
</style>
