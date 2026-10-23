---
title: 社区与贡献
description: 参与 Microsphere Projects 的方式、维护者与行为准则
outline: [2, 3]
---

# 社区与贡献

## 获取帮助

| 渠道 | 用途 |
|------|------|
| [GitHub Issues](https://github.com/microsphere-projects/microsphere-java/issues) | Bug 报告与特性请求（请先搜索既有 issue） |
| [GitHub Discussions](https://github.com/microsphere-projects/microsphere-java/discussions) | 使用问题与方案讨论 |
| [DeepWiki](https://deepwiki.com/microsphere-projects/microsphere-java) | 直接基于源码提问的 AI 文档 |
| 邮件 | mercyblitz@gmail.com |

提交 Bug 时请附上：**Java 版本、Spring / Spring Boot 版本、Microsphere 版本、最小复现示例与完整堆栈**。

## 贡献流程

1. Fork 目标仓库，从 `main` 分支创建特性分支
2. 实现改动并补充测试
3. 本地验证：`./mvnw test`（Windows 使用 `mvnw.cmd test`）
4. 提交 Pull Request，**CI（Maven + JUnit）必须通过**
5. 参与前请先阅读仓库内的 `CODE_OF_CONDUCT.md`

```bash
git clone https://github.com/microsphere-projects/microsphere-java.git
cd microsphere-java
./mvnw package
```

## 维护者

| 姓名 | 角色 | 联系方式 |
|------|------|----------|
| [Mercy Ma (mercyblitz)](https://github.com/mercyblitz) | 首席架构师与开发者 | mercyblitz@gmail.com |

## 组织信息

| 项目 | 值 |
|------|-----|
| 组织 | [microsphere-projects](https://github.com/microsphere-projects) |
| 创建时间 | 2021-12-25 |
| 所在地 | China |
| 公开仓库 | 36 |
| 许可证 | Apache License 2.0 |

## 相关仓库

部分仓库不属于能力层，而是支撑生态运转：

| 仓库 | 用途 |
|------|------|
| `microsphere-projects.github.io` | 官方站点（GitHub Pages） |
| `.github` | 组织级模板与工作流配置 |
| `microsphere-devops` / `microsphere-devops-ui` | 工程效能与运维界面（TypeScript） |
| `microsphere-apidocs` | API 文档生成 |

## 许可证

Microsphere Projects 全部代码基于 [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) 发布。
