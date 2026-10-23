---
title: Microsphere Hibernate
description: "为 Hibernate ORM 提供 Microsphere 扩展能力，覆盖 Hibernate 6.2 – 7.3 与 5.0 – 5.6 两条主要版本线。"
outline: deep
project:
  slug: microsphere-hibernate
  name: Microsphere Hibernate
  layer: integration
  tagline: Hibernate ORM 扩展
  lang: Java
  stars: 0
  forks: 1
  artifactId: microsphere-hibernate-core
  bom: microsphere-hibernate-dependencies
  version: 0.2.10
---

<ProjectHeader />

## 它解决什么问题

为 Hibernate ORM 提供 Microsphere 扩展能力，覆盖 Hibernate 6.2 – 7.3 与 5.0 – 5.6 两条主要版本线。

## 核心特性

- **ORM 扩展** — 提供 Hibernate ORM 的核心扩展特性。
- **测试框架** — 专门的 Hibernate ORM 测试支持模块。
- **宽版本覆盖** — 0.2.x 支持 Hibernate 6.2 – 7.3，0.1.x 支持 5.0 – 5.6。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-hibernate-core` | Hibernate ORM 扩展核心特性 |
| `microsphere-hibernate-test` | Hibernate ORM 测试框架 |
| `microsphere-hibernate-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-hibernate-dependencies</artifactId>
            <version>${microsphere-hibernate.version}</version>
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
        <artifactId>microsphere-hibernate-core</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| 项目 | 版本 |
|------|------|
| JDK | 17 – 25 |
| Hibernate Core | 6.2.x – 7.3.x（0.2.x）/ 5.0.x – 5.6.x（0.1.x） |

### 版本线

| 分支 | 兼容范围 | 最新版本 |
|------|----------|----------|
| `main` | Hibernate 6.2 – 7.3 | `0.2.10` |
| `1.x` | Hibernate 5.0 – 5.6 | `0.1.10` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-hibernate)
- [问题反馈](https://github.com/microsphere-projects/microsphere-hibernate/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-hibernate)
- [Maven Central · microsphere-hibernate-core](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-hibernate-core)

<ProjectNav />
