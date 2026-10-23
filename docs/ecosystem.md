---
title: Ecosystem
description: How Microsphere Projects connects to the external technology stack
outline: [2, 3]
---

# Ecosystem

Microsphere is not a closed framework. Almost every project **enhances an existing technology** rather than replacing
it. This page lists the integration points.

## Technologies we integrate with

| Domain | External technology | Project |
|--------|---------------------|---------|
| **Core frameworks** | Spring Framework 4.3 – 7.0 | [microsphere-spring](/projects/microsphere-spring) |
| | Spring Boot 2.0 – 4.1 | [microsphere-spring-boot](/projects/microsphere-spring-boot) |
| | Spring Cloud Hoxton – 2025.x | [microsphere-spring-cloud](/projects/microsphere-spring-cloud) |
| **Registry & discovery** | Alibaba Nacos | [microsphere-nacos](/projects/microsphere-nacos) |
| | Netflix Eureka | [microsphere-netflix](/projects/microsphere-netflix) |
| | Consul / Zookeeper | [microsphere-spring-cloud](/projects/microsphere-spring-cloud) |
| | etcd | [microsphere-etcd](/projects/microsphere-etcd) |
| **RPC & gateway** | Apache Dubbo | [microsphere-dubbo](/projects/microsphere-dubbo) |
| | Spring Cloud Gateway (WebFlux / MVC) | [microsphere-gateway](/projects/microsphere-gateway) |
| | OpenFeign | [microsphere-spring-cloud](/projects/microsphere-spring-cloud) |
| **Data access** | MyBatis | [microsphere-mybatis](/projects/microsphere-mybatis) |
| | Hibernate ORM 5.0 – 7.3 | [microsphere-hibernate](/projects/microsphere-hibernate) |
| | Alibaba Druid | [microsphere-alibaba-druid](/projects/microsphere-alibaba-druid) |
| | P6Spy | [microsphere-spring](/projects/microsphere-spring) |
| **Caching** | Spring Data Redis 2.1 – 3.5 | [microsphere-redis](/projects/microsphere-redis) |
| | Apache Kafka (Redis replication) | [microsphere-redis](/projects/microsphere-redis) |
| **Resilience** | Alibaba Sentinel | [microsphere-alibaba-sentinel](/projects/microsphere-alibaba-sentinel) |
| | Resilience4j 1.3 – 2.4 | [microsphere-resilience4j](/projects/microsphere-resilience4j) |
| **Observability** | Micrometer | [microsphere-observability](/projects/microsphere-observability) |
| | Prometheus | [microsphere-observability](/projects/microsphere-observability) |
| | OpenTelemetry Instrumentation BOM | [microsphere-observability](/projects/microsphere-observability) |
| **Logging** | JUL / Log4j / Log4j2 / Logback / SLF4J | [microsphere-logging](/projects/microsphere-logging) |
| **Web container** | Apache Tomcat | [microsphere-tomcat](/projects/microsphere-tomcat) |
| **Enterprise specs** | Java EE / Jakarta EE / MicroProfile | [EE](/projects/microsphere-java-enterprise) · [Jakarta](/projects/microsphere-jakarta) · [MicroProfile](/projects/microsphere-microprofile) |
| **Dependency injection** | Google Guice | [microsphere-spring](/projects/microsphere-spring) |
| **Cloud platforms** | AWS (availability zone discovery) | [microsphere-multiactive](/projects/microsphere-multiactive) |

## How we differ from other enhancement libraries

Microsphere is positioned as an **additive enhancement, never a replacement**. Three defining traits:

1. **Zero intrusion** — most capabilities weave in through interception pipelines, auto-configuration and events.
   A single `@EnableP6DataSource` annotation wraps every DataSource bean for SQL tracing.
2. **Trimmable** — each Maven module can be adopted independently, with no forced transitive baggage.
3. **Long-lifecycle compatibility** — a compatibility shim keeps one codebase working across Spring Boot 2.x to 4.x,
   so upgrades never require a fork.

## Publishing

- All artifacts are published to **Maven Central** under the Group ID `io.github.microsphere-projects`
- Since `microsphere-build` 0.2.0, publishing goes through the Central Publisher Portal
  (OSSRH reached end of life on 2025-06-30)
- Every repository runs Maven Build and Codecov workflows

## Documentation

Each sub-project ships bilingual documentation (English by default, Chinese under `zh/`), organised per release branch:

| Resource | Location |
|----------|----------|
| In-repo user guide | `docs/user-guide/` · `docs/developer-guide/` |
| AI-assisted Q&A | The corresponding DeepWiki and Zread spaces |
| JavaDoc | javadoc.io (published per module) |
| Wiki | Each repository's GitHub Wiki |
