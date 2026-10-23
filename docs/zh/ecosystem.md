---
title: 生态全景
description: Microsphere Projects 与外部技术栈的对接关系
outline: [2, 3]
---

# 生态全景

Microsphere 不是一个封闭框架，它的绝大多数项目都是**围绕既有技术栈做增强**。这一页列出它与外部生态的对接点。

## 对接的技术栈

| 领域 | 外部技术 | 对接项目 |
|------|----------|----------|
| **核心框架** | Spring Framework 4.3 – 7.0 | [microsphere-spring](/zh/projects/microsphere-spring) |
| | Spring Boot 2.0 – 4.1 | [microsphere-spring-boot](/zh/projects/microsphere-spring-boot) |
| | Spring Cloud Hoxton – 2025.x | [microsphere-spring-cloud](/zh/projects/microsphere-spring-cloud) |
| **服务注册与发现** | Alibaba Nacos | [microsphere-nacos](/zh/projects/microsphere-nacos) |
| | Netflix Eureka | [microsphere-netflix](/zh/projects/microsphere-netflix) |
| | Consul / Zookeeper | [microsphere-spring-cloud](/zh/projects/microsphere-spring-cloud) |
| | etcd | [microsphere-etcd](/zh/projects/microsphere-etcd) |
| **RPC 与网关** | Apache Dubbo | [microsphere-dubbo](/zh/projects/microsphere-dubbo) |
| | Spring Cloud Gateway（WebFlux / MVC） | [microsphere-gateway](/zh/projects/microsphere-gateway) |
| | OpenFeign | [microsphere-spring-cloud](/zh/projects/microsphere-spring-cloud) |
| **数据访问** | MyBatis | [microsphere-mybatis](/zh/projects/microsphere-mybatis) |
| | Hibernate ORM 5.0 – 7.3 | [microsphere-hibernate](/zh/projects/microsphere-hibernate) |
| | Alibaba Druid | [microsphere-alibaba-druid](/zh/projects/microsphere-alibaba-druid) |
| | P6Spy | [microsphere-spring](/zh/projects/microsphere-spring) |
| **缓存** | Spring Data Redis 2.1 – 3.5 | [microsphere-redis](/zh/projects/microsphere-redis) |
| | Apache Kafka（Redis 复制） | [microsphere-redis](/zh/projects/microsphere-redis) |
| **韧性与流控** | Alibaba Sentinel | [microsphere-alibaba-sentinel](/zh/projects/microsphere-alibaba-sentinel) |
| | Resilience4j 1.3 – 2.4 | [microsphere-resilience4j](/zh/projects/microsphere-resilience4j) |
| **可观测性** | Micrometer | [microsphere-observability](/zh/projects/microsphere-observability) |
| | Prometheus | [microsphere-observability](/zh/projects/microsphere-observability) |
| | OpenTelemetry Instrumentation BOM | [microsphere-observability](/zh/projects/microsphere-observability) |
| **日志** | JUL / Log4j / Log4j2 / Logback / SLF4J | [microsphere-logging](/zh/projects/microsphere-logging) |
| **Web 容器** | Apache Tomcat | [microsphere-tomcat](/zh/projects/microsphere-tomcat) |
| **企业规范** | Java EE / Jakarta EE / MicroProfile | [EE](/zh/projects/microsphere-java-enterprise) · [Jakarta](/zh/projects/microsphere-jakarta) · [MicroProfile](/zh/projects/microsphere-microprofile) |
| **依赖注入** | Google Guice | [microsphere-spring](/zh/projects/microsphere-spring) |
| **云平台** | AWS（可用区发现） | [microsphere-multiactive](/zh/projects/microsphere-multiactive) |

## 与其它增强库的差异

Microsphere 的定位是**增量增强而非替代**。三个显著特征：

1. **零侵入** — 大部分能力通过拦截管道、自动配置与事件机制织入，不需要修改既有代码。
   例如 `@EnableP6DataSource` 只需一个注解，即可包裹全部 DataSource Bean。
2. **可裁剪** — 每个 Maven 模块都可独立引入，不会强制带入整套依赖。
3. **长周期兼容** — 通过兼容 shim 让同一套代码横跨 Spring Boot 2.x 至 4.x，避免为升级而分叉维护。

## 发布与制品

- 全部制品发布至 **Maven Central**，Group ID 为 `io.github.microsphere-projects`
- 自 `microsphere-build` 0.2.0 起使用 Central Publisher Portal（OSSRH 已于 2025-06-30 下线）
- 每个仓库都配置了 Maven Build 与 Codecov 工作流

## 文档资源

每个子项目都提供双语文档（English 默认，中文位于 `zh/` 目录），并按发布分支组织：

| 资源 | 位置 |
|------|------|
| 仓库内用户文档 | `docs/user-guide/` · `docs/developer-guide/` |
| 智能问答文档 | 各仓库对应的 DeepWiki 与 Zread 空间 |
| JavaDoc | javadoc.io（按模块独立发布） |
| Wiki | 各仓库 GitHub Wiki |
