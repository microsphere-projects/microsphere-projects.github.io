---
title: Microsphere Resilience4j
description: "扩展 Resilience4j，让熔断、隔板、限流、重试、超时等韧性模式能够以统一方式作用于 Spring Web MVC 应用、Feign API 客户端以及数据库访问（MyBatis、JDBC + Druid + P6Spy）等不同场景。"
outline: deep
project:
  slug: microsphere-resilience4j
  name: Microsphere Resilience4j
  layer: integration
  tagline: 统一的韧性模式落地方案
  lang: Java
  stars: 2
  forks: 9
  artifactId: microsphere-resilience4j-commons
  bom: microsphere-resilience4j-dependencies
  version: 0.2.4
---

<ProjectHeader />

## 它解决什么问题

扩展 Resilience4j，让熔断、隔板、限流、重试、超时等韧性模式能够以统一方式作用于 Spring Web MVC 应用、Feign API 客户端以及数据库访问（MyBatis、JDBC + Druid + P6Spy）等不同场景。

## 核心特性

- **Web MVC 韧性** — 为 Spring Web MVC 应用提供韧性模式支持。
- **API 客户端韧性** — 面向 Feign 客户端的容错能力。
- **数据库访问韧性** — 覆盖 MyBatis 以及 Druid、P6Spy 之上的 JDBC 访问。
- **统一编程模型** — 在不同技术栈上使用一致的 Resilience4j 接入方式。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-resilience4j-commons` | Resilience4j 扩展通用特性 |
| `microsphere-resilience4j-plugins` | Resilience4j 插件集合 |
| `microsphere-resilience4j-spring` | Resilience4j Spring 集成 |
| `microsphere-resilience4j-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-resilience4j-dependencies</artifactId>
            <version>${microsphere-resilience4j.version}</version>
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
        <artifactId>microsphere-resilience4j-commons</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| 项目 | 版本 |
|------|------|
| Spring Cloud | 2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x） |
| Resilience4j | 2.0.0 – 2.4.0（0.2.x）/ 1.3.0 – 1.7.0（0.1.x） |

### 版本线

| 分支 | 兼容范围 | 最新版本 |
|------|----------|----------|
| `main` | Resilience4j 2.0.0 – 2.4.0 | `0.2.4` |
| `1.x` | Resilience4j 1.3.0 – 1.7.0 | `0.1.4` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-resilience4j)
- [问题反馈](https://github.com/microsphere-projects/microsphere-resilience4j/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-resilience4j)
- [Maven Central · microsphere-resilience4j-commons](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-resilience4j-commons)

<ProjectNav />
