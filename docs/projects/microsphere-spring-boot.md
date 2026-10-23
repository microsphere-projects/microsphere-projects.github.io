---
title: Microsphere Spring Boot
description: "Adds production-ready capabilities to Spring Boot applications around configuration management, application diagnostics and enhanced monitoring: sensible out-of-the-box defaults, Actuator endpoints that expose far more runtime state, and cross-version compatibility from Spring Boot 2.x to 4.x."
outline: deep
project:
  slug: microsphere-spring-boot
  layer: framework
---

<ProjectHeader></ProjectHeader>

## Overview

Adds production-ready capabilities to Spring Boot applications around configuration management, application diagnostics and enhanced monitoring: sensible out-of-the-box defaults, Actuator endpoints that expose far more runtime state, and cross-version compatibility from Spring Boot 2.x to 4.x.

## Key Features

- **Default properties** — Loads graceful shutdown, MVC filter toggles and other defaults from config/default/*.properties on the classpath, overridable per module.
- **Advanced auto-configuration management** — A configurable import filter that merges multiple microsphere.autoconfigure.exclude sources without losing earlier exclusions.
- **Configuration property binding listeners** — Event-driven BindListener hooks notify your beans whenever a @ConfigurationProperties-bound value changes.
- **Custom Actuator endpoints** — Four additional endpoints expose classpath artifact metadata, web endpoint mappings, configuration metadata and bound configuration properties.
- **Monitored task scheduler** — A ThreadPoolTaskScheduler wrapper that records execution metrics via Micrometer — task latency and counts out of the box.
- **Artifact collision detection** — Detects duplicate JAR artifacts on the classpath at startup and surfaces a descriptive FailureAnalyzer message.
- **Multi-version compatibility** — A dedicated compatibility shim keeps one codebase running on Spring Boot 2.x through 4.x without forking.

## Modules

| Module | |
|------|------|
| `microsphere-spring-boot-core` | Core: default properties, auto-configuration filter, bind listeners, diagnostics |
| `microsphere-spring-boot-actuator` | Actuator extensions: custom endpoints, monitored scheduler, endpoint defaults |
| `microsphere-spring-boot-compatible` | Compatibility shim for Spring Boot 2.x – 4.x (not published to Maven Central) |
| `microsphere-spring-boot-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-spring-boot-dependencies</artifactId>
            <version>${microsphere-spring-boot.version}</version>
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
        <artifactId>microsphere-spring-boot-core</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| Java | 17+ |
| Spring Boot | 3.0.x – 4.1.x (main) / 2.0.x – 2.7.x (1.x) |
| Maven | 3.9+ |

### Version Lines

| Branch | | |
|------|----------|----------|
| `main` | 3.0.x – 3.5.x, 4.0.x – 4.1.x | `0.2.34` |
| `1.x` | 2.0.x – 2.7.x | `0.1.34` |

::: tip Note
Unlike spring.autoconfigure.exclude, which replaces earlier values, microsphere.autoconfigure.exclude uses merge semantics: exclusions from multiple sources accumulate.
:::

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-spring-boot)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-spring-boot/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-spring-boot)
- [Maven Central · microsphere-spring-boot-core](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-spring-boot-core)

<ProjectNav></ProjectNav>
