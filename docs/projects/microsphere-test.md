---
title: Microsphere Test
description: "Provides a shared testing baseline and assertion utilities so every Microsphere sub-project follows the same testing conventions."
outline: deep
project:
  slug: microsphere-test
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## Overview

Provides a shared testing baseline and assertion utilities so every Microsphere sub-project follows the same testing conventions.

## Key Features

- **Unified testing baseline** — Centralised test base classes and helper assertions.

## Modules

| Module | |
|------|------|
| `microsphere-test` | Aggregator module for testing infrastructure |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-test</artifactId>
            <version>${microsphere-test.version}</version>
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

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-test)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-test/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-test)
- [Maven Central · microsphere-test](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-test)

<ProjectNav></ProjectNav>
