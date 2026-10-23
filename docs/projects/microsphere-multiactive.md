---
title: Microsphere Multiactive
description: "A comprehensive framework for implementing multi-active, zone-aware deployments in distributed applications. Applications discover their own deployment zone and route intelligently — preferring same-zone instances while providing cross-zone fallback."
outline: deep
project:
  slug: microsphere-multiactive
  layer: crosscutting
---

<ProjectHeader></ProjectHeader>

## Overview

A comprehensive framework for implementing multi-active, zone-aware deployments in distributed applications. Applications discover their own deployment zone and route intelligently — preferring same-zone instances while providing cross-zone fallback.

## Key Features

- **Automatic zone discovery** — Applications identify the deployment zone they belong to.
- **Same-zone preference** — Prefers same-zone instances with graceful fallback for cross-zone scenarios.
- **Cloud and middleware adapters** — Modules for AWS zone discovery and Netflix OSS integration.
- **Full Spring stack** — Covers Spring Framework, Spring Boot and Spring Cloud integration levels.

## Modules

| Module | |
|------|------|
| `microsphere-multiactive-commons` | Core zone management abstractions |
| `microsphere-multiactive-aws` | AWS zone discovery |
| `microsphere-multiactive-netflix` | Netflix OSS integration |
| `microsphere-multiactive-spring` | Spring Framework integration |
| `microsphere-multiactive-spring-boot` | Spring Boot integration |
| `microsphere-multiactive-spring-cloud` | Spring Cloud integration |
| `microsphere-multiactive-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-multiactive-dependencies</artifactId>
            <version>${microsphere-multiactive.version}</version>
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
        <artifactId>microsphere-multiactive-commons</artifactId>
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
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.13` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.13` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-multiactive)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-multiactive/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-multiactive)
- [Maven Central · microsphere-multiactive-commons](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-multiactive-commons)

<ProjectNav></ProjectNav>
