---
title: Microsphere MicroProfile
description: "Provides Microsphere implementations of the MicroProfile specifications, targeting the standardised configuration, fault tolerance and metrics requirements of cloud-native microservices."
outline: deep
project:
  slug: microsphere-microprofile
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## Overview

Provides Microsphere implementations of the MicroProfile specifications, targeting the standardised configuration, fault tolerance and metrics requirements of cloud-native microservices.

## Key Features

- **MicroProfile specifications** — Covers MicroProfile configuration, fault tolerance, health checks and more.
- **Microservice oriented** — Complements the multi-registry capabilities of Microsphere Spring Cloud.

## Modules

| Module | |
|------|------|
| `microsphere-microprofile` | Aggregator module for the MicroProfile implementations |

## Getting Started

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

## Requirements

| | |
|------|------|
| Java | 8+ |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-microprofile)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-microprofile/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-microprofile)
- [Maven Central · microsphere-microprofile](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-microprofile)

<ProjectNav></ProjectNav>
