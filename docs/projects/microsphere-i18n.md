---
title: Microsphere i18n
description: "A comprehensive i18n framework for Java applications with deep Spring integration. Its modular, extensible architecture manages localised messages across deployment scenarios ranging from standalone Spring applications to distributed, cloud-native microservices."
outline: deep
project:
  slug: microsphere-i18n
  layer: crosscutting
---

<ProjectHeader></ProjectHeader>

## Overview

A comprehensive i18n framework for Java applications with deep Spring integration. Its modular, extensible architecture manages localised messages across deployment scenarios ranging from standalone Spring applications to distributed, cloud-native microservices.

## Key Features

- **Layered message sources** — Load localised messages from classpath properties files, the Spring Environment or external configuration systems through a unified ServiceMessageSource abstraction.
- **Composite sources with priority** — CompositeServiceMessageSource combines multiple sources; higher-priority sources shadow lower-priority ones.
- **Dynamic configuration** — Spring Cloud integration enables runtime message updates without restarting the application.
- **Spring MessageSource bridge** — The primary ServiceMessageSource bean is exposed as Spring's MessageSource, working transparently with @Value, Thymeleaf and more.
- **Bean Validation integration** — An i18n-aware LocalValidatorFactoryBean translates constraint violation messages through the same source.
- **OpenFeign propagation** — An Accept-Language request interceptor forwards the current locale to downstream Feign clients.
- **Actuator endpoint** — Read and write i18n messages at runtime through /actuator/i18n.
- **Centralised i18n server** — A dedicated Spring Cloud server module serves consolidated message bundles across microservices.

## Modules

| Module | |
|------|------|
| `microsphere-i18n-core` | Fundamental i18n abstractions and message source implementations |
| `microsphere-i18n-spring` | Integration with Spring's MessageSource and Environment |
| `microsphere-i18n-spring-boot` | Auto-configuration and Actuator endpoint |
| `microsphere-i18n-spring-cloud` | Dynamic configuration updates via Spring Cloud Config |
| `microsphere-i18n-spring-cloud-server` | Centralised i18n management server |
| `microsphere-i18n-openfeign` | Propagates the current locale to OpenFeign clients |
| `microsphere-i18n-dependencies` | BOM |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-i18n-dependencies</artifactId>
            <version>${microsphere-i18n.version}</version>
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
        <artifactId>microsphere-i18n-core</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| Java | 17+ |
| Spring Framework | 6.x |
| Spring Boot | 3.x |
| Spring Cloud | 2022.0.x – 2025.0.x |

### Version Lines

| Branch | | |
|------|----------|----------|
| `main` | 2022.0.x – 2025.0.x | `0.2.21` |
| `1.x` | Hoxton – 2021.0.x | `0.1.21` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-i18n)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-i18n/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-i18n)
- [Maven Central · microsphere-i18n-core](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-i18n-core)

<ProjectNav></ProjectNav>
