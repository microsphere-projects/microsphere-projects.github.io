---
title: Microsphere Alibaba Druid
description: "Enhances Alibaba Druid, a high-performance JDBC connection pool, with fine-grained SQL statement interception and logging. It serves as the interception foundation for Sentinel, Resilience4j, Observability and other projects."
outline: deep
project:
  slug: microsphere-alibaba-druid
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

Enhances Alibaba Druid, a high-performance JDBC connection pool, with fine-grained SQL statement interception and logging. It serves as the interception foundation for Sentinel, Resilience4j, Observability and other projects.

## Key Features

- **SQL statement interception** — Intercepts SQL statements at execution time for downstream extensions.
- **SQL logging** — Fine-grained recording of SQL execution.
- **Full Spring stack** — Covers Spring Framework, Spring Boot auto-configuration and Spring Cloud discovery.
- **Ecosystem foundation** — Provides the interception entry point for Sentinel, Resilience4j and Observability.

## Modules

| Module | |
|------|------|
| `microsphere-alibaba-druid-core` | Foundation classes and filters for Druid integration |
| `microsphere-alibaba-druid-spring` | Spring Framework integration and configuration |
| `microsphere-alibaba-druid-spring-boot` | Spring Boot auto-configuration and properties |
| `microsphere-alibaba-druid-spring-cloud` | Spring Cloud features and service discovery integration |
| `microsphere-alibaba-druid-test / spring-test` | Testing utilities |
| `microsphere-alibaba-druid-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-alibaba-druid-dependencies</artifactId>
            <version>${microsphere-alibaba-druid.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

Then add only the modules you need — versions are managed by the BOM:

```xml
<dependencies>
    <dependency>
        <groupId>io.github.microsphere-projects</groupId>
        <artifactId>microsphere-alibaba-druid-spring-cloud</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| Spring Cloud | 2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x) |

### Version Lines

| Branch | | |
|------|----------|----------|
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.21` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.21` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-alibaba-druid)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-alibaba-druid/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-alibaba-druid)
- [Maven Central · microsphere-alibaba-druid-spring-cloud](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-alibaba-druid-spring-cloud)

<ProjectNav></ProjectNav>
