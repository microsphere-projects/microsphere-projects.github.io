---
title: Microsphere Nacos
description: "A Microsphere integration project for Alibaba Nacos, working alongside the configuration management and service discovery capabilities of the Spring Cloud ecosystem."
outline: deep
project:
  slug: microsphere-nacos
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

A Microsphere integration project for Alibaba Nacos, working alongside the configuration management and service discovery capabilities of the Spring Cloud ecosystem.

## Key Features

- **Nacos integration** — Integration with Alibaba Nacos.
- **BOM management** — Unified versioning through the dependencies module.
- **Dual release lines** — main and 1.x branches maintained in parallel.

## Modules

| Module | |
|------|------|
| `microsphere-nacos-dependencies` | BOM centralising dependency management |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-nacos-dependencies</artifactId>
            <version>${microsphere-nacos.version}</version>
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
        <artifactId>microsphere-nacos</artifactId>
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
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.0` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.0` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-nacos)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-nacos/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-nacos)
- [Maven Central · microsphere-nacos](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-nacos)

<ProjectNav></ProjectNav>
