---
title: Microsphere Multiactive
description: "面向分布式应用的多活（multi-active）分区感知部署综合框架。应用可自动发现自身所处的部署分区，并实现优先同区调用、跨区兜底的智能路由。"
outline: deep
project:
  slug: microsphere-multiactive
  name: Microsphere Multiactive
  layer: crosscutting
  tagline: 多活与单元化部署的分区感知框架
  lang: Java
  stars: 4
  forks: 14
  artifactId: microsphere-multiactive-commons
  bom: microsphere-multiactive-dependencies
  version: 0.2.13
---

<ProjectHeader />

## 它解决什么问题

面向分布式应用的多活（multi-active）分区感知部署综合框架。应用可自动发现自身所处的部署分区，并实现优先同区调用、跨区兜底的智能路由。

## 核心特性

- **分区自动发现** — 应用自动识别自身所属的部署 zone。
- **同区优先路由** — 优先选择同区实例，并在跨区场景提供降级兜底能力。
- **多云与中间件适配** — 提供 AWS 分区发现与 Netflix OSS 集成模块。
- **全栈 Spring 支持** — 覆盖 Spring Framework、Spring Boot 与 Spring Cloud 三个集成层级。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-multiactive-commons` | 核心分区管理抽象 |
| `microsphere-multiactive-aws` | AWS 分区发现 |
| `microsphere-multiactive-netflix` | Netflix OSS 集成 |
| `microsphere-multiactive-spring` | Spring Framework 集成 |
| `microsphere-multiactive-spring-boot` | Spring Boot 集成 |
| `microsphere-multiactive-spring-cloud` | Spring Cloud 集成 |
| `microsphere-multiactive-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-multiactive-dependencies</artifactId>
            <version>${microsphere-multiactive.version}</version>
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
        <artifactId>microsphere-multiactive-commons</artifactId>
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
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.13` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.13` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-multiactive)
- [问题反馈](https://github.com/microsphere-projects/microsphere-multiactive/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-multiactive)
- [Maven Central · microsphere-multiactive-commons](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-multiactive-commons)

<ProjectNav />
