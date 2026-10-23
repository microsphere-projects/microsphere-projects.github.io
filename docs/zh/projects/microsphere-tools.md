---
title: Microsphere Tools
description: "沉淀 Microsphere 生态在日常开发与运维中反复使用的工具类，供各子项目共享。"
outline: deep
project:
  slug: microsphere-tools
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

沉淀 Microsphere 生态在日常开发与运维中反复使用的工具类，供各子项目共享。

## 核心特性

- **工具复用** — 集中收纳跨项目通用的辅助工具。

## 模块构成

| 模块 | |
|------|------|
| `microsphere-tools` | 通用工具聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-tools</artifactId>
            <version>${microsphere-tools.version}</version>
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

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-tools)
- [问题反馈](https://github.com/microsphere-projects/microsphere-tools/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-tools)
- [Maven Central · microsphere-tools](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-tools)

<ProjectNav></ProjectNav>
