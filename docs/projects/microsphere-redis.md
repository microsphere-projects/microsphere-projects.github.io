---
title: Microsphere Redis
description: "在 Spring Data Redis 之上提供企业级增强能力：非侵入式的 Redis 命令拦截、深度 Spring 集成、全面的事件发布与指标采集，以及基于 Kafka 的 Redis 复制支持。"
outline: deep
project:
  slug: microsphere-redis
  name: Microsphere Redis
  layer: integration
  tagline: 增强版 Spring Data Redis 集成框架
  lang: Java
  stars: 3
  forks: 11
  artifactId: microsphere-redis-spring
  bom: microsphere-redis-dependencies
  version: 0.2.14
---

<ProjectHeader />

## 它解决什么问题

在 Spring Data Redis 之上提供企业级增强能力：非侵入式的 Redis 命令拦截、深度 Spring 集成、全面的事件发布与指标采集，以及基于 Kafka 的 Redis 复制支持。

## 核心特性

- **非侵入式操作拦截** — 无需修改应用代码即可监控与拦截 Redis 命令。
- **Spring 深度集成** — 与 Spring 依赖注入和自动配置无缝衔接。
- **企业级监控** — 全面的事件发布与指标采集能力。
- **Redis 复制支持** — 高级复制特性，并与 Kafka 集成。
- **模块化架构** — 多 Maven 模块清晰分离关注点。
- **元数据生成** — generator 模块负责 Redis 元数据生成。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-redis-core` | Redis 操作的基础组件与工具 |
| `microsphere-redis-spring` | Spring Framework 集成 |
| `microsphere-redis-spring-boot` | Spring Boot 集成 |
| `microsphere-redis-spring-cloud` | Spring Cloud 集成 |
| `microsphere-redis-replicator-spring` | Redis 复制支持 |
| `microsphere-redis-spring-test` | Spring Test 集成 |
| `microsphere-redis-generator` | Redis 元数据生成 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-redis-dependencies</artifactId>
            <version>${microsphere-redis.version}</version>
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
        <artifactId>microsphere-redis-spring</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| 项目 | 版本 |
|------|------|
| Spring Data Redis | 3.0.0 – 3.5.x（main）/ 2.1.0 – 2.7.x（1.x） |

### 版本线

| 分支 | 兼容范围 | 最新版本 |
|------|----------|----------|
| `main` | Spring Data Redis 3.0.0 – 3.5.x | `0.2.14` |
| `1.x` | Spring Data Redis 2.1.0 – 2.7.x | `0.1.14` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-redis)
- [问题反馈](https://github.com/microsphere-projects/microsphere-redis/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-redis)
- [Maven Central · microsphere-redis-spring](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-redis-spring)

<ProjectNav />
