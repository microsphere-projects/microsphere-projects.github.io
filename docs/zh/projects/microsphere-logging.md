---
title: Microsphere Logging
description: "在不改动应用代码、不重启服务的前提下，统一管理 JVM 中的日志配置。它通过 SPI 自动装载优先级最高的 Logging 实现，同时支持 JUL、Log4j、Log4j2、Logback 多后端共存。"
outline: deep
project:
  slug: microsphere-logging
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

在不改动应用代码、不重启服务的前提下，统一管理 JVM 中的日志配置。它通过 SPI 自动装载优先级最高的 Logging 实现，同时支持 JUL、Log4j、Log4j2、Logback 多后端共存。

## 核心特性

- **运行时级别调整** — 生产环境动态调整日志级别，无需重启服务。
- **框架无关 API** — 管理代码只写一次，跨全部受支持后端生效。
- **JMX 集成** — 通过 JMX 暴露并操控日志配置，方便运维介入。
- **测试支持** — 提供 JUnit 4 与 JUnit Jupiter 5 扩展，可在多级别下验证日志行为。
- **SPI 可扩展** — 通过 Java ServiceLoader 自动加载最高优先级的 Logging 实现。
- **多后端共存** — 同一 JVM 内可并行使用多个日志后端，按优先级解析。

## 模块构成

| 模块 | |
|------|------|
| `microsphere-logging-commons` | 核心 API：Logging 接口、LoggingUtils、JMX 支持 |
| `microsphere-java-logging` | Java Logging（JUL）扩展 |
| `microsphere-logback` | Logback 扩展 |
| `microsphere-log4j` | Log4j 扩展 |
| `microsphere-log4j2` | Log4j2 扩展 |
| `microsphere-logging-test` | JUnit 4 / JUnit Jupiter 5 测试扩展 |
| `microsphere-logging-examples` | 可运行示例 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-logging-dependencies</artifactId>
            <version>${microsphere-logging.version}</version>
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
        <artifactId>microsphere-logging-commons</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| | |
|------|------|
| Java | 8+ |
| SLF4J | 1.7+ |
| Log4j | 1.2+ |
| Logback | 1.2+ |
| Log4j2 | 2.4+ |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-logging)
- [问题反馈](https://github.com/microsphere-projects/microsphere-logging/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-logging)
- [Maven Central · microsphere-logging-commons](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-logging-commons)

<ProjectNav></ProjectNav>
