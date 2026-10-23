---
title: Microsphere Observability
description: "Improves the monitoring, metrics collection and logging capabilities of Java applications, with a primary focus on the Spring Boot ecosystem. Beyond dedicated integrations for Micrometer, Prometheus, Log4j2 and Alibaba Sentinel, it ships custom metrics for system-level resources such as CGroups and network statistics."
outline: deep
project:
  slug: microsphere-observability
  layer: crosscutting
---

<ProjectHeader></ProjectHeader>

## Overview

Improves the monitoring, metrics collection and logging capabilities of Java applications, with a primary focus on the Spring Boot ecosystem. Beyond dedicated integrations for Micrometer, Prometheus, Log4j2 and Alibaba Sentinel, it ships custom metrics for system-level resources such as CGroups and network statistics.

## Key Features

- **Micrometer integration** — Custom MeterBinder implementations covering Sentinel, JDBC (P6Spy) and system metrics.
- **Prometheus bridge** — Custom Collectors convert Sentinel and other metrics into Prometheus format.
- **Logging abstraction** — The logging module provides core abstractions and dynamic layouts, including a lambda-friendly LoggerUtils.
- **Sentinel metrics** — Dedicated Sentinel metric logic and constants.
- **System-level metrics** — Collects CGroups, network statistics and other system resource metrics.
- **Single BOM entry point** — The dependencies module manages logging, micrometer, prometheus and all internal module versions.
- **OpenTelemetry alignment** — The parent POM imports the OpenTelemetry Instrumentation BOM.

## Modules

| Module | |
|------|------|
| `microsphere-observability-logging` | Core logging abstraction and dynamic layouts, including a lambda-based LoggerUtils |
| `microsphere-observability-metrics-commons` | Foundational metric types and definitions |
| `microsphere-observability-metrics-alibaba-sentinel` | Sentinel-specific metric logic and constants |
| `microsphere-observability-metrics-micrometer` | Custom MeterBinders: Sentinel, JDBC (P6Spy), system metrics |
| `microsphere-observability-metrics-prometheus` | Prometheus Collector bridge |
| `microsphere-observability-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-observability-dependencies</artifactId>
            <version>${microsphere-observability.version}</version>
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
        <artifactId>microsphere-observability-metrics-micrometer</artifactId>
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
| `main` | Spring Cloud 2022.0.x – 2025.0.x | `0.2.3` |
| `1.x` | Spring Cloud Hoxton – 2021.0.x | `0.1.3` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-observability)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-observability/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-observability)
- [Maven Central · microsphere-observability-metrics-micrometer](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-observability-metrics-micrometer)

<ProjectNav></ProjectNav>
