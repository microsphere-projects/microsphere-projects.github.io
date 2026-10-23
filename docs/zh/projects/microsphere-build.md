---
title: Microsphere Build
description: "提供统一的构建设置与插件配置，被 Microsphere Java、Microsphere Spring 等所有子项目继承。它把 Java 多 TLS 版本编译、发布签名、覆盖率、文档生成等能力收敛到一处，让各子仓库只关心业务代码。"
outline: deep
project:
  slug: microsphere-build
  layer: foundation
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

提供统一的构建设置与插件配置，被 Microsphere Java、Microsphere Spring 等所有子项目继承。它把 Java 多 TLS 版本编译、发布签名、覆盖率、文档生成等能力收敛到一处，让各子仓库只关心业务代码。

## 核心特性

- **语言版本支持** — 同一份 POM 覆盖 Java 8、11、17、21、25 五个 TLS 版本的构建。
- **插件集中管理** — 统一锁定 Compiler、Source、Flatten 等默认插件版本，避免各仓库版本漂移。
- **Profile 治理** — 内置 publish、release、ci、test、coverage、docs 六套 profile，按需激活。
- **统一发布通道** — publish profile 集成 Central Publishing 插件，对接 Maven Central 新发布门户。

## 模块构成

| 模块 | |
|------|------|
| `Maven Compiler Plugin` | 3.16.0 — 编译，支持多 Java TLS 版本 |
| `Maven Source Plugin` | 3.4.0 — 生成源码 jar |
| `Flatten Maven Plugin` | 1.7.3 — 扁平化 POM 以便发布 |
| `Maven JavaDoc Plugin` | 3.12.0 — publish / release profile |
| `Maven GPG Plugin` | 3.2.8 — 制品签名 |
| `Git Commit Id Plugin` | 4.9.10 — 注入 Git 元信息 |
| `JaCoCo Plugin` | 0.8.15 — coverage profile |
| `Asciidoctor / Docbkx` | docs profile 下的文档生成 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-build</artifactId>
            <version>${microsphere-build.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## 环境要求

| | |
|------|------|
| Java | 8 / 11 / 17 / 21 / 25 |
| Maven | 3.6+ |

::: tip 注意
自 0.2.0 起推荐使用 publish profile：OSSRH 已于 2025-06-30 下线，命名空间全部迁移至 Central Publisher Portal。
:::

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-build)
- [问题反馈](https://github.com/microsphere-projects/microsphere-build/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-build)
- [Maven Central · microsphere-build](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-build)

<ProjectNav></ProjectNav>
