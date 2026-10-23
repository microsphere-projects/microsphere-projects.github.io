---
title: Microsphere MicroProfile
description: "为 MicroProfile 规范提供 Microsphere 实现，面向云原生微服务的配置、容错、指标等标准化需求。"
outline: deep
project:
  slug: microsphere-microprofile
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

为 MicroProfile 规范提供 Microsphere 实现，面向云原生微服务的配置、容错、指标等标准化需求。

## 核心特性

- **MicroProfile 规范** — 覆盖配置、容错、健康检查等 MicroProfile 能力。
- **微服务友好** — 与 Microsphere Spring Cloud 的多注册中心能力互补。

## 模块构成

| 模块 | |
|------|------|
| `microsphere-microprofile` | MicroProfile 实现聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-microprofile</artifactId>
            <version>${microsphere-microprofile.version}</version>
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

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-microprofile)
- [问题反馈](https://github.com/microsphere-projects/microsphere-microprofile/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-microprofile)
- [Maven Central · microsphere-microprofile](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-microprofile)

<ProjectNav></ProjectNav>
