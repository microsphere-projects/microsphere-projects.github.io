---
title: Microsphere Gateway
description: "Extends the Spring Cloud Gateway ecosystem with Microsphere-specific routing, discovery and refresh behaviour. A custom we:// route scheme exposes the web endpoints of discovered services behind a single gateway, so you never duplicate route definitions in every service."
outline: deep
project:
  slug: microsphere-gateway
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

Extends the Spring Cloud Gateway ecosystem with Microsphere-specific routing, discovery and refresh behaviour. A custom we:// route scheme exposes the web endpoints of discovered services behind a single gateway, so you never duplicate route definitions in every service.

## Key Features

- **Both gateway stacks** — Dedicated modules for Spring Cloud Gateway WebFlux and Gateway Server MVC.
- **we:// dynamic routing** — Routes discovered web endpoints dynamically through a custom we:// scheme backed by Spring Cloud discovery.
- **Self-refreshing routes** — Keeps routes current when gateway configuration, route definitions or service instances change.
- **Fine-grained exposure rules** — metadata.web-endpoint.excludes filters by path, method, header, param, consumes and produces.
- **Unified BOM and commons** — A shared BOM and commons module keep every gateway module consistent.

## Usage Example

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: web-endpoint-mapping
          uri: we://all            # subscribe to every discovered service
          predicates:
            - Path=/{application}/**
          metadata:
            web-endpoint:
              excludes:
                - patterns: /internal/**
                  methods: GET
```

## Modules

| Module | |
|------|------|
| `microsphere-spring-cloud-gateway-commons` | Shared constants, annotations and configuration binding |
| `microsphere-spring-cloud-gateway-server-webflux` | Reactive gateway integration |
| `microsphere-spring-cloud-gateway-server-webmvc` | Servlet-based integration for Spring Cloud Gateway Server MVC |
| `microsphere-gateway-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-gateway-dependencies</artifactId>
            <version>${microsphere-gateway.version}</version>
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
        <artifactId>microsphere-spring-cloud-gateway-server-webflux</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| JDK | 17+ |
| Maven | 3.9+ |
| Spring Cloud | 2022 / 2023 / 2024 / 2025 |

::: tip Note
Target services must publish Microsphere web endpoint metadata so the gateway can discover request mappings and rewrite incoming paths correctly.
:::

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-gateway)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-gateway/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-gateway)
- [Maven Central · microsphere-spring-cloud-gateway-server-webflux](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-spring-cloud-gateway-server-webflux)

<ProjectNav></ProjectNav>
