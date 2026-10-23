---
title: Microsphere Java EE
description: "Implements the Java EE (pre-Jakarta) specifications the Microsphere way, offering a programming model consistent with the rest of the ecosystem for teams that need standardised enterprise APIs."
outline: deep
project:
  slug: microsphere-java-enterprise
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## Overview

Implements the Java EE (pre-Jakarta) specifications the Microsphere way, offering a programming model consistent with the rest of the ecosystem for teams that need standardised enterprise APIs.

## Key Features

- **Specification implementations** — Provides implementation modules for the corresponding Java EE specifications.
- **Ecosystem consistency** — Reuses the reflection, type conversion and event capabilities of Microsphere Java.
- **Parallel with the Jakarta line** — Forms a dual EE / Jakarta support track together with microsphere-jakarta.

## Modules

| Module | |
|------|------|
| `microsphere-java-enterprise` | Aggregator module for the Java EE implementations |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-java-enterprise</artifactId>
            <version>${microsphere-java-enterprise.version}</version>
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

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-java-enterprise)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-java-enterprise/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-java-enterprise)
- [Maven Central · microsphere-java-enterprise](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-java-enterprise)

<ProjectNav></ProjectNav>
