---
title: Microsphere Redis
description: "Adds enterprise-grade capabilities on top of Spring Data Redis: non-intrusive command interception, deep Spring integration, comprehensive event publishing and metrics collection, and Redis replication support backed by Kafka."
outline: deep
project:
  slug: microsphere-redis
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

Adds enterprise-grade capabilities on top of Spring Data Redis: non-intrusive command interception, deep Spring integration, comprehensive event publishing and metrics collection, and Redis replication support backed by Kafka.

## Key Features

- **Non-intrusive interception** — Monitor and intercept Redis commands without modifying application code.
- **Deep Spring integration** — Seamless integration with Spring dependency injection and auto-configuration.
- **Enterprise monitoring** — Comprehensive event publishing and metrics collection.
- **Redis replication** — Advanced replication features integrated with Kafka.
- **Modular architecture** — Multiple Maven modules with clean separation of concerns.
- **Metadata generation** — A dedicated generator module produces Redis metadata.

## Modules

| Module | |
|------|------|
| `microsphere-redis-core` | Foundational components and utilities for Redis operations |
| `microsphere-redis-spring` | Spring Framework integration |
| `microsphere-redis-spring-boot` | Spring Boot integration |
| `microsphere-redis-spring-cloud` | Spring Cloud integration |
| `microsphere-redis-replicator-spring` | Redis replication support |
| `microsphere-redis-spring-test` | Spring Test integration |
| `microsphere-redis-generator` | Redis metadata generation |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-redis-dependencies</artifactId>
            <version>${microsphere-redis.version}</version>
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
        <artifactId>microsphere-redis-spring</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| Spring Data Redis | 3.0.0 – 3.5.x (main) / 2.1.0 – 2.7.x (1.x) |

### Version Lines

| Branch | | |
|------|----------|----------|
| `main` | Spring Data Redis 3.0.0 – 3.5.x | `0.2.14` |
| `1.x` | Spring Data Redis 2.1.0 – 2.7.x | `0.1.14` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-redis)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-redis/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-redis)
- [Maven Central · microsphere-redis-spring](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-redis-spring)

<ProjectNav></ProjectNav>
