# Microsphere Projects — Official Site

The official website for [Microsphere Projects](https://github.com/microsphere-projects), built with **VitePress**.

All content is stored as **standalone Markdown files** — one page per sub-project — and compiles to a fully static
site ready for GitHub Pages.

**Bilingual, English-first**: English lives at the site root (`/`), Chinese under `/zh/`. Every page has a
counterpart in both locales.

## Quick start

```bash
npm install
npm run dev        # dev server at http://localhost:5173
npm run build      # build to docs/.vitepress/dist
npm run preview    # preview the build
```

> The `docs` argument in the npm scripts is required — without it VitePress infers the wrong root directory.

## Structure

```
docs/                              ← English (primary locale)
├── index.md                       Home: hero, layer rail, design principles, flagship projects
├── architecture.md                Architecture: interactive layers, capability map, request path
├── ecosystem.md                   Integration points with the external stack
├── community.md                   Contributing and maintainers
├── guide/
│   ├── getting-started.md
│   ├── dependencies.md
│   └── compatibility.md
├── projects/
│   ├── index.md                   Catalogue: search, layer filters, sorting
│   └── microsphere-*.md           32 standalone project pages
├── zh/                            ← Chinese (secondary locale, mirrors the tree above)
│   ├── index.md
│   ├── architecture.md
│   ├── ecosystem.md
│   ├── community.md
│   ├── guide/…
│   └── projects/…
├── public/                        logo.svg, favicon.svg
└── .vitepress/
    ├── config.mts                 Locales, nav, sidebars, search, UI strings
    ├── sidebar.mjs                AUTO-GENERATED — English sidebar
    ├── sidebar.zh.mjs             AUTO-GENERATED — Chinese sidebar
    └── theme/
        ├── index.ts               Theme entry, component registration
        ├── custom.css             Design system
        ├── composables/
        │   └── useLocale.js       Locale helpers: L(), tx(), base, link()
        ├── data/projects.json     AUTO-GENERATED — bilingual project data
        └── components/
            ├── HomeHero.vue           Home page hero (bilingual)
            ├── ArchitectureMap.vue    Interactive five-layer map
            ├── ProjectsIndex.vue      Catalogue with search / filter / sort
            ├── ProjectHeader.vue      Project page header
            └── ProjectNav.vue         Prev / next project navigation
tools/
├── projects_a.py                  L0–L2 bilingual data (12 projects)
├── projects_b.py                  L3–L4 bilingual data (20 projects)
├── data.py                        Aggregates the two, asserts locale parity
├── gen.py                         Generates all pages, sidebars and projects.json
└── fetch.py / fetch2.py           Pull READMEs from the GitHub API
```

## How the i18n works

There is **no runtime translation layer** — both locales are pre-rendered at build time.

1. **Data** — every user-facing string in `tools/projects_*.py` is an `{"en": …, "zh": …}` pair.
2. **Generation** — `tools/gen.py` writes the same page twice, once into `docs/projects/` and once into
   `docs/zh/projects/`, using the label set for that locale.
3. **Components** — read the active locale through `useLocale()`, which derives it from VitePress's
   `useData().lang`. `L('English', '中文')` picks a string; `base` is `''` or `'/zh'` and drives every internal link.
4. **Config** — `config.mts` declares two locales with their own nav, sidebar and UI strings. VitePress renders the
   language switcher automatically and maps paths across locales.

## Maintaining content

All project copy lives in `tools/projects_a.py` and `tools/projects_b.py`. After editing, regenerate:

```bash
python tools/gen.py
```

This rewrites:

- `docs/projects/*.md` and `docs/zh/projects/*.md` — 32 pages per locale
- `docs/.vitepress/sidebar.mjs` and `sidebar.zh.mjs`
- `docs/.vitepress/theme/data/projects.json` — consumed by the home page, architecture map and catalogue

To refresh upstream facts (stars, forks, README changes), run `python tools/fetch.py` and
`python tools/fetch2.py`, then reconcile `tools/projects_*.py` by hand.

> `gen.py` escapes bare angle brackets outside inline code so fragments like `<version>` are not parsed as HTML
> by Vue.

## Layers

The site's information architecture is built on five dependency layers:

| Layer | Description | Projects |
|-------|-------------|----------|
| L0 Foundation | Maven parent POM and BOM governance | 2 |
| L1 Runtime | Framework-free Java capabilities | 7 |
| L2 Framework | Spring / Boot / Cloud enhancements | 3 |
| L3 Integration | Registries, data access, caching, RPC, resilience | 12 |
| L4 Cross-cutting | Observability, i18n, security, dynamic config, multi-active | 8 |

## Deployment

Build output goes to `docs/.vitepress/dist`. Push it to the `microsphere-projects.github.io` repository to serve
via GitHub Pages, or use the included workflow at `.github/workflows/deploy.yml`.

If deploying under a sub-path, set `base` in `docs/.vitepress/config.mts`.

## License

Site content is released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
