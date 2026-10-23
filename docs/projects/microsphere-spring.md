---
title: Microsphere Spring
description: "Solves real production pain points in a modular way: enhancing dependency injection, configuration management, web endpoint handling, events, caching and JDBC monitoring. It is a pure additive enhancement — a drop-in dependency for any existing Spring application."
outline: deep
project:
  slug: microsphere-spring
  layer: framework
---

<ProjectHeader></ProjectHeader>

## Overview

Solves real production pain points in a modular way: enhancing dependency injection, configuration management, web endpoint handling, events, caching and JDBC monitoring. It is a pure additive enhancement — a drop-in dependency for any existing Spring application.

## Key Features

- **Parallel bean instantiation** — Resolves the bean dependency graph and initialises independent singletons concurrently to cut startup time.
- **Listenable Environment** — Intercepts property resolution and profile activation via EnvironmentListener and PropertyResolverListener.
- **Enhanced @PropertySource** — @ResourcePropertySource adds wildcard patterns, ordering, inheritance and auto-refresh on change, plus @YamlPropertySource and @JsonPropertySource.
- **TTL caching** — @EnableTTLCaching / @TTLCacheable add per-entry time-to-live to Spring Cache, including Redis.
- **Web endpoint registry** — Collects WebEndpointMapping metadata from Spring MVC, WebFlux and classic Servlet at startup for introspection and routing.
- **Handler method interception** — HandlerMethodInterceptor / HandlerMethodArgumentInterceptor provide AOP-style hooks around MVC and WebFlux controller invocations.
- **P6Spy JDBC monitoring** — @EnableP6DataSource transparently wraps existing DataSource beans for SQL tracing.
- **Google Guice integration** — @EnableGuice bridges Guice @Inject injection points into the Spring bean lifecycle.
- **Rich testing utilities** — EmbeddedTomcatContextLoader, @EnableEmbeddedDatabase, AbstractWebFluxTest and servlet/MVC test helpers.

## Usage Example

```java
@Configuration
@ResourcePropertySource(
        name = "app-config",
        value = "classpath*:/META-INF/config/*.properties",
        autoRefreshed = true)      // reload whenever any matched file changes
public class AppConfig { }

@Configuration
@EnableTTLCaching
public class CachingConfig { }

@TTLCacheable(cacheNames = "products", ttl = 300, timeUnit = TimeUnit.SECONDS)
public Product findById(Long id) { ... }

@Configuration
@EnableWebMvcExtension(interceptHandlerMethods = true, registerWebEndpointMappings = true)
public class WebConfig { }

@Configuration
@EnableP6DataSource          // wraps every DataSource transparently — zero code changes
public class DataSourceConfig { }
```

## Modules

| Module | |
|------|------|
| `microsphere-spring-context` | Core context and configuration extensions: @ResourcePropertySource, @EnableTTLCaching, @EnableConfigurationBeanBinding |
| `microsphere-spring-web` | Shared web abstractions: WebEndpointMapping, HandlerMethodInterceptor, @EnableWebExtension, @Idempotent |
| `microsphere-spring-webmvc` | Spring MVC extensions: @EnableWebMvcExtension, ReversedProxyHandlerMapping |
| `microsphere-spring-webflux` | Reactive web extensions: @EnableWebFluxExtension, InterceptingHandlerMethodProcessor |
| `microsphere-spring-jdbc` | JDBC / P6Spy integration: @EnableP6DataSource |
| `microsphere-spring-guice` | Google Guice bridge: @EnableGuice |
| `microsphere-spring-test` | Testing utilities: @EnableEmbeddedDatabase, EmbeddedTomcatContextLoader |

## Getting Started

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-spring-dependencies</artifactId>
            <version>${microsphere-spring.version}</version>
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
        <artifactId>microsphere-spring-context</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| Java | 17+ |
| Spring Framework | 6.0.x – 7.0.x (main) / 4.3.x – 5.3.x (1.x) |
| Maven | 3.6+ |

### Version Lines

| Branch | | |
|------|----------|----------|
| `main` | 6.0.x – 7.0.x | `0.2.39` |
| `1.x` | 4.3.x – 5.3.x | `0.1.39` |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-spring)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-spring/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-spring)
- [Maven Central · microsphere-spring-context](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-spring-context)

<ProjectNav></ProjectNav>
