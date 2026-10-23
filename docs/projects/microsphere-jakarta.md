---
title: Microsphere Jakarta
description: "An implementation track targeting the Jakarta EE namespace (jakarta.*), for enterprise applications that have completed the migration away from Java EE."
outline: deep
project:
  slug: microsphere-jakarta
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## Overview

An implementation track targeting the Jakarta EE namespace (jakarta.*), for enterprise applications that have completed the migration away from Java EE.

## Key Features

- **Jakarta namespace** — Fully adapted to the jakarta.* package namespace.
- **Aligned with Spring 6/7** — Matches the Jakarta baseline adopted by Spring Framework 6 and later.

## Modules

| Module | |
|------|------|
| `microsphere-jakarta` | Aggregator module for the Jakarta EE implementations |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-jakarta</artifactId>
            <version>${microsphere-jakarta.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## Requirements

| | |
|------|------|
| Java | 17+ |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-jakarta)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-jakarta/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-jakarta)
- [Maven Central · microsphere-jakarta](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-jakarta)

<ProjectNav></ProjectNav>
