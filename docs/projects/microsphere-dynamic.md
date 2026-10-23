---
title: Microsphere Dynamic
description: "Provides the dynamism foundation for the ecosystem, supporting restart-free change scenarios such as runtime configuration refresh and hot updates of Feign components."
outline: deep
project:
  slug: microsphere-dynamic
  layer: crosscutting
---

<ProjectHeader></ProjectHeader>

## Overview

Provides the dynamism foundation for the ecosystem, supporting restart-free change scenarios such as runtime configuration refresh and hot updates of Feign components.

## Key Features

- **Dynamic foundation** — Infrastructure for runtime dynamic changes.

## Modules

| Module | |
|------|------|
| `microsphere-dynamic` | Aggregator module for dynamic capabilities |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-dynamic</artifactId>
            <version>${microsphere-dynamic.version}</version>
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

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-dynamic)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-dynamic/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-dynamic)
- [Maven Central · microsphere-dynamic](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-dynamic)

<ProjectNav></ProjectNav>
