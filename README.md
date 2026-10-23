# Microsphere Projects 官方站点

基于 **VitePress** 构建的 [Microsphere Projects](https://github.com/microsphere-projects) 官方网站。
全部内容以 **Markdown 独立存储**，每个子项目一个独立页面，构建产物为纯静态站点，可直接发布到 GitHub Pages。

## 快速开始

```bash
npm install
npm run dev        # 本地开发 http://localhost:5173
npm run build      # 构建到 docs/.vitepress/dist
npm run preview    # 预览构建产物
```

## 目录结构

```
docs/
├── index.md                      首页（自定义 hero + 五层架构导航 + 设计取向 + 核心项目）
├── architecture.md               架构大图（五层交互图 + 能力域横切汇总 + 调用链路图）
├── ecosystem.md                  生态全景（对接的外部技术栈）
├── community.md                  社区与贡献
├── guide/
│   ├── getting-started.md        快速开始
│   ├── dependencies.md           依赖与 BOM
│   └── compatibility.md          版本兼容矩阵
├── projects/
│   ├── index.md                  子项目总览（支持搜索 / 分层 / 热度 / 名称排序）
│   ├── microsphere-java.md       ← 每个子项目一个独立 Markdown 单页
│   ├── microsphere-spring.md
│   ├── microsphere-spring-boot.md
│   ├── microsphere-spring-cloud.md
│   └── ...（共 32 个）
├── public/                       logo.svg、favicon.svg
└── .vitepress/
    ├── config.mts                站点配置与导航
    ├── sidebar.mjs               AUTO-GENERATED 侧边栏
    └── theme/
        ├── index.ts              主题注册
        ├── custom.css            设计系统（品牌色、排版、表格、代码块）
        ├── data/projects.json    AUTO-GENERATED 子项目数据
        └── components/
            ├── HomeHero.vue          首页 hero
            ├── ArchitectureMap.vue   可交互五层架构图
            ├── ProjectsIndex.vue     项目总览（搜索 / 筛选 / 排序）
            ├── ProjectHeader.vue     子项目页头部
            └── ProjectNav.vue        子项目间上下页导航
tools/
├── data.py                      32 个子项目的权威数据源（各字段取自对应仓库 README）
├── gen.py                       生成 docs/projects/*.md、sidebar.mjs、projects.json
└── fetch.py / fetch2.py         从 GitHub API 抓取各仓库 README
```

## 内容维护

子项目页面的正文内容集中在 `tools/data.py`，修改后重新生成：

```bash
python tools/gen.py
```

该脚本会重新生成：

- `docs/projects/*.md` — 32 个子项目单页
- `docs/.vitepress/sidebar.mjs` — 侧边栏
- `docs/.vitepress/theme/data/projects.json` — 供首页、架构图、总览页消费的数据

若需要刷新上游数据（star / fork / README 变更），先运行 `python tools/fetch.py`、`python tools/fetch2.py` 抓取，
再人工核对 `tools/data.py`。

> 注意：`gen.py` 会对写入 Markdown 正文的文本做尖括号转义，避免 `<version>` 这类片段被 Vue 当作 HTML 解析。

## 架构分层

站点把 32 个子项目归入五层，这也是官方站信息架构的主线：

| 层 | 说明 | 项目数 |
|----|------|--------|
| L0 工程基座 | Maven 父 POM 与 BOM 治理 | 2 |
| L1 运行时基座 | 零框架依赖的 Java 能力 | 7 |
| L2 框架扩展 | Spring / Boot / Cloud 增强 | 3 |
| L3 生态集成 | 注册中心、数据访问、缓存、RPC、容错 | 12 |
| L4 横向能力 | 可观测、国际化、安全、动态配置、多活 | 8 |

## 部署

构建产物位于 `docs/.vitepress/dist`。推送到 `microsphere-projects.github.io` 仓库即可通过 GitHub Pages 访问。

若部署到子路径（如 `https://xxx.github.io/microsphere/`），需在 `docs/.vitepress/config.mts` 中设置 `base`。

## 许可证

站点内容基于 [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) 发布。
