---
title: Microsphere MyBatis
description: "通过一套成熟的拦截管道为 MyBatis 提供强大的 SQL 语句拦截能力，在不改动既有 MyBatis 代码的前提下监控、修改或增强 SQL 执行。"
outline: deep
project:
  slug: microsphere-mybatis
  layer: integration
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

通过一套成熟的拦截管道为 MyBatis 提供强大的 SQL 语句拦截能力，在不改动既有 MyBatis 代码的前提下监控、修改或增强 SQL 执行。

## 核心特性

- **SQL 执行监控** — 为日志、指标与可观测性采集 SQL 执行情况。
- **横切关注点注入** — 为 SQL 操作附加安全、限流、缓存等横切逻辑。
- **SQL 执行增强** — 在不侵入业务代码的前提下扩展 SQL 执行能力。
- **生态联动** — 与 Sentinel、Resilience4j、Observability 等 Microsphere 项目集成。

## 模块构成

| 模块 | |
|------|------|
| `microsphere-mybatis-core` | 核心 MyBatis 框架 |
| `microsphere-mybatis-spring` | Spring Framework 集成与配置 |
| `microsphere-mybatis-spring-boot` | Spring Boot 自动配置与属性 |
| `microsphere-mybatis-spring-cloud` | Spring Cloud 特性集成 |
| `microsphere-mybatis-test / spring-test` | 测试基础设施 |
| `microsphere-mybatis-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-mybatis-dependencies</artifactId>
            <version>${microsphere-mybatis.version}</version>
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
        <artifactId>microsphere-mybatis-core</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| | |
|------|------|
| Spring Cloud | 2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x） |

### 版本线

| 分支 | | |
|------|----------|----------|
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.16` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.16` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-mybatis)
- [问题反馈](https://github.com/microsphere-projects/microsphere-mybatis/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-mybatis)
- [Maven Central · microsphere-mybatis-core](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-mybatis-core)

<ProjectNav></ProjectNav>
