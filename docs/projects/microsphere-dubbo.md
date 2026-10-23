---
title: Microsphere Dubbo
description: "A Microsphere integration project for the Apache Dubbo RPC framework, bringing the ecosystem's interception, observability and resilience capabilities into Dubbo call chains."
outline: deep
project:
  slug: microsphere-dubbo
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

A Microsphere integration project for the Apache Dubbo RPC framework, bringing the ecosystem's interception, observability and resilience capabilities into Dubbo call chains.

## Key Features

- **Dubbo integration** — Integration with Apache Dubbo.
- **Ecosystem interop** — Combines with Observability, Sentinel and other capabilities.

## Modules

| Module | |
|------|------|
| `microsphere-dubbo` | Aggregator module for the Dubbo integration |

## Getting Started

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

## Requirements

| | |
|------|------|
| Java | 8+ |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-dubbo)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-dubbo/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-dubbo)
- [Maven Central · microsphere-dubbo](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-dubbo)

<ProjectNav></ProjectNav>
