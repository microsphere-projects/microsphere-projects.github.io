---
title: Microsphere Build
description: "Supplies unified build settings and plugin configuration inherited by every Microsphere sub-project, including Microsphere Java and Microsphere Spring. Multi-TLS compilation, release signing, coverage and documentation generation are all centralised here, so each repository only carries business code."
outline: deep
project:
  slug: microsphere-build
  layer: foundation
---

<ProjectHeader></ProjectHeader>

## Overview

Supplies unified build settings and plugin configuration inherited by every Microsphere sub-project, including Microsphere Java and Microsphere Spring. Multi-TLS compilation, release signing, coverage and documentation generation are all centralised here, so each repository only carries business code.

## Key Features

- **Multi-TLS language support** — A single POM builds against Java 8, 11, 17, 21 and 25.
- **Centralised plugin management** — Locks Compiler, Source and Flatten plugin versions so no repository drifts.
- **Profile governance** — Six built-in profiles: publish, release, ci, test, coverage and docs, activated on demand.
- **Unified publishing channel** — The publish profile integrates the Central Publishing plugin for the new Maven Central portal.

## Modules

| Module | |
|------|------|
| `Maven Compiler Plugin` | 3.16.0 — compilation across multiple Java TLS versions |
| `Maven Source Plugin` | 3.4.0 — generates source jars |
| `Flatten Maven Plugin` | 1.7.3 — flattens POMs for publishing |
| `Maven JavaDoc Plugin` | 3.12.0 — publish / release profile |
| `Maven GPG Plugin` | 3.2.8 — artifact signing |
| `Git Commit Id Plugin` | 4.9.10 — injects Git metadata |
| `JaCoCo Plugin` | 0.8.15 — coverage profile |
| `Asciidoctor / Docbkx` | documentation generation under the docs profile |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-build</artifactId>
            <version>${microsphere-build.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## Requirements

| | |
|------|------|
| Java | 8 / 11 / 17 / 21 / 25 |
| Maven | 3.6+ |

::: tip Note
Since 0.2.0 the publish profile is the recommended path: OSSRH reached end of life on 2025-06-30 and every namespace migrated to the Central Publisher Portal.
:::

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-build)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-build/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-build)
- [Maven Central · microsphere-build](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-build)

<ProjectNav></ProjectNav>
