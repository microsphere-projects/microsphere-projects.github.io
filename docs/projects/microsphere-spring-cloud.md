---
title: Microsphere Spring Cloud
description: "A production-ready extension library for Spring Cloud that targets common operational pain points in distributed systems — above all, applying runtime configuration changes without restarting the application."
outline: deep
project:
  slug: microsphere-spring-cloud
  layer: framework
---

<ProjectHeader></ProjectHeader>

## Overview

A production-ready extension library for Spring Cloud that targets common operational pain points in distributed systems — above all, applying runtime configuration changes without restarting the application.

## Key Features

- **OpenFeign auto-refresh** — Dynamically refreshes Feign client components (encoder, decoder, retryer, request interceptors) in response to EnvironmentChangeEvent — no restart required.
- **Multiple service registries** — Registers a single service instance with several registries at once (Nacos, Eureka, Consul, Zookeeper) through one unified API.
- **Service registration events** — Rich lifecycle events published via AOP — RegistrationPreRegisteredEvent, RegistrationRegisteredEvent, RegistrationPreDeregisteredEvent and RegistrationDeregisteredEvent.
- **Union discovery client** — Aggregates service instances from multiple discovery backends behind a single DiscoveryClient interface.
- **Fault tolerance utilities** — Weighted round-robin load balancing and Tomcat dynamic configuration support for improved resilience.
- **Actuator endpoints** — Built-in /service-registration and /service-deregistration endpoints for operational control at runtime.
- **Multi-version support** — The main branch targets Spring Cloud 2022.x – 2025.x; the 1.x branch covers Hoxton – 2021.0.x.

## Usage Example

```java
@SpringBootApplication
@EnableFeignClients
@EnableFeignAutoRefresh     // refresh Feign components when configuration changes
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

## Modules

| Module | |
|------|------|
| `microsphere-spring-cloud-commons` | Common utilities for service discovery, registration and fault tolerance |
| `microsphere-spring-cloud-openfeign` | OpenFeign extensions with auto-refresh support |
| `microsphere-spring-cloud-dependencies` | BOM centralising dependency management |
| `microsphere-spring-cloud-parent` | Parent POM with Spring Cloud version profiles |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-spring-cloud-dependencies</artifactId>
            <version>${microsphere-spring-cloud.version}</version>
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
        <artifactId>microsphere-spring-cloud-commons</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| Java | 17+ |
| Spring Boot | 3.0+ (main) / 2.x (1.x) |
| Spring Cloud | 2022.0.x – 2025.0.x |
| Maven | 3.6+ |

### Version Lines

| Branch | | |
|------|----------|----------|
| `main` | 2022.0.x – 2025.0.x | `0.2.26` |
| `1.x` | Hoxton – 2021.0.x | `0.1.26` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-spring-cloud)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-spring-cloud/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-spring-cloud)
- [Maven Central · microsphere-spring-cloud-commons](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-spring-cloud-commons)

<ProjectNav></ProjectNav>
