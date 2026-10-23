---
title: Microsphere Logging
description: "Manage logging configuration across a JVM without touching application code or restarting services. It auto-loads the highest-priority Logging implementation via SPI and supports JUL, Log4j, Log4j2 and Logback coexisting in the same process."
outline: deep
project:
  slug: microsphere-logging
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## Overview

Manage logging configuration across a JVM without touching application code or restarting services. It auto-loads the highest-priority Logging implementation via SPI and supports JUL, Log4j, Log4j2 and Logback coexisting in the same process.

## Key Features

- **Runtime level management** — Adjust log levels in production without restarting the service.
- **Framework-agnostic API** — Write management code once; it works across every supported backend.
- **JMX integration** — Expose and control logging configuration through JMX for operations teams.
- **Testing support** — JUnit 4 and JUnit Jupiter 5 extensions to verify behaviour across multiple log levels.
- **SPI-based extensibility** — Load the highest-priority Logging implementation automatically via Java ServiceLoader.
- **Multi-backend coexistence** — Use several logging backends in one JVM with priority-based resolution.

## Modules

| Module | |
|------|------|
| `microsphere-logging-commons` | Core API: Logging interface, LoggingUtils, JMX support |
| `microsphere-java-logging` | Java Logging (JUL) extension |
| `microsphere-logback` | Logback extension |
| `microsphere-log4j` | Log4j extension |
| `microsphere-log4j2` | Log4j2 extension |
| `microsphere-logging-test` | JUnit 4 / JUnit Jupiter 5 test extensions |
| `microsphere-logging-examples` | Runnable examples |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-logging-dependencies</artifactId>
            <version>${microsphere-logging.version}</version>
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
        <artifactId>microsphere-logging-commons</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| Java | 8+ |
| SLF4J | 1.7+ |
| Log4j | 1.2+ |
| Logback | 1.2+ |
| Log4j2 | 2.4+ |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-logging)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-logging/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-logging)
- [Maven Central · microsphere-logging-commons](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-logging-commons)

<ProjectNav></ProjectNav>
