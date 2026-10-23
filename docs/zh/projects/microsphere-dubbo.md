---
title: Microsphere Dubbo
description: "面向 Apache Dubbo RPC 框架的 Microsphere 集成项目，把生态中的拦截、可观测与容错能力带到 Dubbo 服务调用链路。"
outline: deep
project:
  slug: microsphere-dubbo
  layer: integration
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

面向 Apache Dubbo RPC 框架的 Microsphere 集成项目，把生态中的拦截、可观测与容错能力带到 Dubbo 服务调用链路。

## 核心特性

- **Dubbo 集成** — 提供与 Apache Dubbo 的集成能力。
- **生态联动** — 可与 Observability、Sentinel 等能力组合。

## 模块构成

| 模块 | |
|------|------|
| `microsphere-dubbo` | Dubbo 集成聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-dubbo</artifactId>
            <version>${microsphere-dubbo.version}</version>
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

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-dubbo)
- [问题反馈](https://github.com/microsphere-projects/microsphere-dubbo/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-dubbo)
- [Maven Central · microsphere-dubbo](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-dubbo)

<ProjectNav></ProjectNav>
