---
title: Microsphere BOM
description: "集中声明 Microsphere 生态各模块的版本，使用者导入一次即可对齐全部依赖版本，避免多模块之间的版本冲突。"
outline: deep
project:
  slug: microsphere-bom
  layer: foundation
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

集中声明 Microsphere 生态各模块的版本，使用者导入一次即可对齐全部依赖版本，避免多模块之间的版本冲突。

## 核心特性

- **单点版本对齐** — 导入 BOM 后无需为每个模块指定 `<version>`。
- **跨仓库一致性** — 与各子项目的 dependencies 模块保持版本同步。
- **与 Build 协同** — 配合 microsphere-build 父 POM 使用，构建与依赖口径统一。

## 模块构成

| 模块 | |
|------|------|
| `microsphere-bom` | 顶层 BOM，聚合各子项目版本 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-bom</artifactId>
            <version>${microsphere-bom.version}</version>
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
| Maven | 3.6+ |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-bom)
- [问题反馈](https://github.com/microsphere-projects/microsphere-bom/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-bom)
- [Maven Central · microsphere-bom](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-bom)

<ProjectNav></ProjectNav>
