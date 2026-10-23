---
title: Microsphere etcd
description: "A Microsphere integration project for the etcd distributed key-value store, usable as a backend for configuration management and service discovery."
outline: deep
project:
  slug: microsphere-etcd
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

A Microsphere integration project for the etcd distributed key-value store, usable as a backend for configuration management and service discovery.

## Key Features

- **etcd integration** — Integration with etcd.

## Modules

| Module | |
|------|------|
| `microsphere-etcd` | Aggregator module for the etcd integration |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-etcd</artifactId>
            <version>${microsphere-etcd.version}</version>
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

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-etcd)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-etcd/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-etcd)
- [Maven Central · microsphere-etcd](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-etcd)

<ProjectNav></ProjectNav>
