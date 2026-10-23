---
title: Microsphere Configuration
description: "围绕配置体系提供增强能力，与 Spring Environment、@ConfigurationProperties 以及 Spring Cloud 配置刷新机制协同。"
outline: deep
project:
  slug: microsphere-configuration
  name: Microsphere Configuration
  layer: crosscutting
  tagline: 配置体系增强
  lang: Java
  stars: 2
  forks: 10
  artifactId: microsphere-configuration
---

<ProjectHeader />

## 它解决什么问题

围绕配置体系提供增强能力，与 Spring Environment、@ConfigurationProperties 以及 Spring Cloud 配置刷新机制协同。

## 核心特性

- **配置增强** — 提供配置体系相关的增强能力。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-configuration` | 配置增强聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-configuration</artifactId>
            <version>${microsphere-configuration.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## 环境要求

| 项目 | 版本 |
|------|------|
| Java | 8+ |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-configuration)
- [问题反馈](https://github.com/microsphere-projects/microsphere-configuration/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-configuration)
- [Maven Central · microsphere-configuration](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-configuration)

<ProjectNav />
