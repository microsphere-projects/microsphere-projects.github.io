---
title: Microsphere MyBatis
description: "Provides powerful SQL statement interception through a mature interception pipeline, letting you monitor, modify or enhance SQL execution without changing existing MyBatis code."
outline: deep
project:
  slug: microsphere-mybatis
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

Provides powerful SQL statement interception through a mature interception pipeline, letting you monitor, modify or enhance SQL execution without changing existing MyBatis code.

## Key Features

- **SQL execution monitoring** — Collect execution details for logging, metrics and observability.
- **Cross-cutting concerns** — Attach security, throttling, caching and other concerns to SQL operations.
- **SQL enhancement** — Extend SQL execution capabilities without touching business code.
- **Ecosystem interop** — Integrates with Sentinel, Resilience4j, Observability and other Microsphere projects.

## Modules

| Module | |
|------|------|
| `microsphere-mybatis-core` | Core MyBatis framework |
| `microsphere-mybatis-spring` | Spring Framework integration and configuration |
| `microsphere-mybatis-spring-boot` | Spring Boot auto-configuration and properties |
| `microsphere-mybatis-spring-cloud` | Spring Cloud feature integration |
| `microsphere-mybatis-test / spring-test` | Testing infrastructure |
| `microsphere-mybatis-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-mybatis-dependencies</artifactId>
            <version>${microsphere-mybatis.version}</version>
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
        <artifactId>microsphere-mybatis-core</artifactId>
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
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.16` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.16` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-mybatis)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-mybatis/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-mybatis)
- [Maven Central · microsphere-mybatis-core](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-mybatis-core)

<ProjectNav></ProjectNav>
