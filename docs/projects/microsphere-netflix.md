---
title: Microsphere Netflix
description: "面向 Netflix OSS 组件的增强集成框架，聚焦 Eureka 服务发现：通过 Apache Tomcat 实现服务端高可用集群，并增强客户端元数据同步与多客户端管理能力。"
outline: deep
project:
  slug: microsphere-netflix
  name: Microsphere Netflix
  layer: integration
  tagline: Eureka 的高可用集群与增强客户端
  lang: Java
  stars: 2
  forks: 8
  artifactId: microsphere-netflix-eureka-client-spring-cloud
  bom: microsphere-netflix-dependencies
  version: 0.2.0
---

<ProjectHeader />

## 它解决什么问题

面向 Netflix OSS 组件的增强集成框架，聚焦 Eureka 服务发现：通过 Apache Tomcat 实现服务端高可用集群，并增强客户端元数据同步与多客户端管理能力。

## 核心特性

- **Eureka 服务端集群** — 基于 Apache Tomcat 的高可用 Eureka Server 集群能力。
- **增强客户端元数据同步** — 在标准 Eureka 客户端之上增强元数据同步。
- **多客户端管理** — 支持在同一应用内管理多个 Eureka 客户端。
- **独立核心模块** — eureka-client-core 不依赖 Spring Cloud，可独立使用。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-netflix-eureka-client-core` | 不依赖 Spring Cloud 的基础 Eureka 客户端能力 |
| `microsphere-netflix-eureka-client-spring-cloud` | Spring Cloud 集成，增强特性与多客户端支持 |
| `microsphere-netflix-eureka-server-spring-cloud` | 具备 Tomcat 集群能力的高可用 Eureka 服务端 |
| `microsphere-netflix-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-netflix-dependencies</artifactId>
            <version>${microsphere-netflix.version}</version>
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
        <artifactId>microsphere-netflix-eureka-client-spring-cloud</artifactId>
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
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.0` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.0` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-netflix)
- [问题反馈](https://github.com/microsphere-projects/microsphere-netflix/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-netflix)
- [Maven Central · microsphere-netflix-eureka-client-spring-cloud](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-netflix-eureka-client-spring-cloud)

<ProjectNav />
