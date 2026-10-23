---
title: Microsphere Resilience4j
description: "Extends Resilience4j so circuit breaker, bulkhead, rate limiter, retry and time limiter patterns can be applied uniformly to Spring Web MVC applications, Feign API clients and database access via MyBatis or JDBC with Druid and P6Spy."
outline: deep
project:
  slug: microsphere-resilience4j
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

Extends Resilience4j so circuit breaker, bulkhead, rate limiter, retry and time limiter patterns can be applied uniformly to Spring Web MVC applications, Feign API clients and database access via MyBatis or JDBC with Druid and P6Spy.

## Key Features

- **Web MVC resilience** — Resilience patterns for Spring Web MVC applications.
- **API client resilience** — Fault tolerance for Feign clients.
- **Database resilience** — Covers MyBatis and JDBC access on top of Druid and P6Spy.
- **Unified programming model** — A consistent Resilience4j integration across different technology stacks.

## Modules

| Module | |
|------|------|
| `microsphere-resilience4j-commons` | Common features of the Resilience4j extension |
| `microsphere-resilience4j-plugins` | Resilience4j plugin collection |
| `microsphere-resilience4j-spring` | Resilience4j Spring integration |
| `microsphere-resilience4j-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-resilience4j-dependencies</artifactId>
            <version>${microsphere-resilience4j.version}</version>
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
        <artifactId>microsphere-resilience4j-commons</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| Spring Cloud | 2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x) |
| Resilience4j | 2.0.0 – 2.4.0 (0.2.x) / 1.3.0 – 1.7.0 (0.1.x) |

### Version Lines

| Branch | | |
|------|----------|----------|
| `main` | Resilience4j 2.0.0 – 2.4.0 | `0.2.4` |
| `1.x` | Resilience4j 1.3.0 – 1.7.0 | `0.1.4` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-resilience4j)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-resilience4j/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-resilience4j)
- [Maven Central · microsphere-resilience4j-commons](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-resilience4j-commons)

<ProjectNav></ProjectNav>
