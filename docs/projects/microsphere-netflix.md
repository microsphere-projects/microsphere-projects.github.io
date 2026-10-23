---
title: Microsphere Netflix
description: "An enhanced integration framework for Netflix OSS components, focused on Eureka service discovery: high-availability server clustering via Apache Tomcat, enhanced client metadata synchronisation and multi-client management."
outline: deep
project:
  slug: microsphere-netflix
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

An enhanced integration framework for Netflix OSS components, focused on Eureka service discovery: high-availability server clustering via Apache Tomcat, enhanced client metadata synchronisation and multi-client management.

## Key Features

- **Eureka server clustering** — High-availability Eureka Server clustering backed by Apache Tomcat.
- **Enhanced metadata sync** — Enhanced metadata synchronisation on top of the standard Eureka client.
- **Multiple client management** — Manage several Eureka clients within a single application.
- **Standalone core module** — eureka-client-core does not depend on Spring Cloud and can be used on its own.

## Modules

| Module | |
|------|------|
| `microsphere-netflix-eureka-client-core` | Foundational Eureka client capabilities independent of Spring Cloud |
| `microsphere-netflix-eureka-client-spring-cloud` | Spring Cloud integration with enhanced features and multi-client support |
| `microsphere-netflix-eureka-server-spring-cloud` | High-availability Eureka server with Tomcat clustering |
| `microsphere-netflix-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-netflix-dependencies</artifactId>
            <version>${microsphere-netflix.version}</version>
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
        <artifactId>microsphere-netflix-eureka-client-spring-cloud</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| Spring Cloud | 2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x) |

### Version Lines

| Branch | | |
|------|----------|----------|
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.0` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.0` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-netflix)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-netflix/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-netflix)
- [Maven Central · microsphere-netflix-eureka-client-spring-cloud](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-netflix-eureka-client-spring-cloud)

<ProjectNav></ProjectNav>
