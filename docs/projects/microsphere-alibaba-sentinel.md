---
title: Microsphere Alibaba Sentinel
description: "An abstraction layer that integrates Alibaba Sentinel's flow control framework with common Java technologies, applying Sentinel's flow control, circuit breaking and system protection transparently to database operations, caching and other infrastructure components."
outline: deep
project:
  slug: microsphere-alibaba-sentinel
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

An abstraction layer that integrates Alibaba Sentinel's flow control framework with common Java technologies, applying Sentinel's flow control, circuit breaking and system protection transparently to database operations, caching and other infrastructure components.

## Key Features

- **Web layer flow control** — Covers Spring WebMVC and Spring WebFlux.
- **Data access flow control** — Covers Alibaba Druid, Hibernate, MyBatis and P6Spy.
- **Cache layer flow control** — Covers Spring Data Redis.
- **Incremental adoption** — Both low-level integration APIs and high-level Spring Boot auto-configuration, so protection can be adopted step by step.

## Modules

| Module | |
|------|------|
| `microsphere-alibaba-sentinel-commons` | Common features of the Sentinel extension |
| `microsphere-alibaba-sentinel-plugins` | Sentinel plugin collection |
| `microsphere-alibaba-sentinel-spring` | Alibaba Sentinel Spring integration |
| `microsphere-alibaba-sentinel-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-alibaba-sentinel-dependencies</artifactId>
            <version>${microsphere-alibaba-sentinel.version}</version>
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
        <artifactId>microsphere-alibaba-sentinel-commons</artifactId>
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
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.5` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.5` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-alibaba-sentinel)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-alibaba-sentinel/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-alibaba-sentinel)
- [Maven Central · microsphere-alibaba-sentinel-commons](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-alibaba-sentinel-commons)

<ProjectNav></ProjectNav>
