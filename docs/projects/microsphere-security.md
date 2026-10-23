---
title: Microsphere Security
description: "Provides security-related extensions for the Microsphere ecosystem, working alongside Spring Security and the ecosystem's interception mechanisms."
outline: deep
project:
  slug: microsphere-security
  layer: crosscutting
---

<ProjectHeader></ProjectHeader>

## Overview

Provides security-related extensions for the Microsphere ecosystem, working alongside Spring Security and the ecosystem's interception mechanisms.

## Key Features

- **Security extensions** — Security capability extensions for the ecosystem.

## Modules

| Module | |
|------|------|
| `microsphere-security` | Aggregator module for the security extensions |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-security</artifactId>
            <version>${microsphere-security.version}</version>
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

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-security)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-security/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-security)
- [Maven Central · microsphere-security](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-security)

<ProjectNav></ProjectNav>
