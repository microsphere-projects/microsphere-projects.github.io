---
title: Microsphere Tools
description: "Collects the utilities repeatedly used across the ecosystem during day-to-day development and operations, shared by every sub-project."
outline: deep
project:
  slug: microsphere-tools
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## Overview

Collects the utilities repeatedly used across the ecosystem during day-to-day development and operations, shared by every sub-project.

## Key Features

- **Tool reuse** — A single home for utilities shared across projects.

## Modules

| Module | |
|------|------|
| `microsphere-tools` | Aggregator module for shared utilities |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-tools</artifactId>
            <version>${microsphere-tools.version}</version>
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

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-tools)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-tools/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-tools)
- [Maven Central · microsphere-tools](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-tools)

<ProjectNav></ProjectNav>
