---
title: Microsphere Hibernate
description: "Provides Microsphere extensions for Hibernate ORM, covering both the Hibernate 6.2 – 7.3 and 5.0 – 5.6 lines."
outline: deep
project:
  slug: microsphere-hibernate
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

Provides Microsphere extensions for Hibernate ORM, covering both the Hibernate 6.2 – 7.3 and 5.0 – 5.6 lines.

## Key Features

- **ORM extensions** — Core extension features for Hibernate ORM.
- **Testing framework** — A dedicated test support module for Hibernate ORM.
- **Broad version coverage** — 0.2.x supports Hibernate 6.2 – 7.3; 0.1.x supports 5.0 – 5.6.

## Modules

| Module | |
|------|------|
| `microsphere-hibernate-core` | Core extension features for Hibernate ORM |
| `microsphere-hibernate-test` | Testing framework for Hibernate ORM |
| `microsphere-hibernate-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-hibernate-dependencies</artifactId>
            <version>${microsphere-hibernate.version}</version>
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
        <artifactId>microsphere-hibernate-core</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| JDK | 17 – 25 |
| Hibernate Core | 6.2.x – 7.3.x (0.2.x) / 5.0.x – 5.6.x (0.1.x) |

### Version Lines

| Branch | | |
|------|----------|----------|
| `main` | Hibernate 6.2 – 7.3 | `0.2.10` |
| `1.x` | Hibernate 5.0 – 5.6 | `0.1.10` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-hibernate)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-hibernate/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-hibernate)
- [Maven Central · microsphere-hibernate-core](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-hibernate-core)

<ProjectNav></ProjectNav>
