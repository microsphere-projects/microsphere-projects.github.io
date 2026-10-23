---
title: Microsphere Observability
description: "全面提升 Java 应用（以 Spring Boot 生态为主）的监控、指标采集与日志能力。除 Micrometer、Prometheus、Log4j2、Alibaba Sentinel 的专项集成外，还提供 CGroups、网络统计等系统级自定义指标。"
outline: deep
project:
  slug: microsphere-observability
  layer: crosscutting
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

全面提升 Java 应用（以 Spring Boot 生态为主）的监控、指标采集与日志能力。除 Micrometer、Prometheus、Log4j2、Alibaba Sentinel 的专项集成外，还提供 CGroups、网络统计等系统级自定义指标。

## 核心特性

- **Micrometer 集成** — 自定义 MeterBinder 实现，覆盖 Sentinel、JDBC（P6Spy）与系统指标。
- **Prometheus 桥接** — 通过自定义 Collector 把 Sentinel 及其它指标转换为 Prometheus 格式。
- **日志抽象** — logging 模块提供核心日志抽象与动态 layout，含支持 lambda 的 LoggerUtils。
- **Sentinel 指标** — 专门的 Sentinel 指标逻辑与常量定义。
- **系统级指标** — 采集 CGroups、网络统计等系统资源指标。
- **BOM 统一入口** — dependencies 模块集中管理 logging、micrometer、prometheus 等所有内部模块版本。
- **OpenTelemetry 对齐** — 父 POM 导入 OpenTelemetry Instrumentation BOM。

## 模块构成

| 模块 | |
|------|------|
| `microsphere-observability-logging` | 核心日志抽象与动态 layout，含 lambda 版 LoggerUtils |
| `microsphere-observability-metrics-commons` | 基础指标类型与定义 |
| `microsphere-observability-metrics-alibaba-sentinel` | Sentinel 专项指标逻辑与常量 |
| `microsphere-observability-metrics-micrometer` | 自定义 MeterBinder：Sentinel、JDBC(P6Spy)、系统指标 |
| `microsphere-observability-metrics-prometheus` | Prometheus Collector 桥接 |
| `microsphere-observability-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-observability-dependencies</artifactId>
            <version>${microsphere-observability.version}</version>
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
        <artifactId>microsphere-observability-metrics-micrometer</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| | |
|------|------|
| Spring Cloud | 2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x） |

### 版本线

| 分支 | | |
|------|----------|----------|
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.3` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.3` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-observability)
- [问题反馈](https://github.com/microsphere-projects/microsphere-observability/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-observability)
- [Maven Central · microsphere-observability-metrics-micrometer](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-observability-metrics-micrometer)

<ProjectNav></ProjectNav>
