---
layout: page
title: Microsphere Projects — Java / Spring 生态分层增强体系
description: Microsphere Projects 官方站点，32 个子项目、五层架构、统一 BOM 与版本矩阵。
outline: false
---

<HomeHero></HomeHero>

---

## 一分钟了解 Microsphere

Microsphere Projects 是一个由 **36 个 GitHub 仓库**组成的开源组织，围绕 Java 与 Spring 生态提供分层增强。
它不是一个单一框架，而是一套**可以按需组合的能力矩阵**：你可以只用最底部的 `microsphere-java` 作为工具库，
也可以引入 Spring Cloud 增强实现免重启的 Feign 配置刷新，再往上叠加可观测性、国际化与多活路由。

所有项目共享同一套工程约定：

- **统一 Group ID** — `io.github.microsphere-projects`
- **统一 BOM 治理** — 每个子项目都提供 `*-dependencies` 模块，导入一次即可对齐全部版本
- **统一构建口径** — `microsphere-build` 父 POM 覆盖 Java 8 / 11 / 17 / 21 / 25
- **双版本线** — `main` 面向新一代（Spring Boot 3/4、Spring Cloud 2022–2025），`1.x` 面向存量（Spring Boot 2、Hoxton–2021）

## 哪些场景适合用它

| 场景 | 对应能力 | 入口项目 |
|------|----------|----------|
| 启动慢，Bean 初始化串行 | 解析依赖图，并发生成互不依赖的单例 | [Spring](/projects/microsphere-spring) |
| 改一次配置就要重启发布 | 配置变更驱动 Feign / 属性源 / i18n 消息热更新 | [Spring Cloud](/projects/microsphere-spring-cloud) |
| 线上想看 SQL 慢在哪 | 非侵入拦截 SQL 并接入 Micrometer | [Observability](/projects/microsphere-observability) |
| 接口需要流控与熔断 | 统一模型覆盖 Web / DB / Redis | [Sentinel](/projects/microsphere-alibaba-sentinel) |
| 多语言消息要集中管理 | 分层消息源 + 集中式 i18n Server | [i18n](/projects/microsphere-i18n) |
| 同一实例要注册到多个注册中心 | 统一 API 多注册中心 + 联合 DiscoveryClient | [Spring Cloud](/projects/microsphere-spring-cloud) |
| 多活单元化，优先同区调用 | Zone 感知路由与跨区兜底 | [Multiactive](/projects/microsphere-multiactive) |
| 网关路由不想在每个服务里重复写 | `we://` 协议基于服务发现动态路由 | [Gateway](/projects/microsphere-gateway) |

## 接下来

- [架构大图](/architecture) — 五层架构与全部子项目的交互关系，可交互查看
- [子项目总览](/projects/) — 支持搜索、按分层/热度/名称排序的完整清单
- [快速开始](/guide/getting-started) — 从引入 BOM 到跑通第一个特性
