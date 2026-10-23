---
title: Microsphere Jakarta
description: "面向 Jakarta EE 命名空间（jakarta.*）的实现分支，适配从 Java EE 迁移后的企业应用。"
outline: deep
project:
  slug: microsphere-jakarta
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

面向 Jakarta EE 命名空间（jakarta.*）的实现分支，适配从 Java EE 迁移后的企业应用。

## 核心特性

- **Jakarta 命名空间** — 全面适配 jakarta.* 包名。
- **与 Spring 6/7 对齐** — 匹配 Spring Framework 6+ 采用的 Jakarta 基线。

## 模块构成

| 模块 | |
|------|------|
| `microsphere-jakarta` | Jakarta EE 实现聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-jakarta</artifactId>
            <version>${microsphere-jakarta.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## 环境要求

| | |
|------|------|
| Java | 17+ |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-jakarta)
- [问题反馈](https://github.com/microsphere-projects/microsphere-jakarta/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-jakarta)
- [Maven Central · microsphere-jakarta](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-jakarta)

<ProjectNav></ProjectNav>
