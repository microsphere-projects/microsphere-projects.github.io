---
title: Microsphere BOM
description: "Declares the versions of every Microsphere module in one place. Import it once to align all dependency versions and avoid conflicts across modules."
outline: deep
project:
  slug: microsphere-bom
  layer: foundation
---

<ProjectHeader></ProjectHeader>

## Overview

Declares the versions of every Microsphere module in one place. Import it once to align all dependency versions and avoid conflicts across modules.

## Key Features

- **Single point of version alignment** — No need to declare a version for each module after importing the BOM.
- **Cross-repository consistency** — Kept in sync with each sub-project's own dependencies module.
- **Works with Build** — Pairs with the microsphere-build parent POM for a single build and dependency baseline.

## Modules

| Module | |
|------|------|
| `microsphere-bom` | Top-level BOM aggregating every sub-project version |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-bom</artifactId>
            <version>${microsphere-bom.version}</version>
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
| Maven | 3.6+ |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-bom)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-bom/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-bom)
- [Maven Central · microsphere-bom](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-bom)

<ProjectNav></ProjectNav>
