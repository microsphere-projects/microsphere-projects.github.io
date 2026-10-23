---
title: Microsphere Nacos
description: "面向 Alibaba Nacos 的 Microsphere 集成项目，与 Spring Cloud 生态中的配置管理和服务发现能力协同。"
outline: deep
project:
  slug: microsphere-nacos
  name: Microsphere Nacos
  layer: integration
  tagline: Alibaba Nacos 集成
  lang: Java
  stars: 2
  forks: 6
  artifactId: microsphere-nacos
  bom: microsphere-nacos-dependencies
  version: 0.2.0
---

<ProjectHeader />

## 它解决什么问题

面向 Alibaba Nacos 的 Microsphere 集成项目，与 Spring Cloud 生态中的配置管理和服务发现能力协同。

## 核心特性

- **Nacos 集成** — 提供与 Alibaba Nacos 的集成能力。
- **BOM 管理** — 通过 dependencies 模块统一版本。
- **双线维护** — main 与 1.x 分支并行维护。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-nacos-dependencies` | BOM，集中依赖管理 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-nacos-dependencies</artifactId>
            <version>${microsphere-nacos.version}</version>
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
        <artifactId>microsphere-nacos</artifactId>
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

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-nacos)
- [问题反馈](https://github.com/microsphere-projects/microsphere-nacos/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-nacos)
- [Maven Central · microsphere-nacos](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-nacos)

<ProjectNav />
