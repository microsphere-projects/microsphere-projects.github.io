---
title: Microsphere Alibaba Sentinel
description: "在 Alibaba Sentinel 流控框架与常用 Java 技术之间建立无缝集成的抽象层，将 Sentinel 的流控、熔断与系统保护能力透明地施加到数据库操作、缓存与其它基础设施组件上。"
outline: deep
project:
  slug: microsphere-alibaba-sentinel
  name: Microsphere Alibaba Sentinel
  layer: integration
  tagline: 把流控能力透明注入数据库、缓存与 Web
  lang: Java
  stars: 2
  forks: 11
  artifactId: microsphere-alibaba-sentinel-commons
  bom: microsphere-alibaba-sentinel-dependencies
  version: 0.2.5
---

<ProjectHeader />

## 它解决什么问题

在 Alibaba Sentinel 流控框架与常用 Java 技术之间建立无缝集成的抽象层，将 Sentinel 的流控、熔断与系统保护能力透明地施加到数据库操作、缓存与其它基础设施组件上。

## 核心特性

- **Web 层流控** — 覆盖 Spring WebMVC 与 Spring WebFlux。
- **数据访问层流控** — 覆盖 Alibaba Druid、Hibernate、MyBatis、P6Spy。
- **缓存层流控** — 覆盖 Spring Data Redis。
- **渐进式接入** — 同时提供底层集成 API 与 Spring Boot 高层自动配置，可按需逐步采用。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-alibaba-sentinel-commons` | Sentinel 扩展通用特性 |
| `microsphere-alibaba-sentinel-plugins` | Sentinel 插件集合 |
| `microsphere-alibaba-sentinel-spring` | Alibaba Sentinel Spring 集成 |
| `microsphere-alibaba-sentinel-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-alibaba-sentinel-dependencies</artifactId>
            <version>${microsphere-alibaba-sentinel.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

然后按需引入模块（版本由 BOM 管理，无需指定）：

```xml
<dependencies>
    <dependency>
        <groupId>io.github.microsphere-projects</groupId>
        <artifactId>microsphere-alibaba-sentinel-commons</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| 项目 | 版本 |
|------|------|
| Spring Cloud | 2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x） |

### 版本线

| 分支 | 兼容范围 | 最新版本 |
|------|----------|----------|
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.5` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.5` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-alibaba-sentinel)
- [问题反馈](https://github.com/microsphere-projects/microsphere-alibaba-sentinel/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-alibaba-sentinel)
- [Maven Central · microsphere-alibaba-sentinel-commons](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-alibaba-sentinel-commons)

<ProjectNav />
