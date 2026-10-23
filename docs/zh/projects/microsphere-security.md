---
title: Microsphere Security
description: "为 Microsphere 生态提供安全相关的扩展能力，与 Spring Security 及生态内的拦截机制协同工作。"
outline: deep
project:
  slug: microsphere-security
  layer: crosscutting
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

为 Microsphere 生态提供安全相关的扩展能力，与 Spring Security 及生态内的拦截机制协同工作。

## 核心特性

- **安全扩展** — 提供面向生态的安全能力扩展。

## 模块构成

| 模块 | |
|------|------|
| `microsphere-security` | 安全扩展聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-security</artifactId>
            <version>${microsphere-security.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## 环境要求

| | |
|------|------|
| Java | 8+ |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-security)
- [问题反馈](https://github.com/microsphere-projects/microsphere-security/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-security)
- [Maven Central · microsphere-security](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-security)

<ProjectNav></ProjectNav>
