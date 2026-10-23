---
title: Microsphere Alibaba Druid
description: "增强 Alibaba Druid 高性能 JDBC 连接池，提供细粒度的 SQL 语句拦截与日志能力，并作为 Sentinel、Resilience4j、Observability 等项目的底层扩展支撑。"
outline: deep
project:
  slug: microsphere-alibaba-druid
  name: Microsphere Alibaba Druid
  layer: integration
  tagline: 为 Druid 连接池注入 SQL 拦截能力
  lang: Java
  stars: 2
  forks: 3
  artifactId: microsphere-alibaba-druid-spring-cloud
  bom: microsphere-alibaba-druid-dependencies
  version: 0.2.21
---

<ProjectHeader />

## 它解决什么问题

增强 Alibaba Druid 高性能 JDBC 连接池，提供细粒度的 SQL 语句拦截与日志能力，并作为 Sentinel、Resilience4j、Observability 等项目的底层扩展支撑。

## 核心特性

- **SQL 语句拦截** — 在执行阶段拦截 SQL 语句，供上下游项目扩展。
- **SQL 日志记录** — 细粒度记录 SQL 执行情况。
- **Spring 全栈集成** — 覆盖 Spring Framework、Spring Boot 自动配置、Spring Cloud 服务发现。
- **生态底座** — 为 Sentinel、Resilience4j、Observability 提供拦截入口。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-alibaba-druid-core` | Druid 集成的基础类与过滤器 |
| `microsphere-alibaba-druid-spring` | Spring Framework 集成与配置 |
| `microsphere-alibaba-druid-spring-boot` | Spring Boot 自动配置与属性 |
| `microsphere-alibaba-druid-spring-cloud` | Spring Cloud 特性与服务发现集成 |
| `microsphere-alibaba-druid-test / spring-test` | 测试工具 |
| `microsphere-alibaba-druid-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-alibaba-druid-dependencies</artifactId>
            <version>${microsphere-alibaba-druid.version}</version>
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
        <artifactId>microsphere-alibaba-druid-spring-cloud</artifactId>
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
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.21` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.21` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-alibaba-druid)
- [问题反馈](https://github.com/microsphere-projects/microsphere-alibaba-druid/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-alibaba-druid)
- [Maven Central · microsphere-alibaba-druid-spring-cloud](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-alibaba-druid-spring-cloud)

<ProjectNav />
