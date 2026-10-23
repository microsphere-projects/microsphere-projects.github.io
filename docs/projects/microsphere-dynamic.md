---
title: Microsphere Dynamic
description: "为生态提供动态化基础能力，支撑运行时配置刷新、Feign 组件热更新等免重启变更场景。"
outline: deep
project:
  slug: microsphere-dynamic
  name: Microsphere Dynamic
  layer: crosscutting
  tagline: 动态化能力支撑
  lang: Java
  stars: 3
  forks: 7
  artifactId: microsphere-dynamic
---

<ProjectHeader />

## 它解决什么问题

为生态提供动态化基础能力，支撑运行时配置刷新、Feign 组件热更新等免重启变更场景。

## 核心特性

- **动态化支撑** — 为运行时动态变更提供基础设施。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-dynamic` | 动态化能力聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-dynamic</artifactId>
            <version>${microsphere-dynamic.version}</version>
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

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-dynamic)
- [问题反馈](https://github.com/microsphere-projects/microsphere-dynamic/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-dynamic)
- [Maven Central · microsphere-dynamic](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-dynamic)

<ProjectNav />
