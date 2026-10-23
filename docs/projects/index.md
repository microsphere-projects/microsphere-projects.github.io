---
title: All Projects
description: "The complete Microsphere catalogue — layered, searchable, and sortable"
outline: false
---

<ProjectsIndex></ProjectsIndex>

## How the layers work

### L0 · Foundation

Unified build and dependency governance. The Maven parent POM and BOM that keep all 36 repositories on one baseline.

### L1 · Runtime

Framework-free Java capabilities: strings and collections, reflection, type conversion, events, logging abstraction, plus Java / Jakarta EE implementations.

### L2 · Framework

Enhancements for Spring, Spring Boot and Spring Cloud — the most central layer of the ecosystem.

### L3 · Integration

Adapters for concrete infrastructure: service registries, data access, caching, RPC, resilience and gateways.

### L4 · Cross-cutting

Capabilities that cut across every layer: observability, internationalisation, security, dynamic configuration and multi-active routing.

::: tip
Layers follow dependency order: L1 depends on no framework, L2 extends the Spring stack on top of L1, L3 adapts concrete infrastructure, and L4 is a pluggable cross-cutting capability. Any combination is valid.
:::

## Capability Matrix

| Project | Layer | Lang | Stars | Forks | In one line |
|--------|------|------|------|------|--------|
| [Microsphere Build](./microsphere-build) | L0 · Foundation | Maven | 8 | 29 | The shared Maven parent POM for the whole ecosystem |
| [Microsphere BOM](./microsphere-bom) | L0 · Foundation | Maven | 0 | 1 | A cross-project Maven bill of materials |
| [Microsphere Java](./microsphere-java) | L1 · Runtime | Java | 104 | 52 | The foundation of the ecosystem: reusable Java components and utilities |
| [Microsphere Java EE](./microsphere-java-enterprise) | L1 · Runtime | Java | 14 | 18 | Microsphere's implementation of the Java EE specifications |
| [Microsphere Jakarta](./microsphere-jakarta) | L1 · Runtime | Java | 2 | 6 | Microsphere's implementation of the Jakarta EE specifications |
| [Microsphere Logging](./microsphere-logging) | L1 · Runtime | Java | 2 | 1 | One abstraction layer for runtime logging management |
| [Microsphere MicroProfile](./microsphere-microprofile) | L1 · Runtime | Java | 1 | 6 | Eclipse MicroProfile support |
| [Microsphere Test](./microsphere-test) | L1 · Runtime | Java | 0 | 0 | Cross-project testing infrastructure |
| [Microsphere Tools](./microsphere-tools) | L1 · Runtime | Java | 0 | 5 | Shared development tooling |
| [Microsphere Spring](./microsphere-spring) | L2 · Framework | Java | 61 | 39 | Production-grade extensions for the Spring Framework |
| [Microsphere Spring Cloud](./microsphere-spring-cloud) | L2 · Framework | Java | 33 | 30 | Dynamic runtime configuration without restarts |
| [Microsphere Spring Boot](./microsphere-spring-boot) | L2 · Framework | Java | 24 | 22 | Configuration governance, diagnostics and enhanced monitoring |
| [Microsphere Gateway](./microsphere-gateway) | L3 · Integration | Java | 5 | 5 | Discovery-driven dynamic routing for web endpoints |
| [Microsphere Dubbo](./microsphere-dubbo) | L3 · Integration | Java | 4 | 7 | Apache Dubbo integration |
| [Microsphere Redis](./microsphere-redis) | L3 · Integration | Java | 3 | 11 | An enhanced Spring Data Redis integration framework |
| [Microsphere Alibaba Druid](./microsphere-alibaba-druid) | L3 · Integration | Java | 2 | 3 | SQL interception for the Druid connection pool |
| [Microsphere Alibaba Sentinel](./microsphere-alibaba-sentinel) | L3 · Integration | Java | 2 | 11 | Flow control injected transparently into data, cache and web layers |
| [Microsphere Nacos](./microsphere-nacos) | L3 · Integration | Java | 2 | 6 | Alibaba Nacos integration |
| [Microsphere Netflix](./microsphere-netflix) | L3 · Integration | Java | 2 | 8 | Highly available Eureka clusters and an enhanced client |
| [Microsphere Resilience4j](./microsphere-resilience4j) | L3 · Integration | Java | 2 | 9 | A unified way to apply resilience patterns |
| [Microsphere Tomcat](./microsphere-tomcat) | L3 · Integration | Java | 2 | 6 | Apache Tomcat integration |
| [Microsphere MyBatis](./microsphere-mybatis) | L3 · Integration | Java | 1 | 3 | A lightweight SQL interception framework |
| [Microsphere etcd](./microsphere-etcd) | L3 · Integration | Java | 0 | 7 | etcd integration |
| [Microsphere Hibernate](./microsphere-hibernate) | L3 · Integration | Java | 0 | 1 | Extensions for Hibernate ORM |
| [Microsphere i18n](./microsphere-i18n) | L4 · Cross-cutting | Java | 13 | 18 | A layered internationalisation framework for microservices |
| [Microsphere DevOps](./microsphere-devops) | L4 · Cross-cutting | Shell | 5 | 6 | Engineering efficiency and operations support |
| [Microsphere Multiactive](./microsphere-multiactive) | L4 · Cross-cutting | Java | 4 | 14 | Zone-aware routing for multi-active deployments |
| [Microsphere Observability](./microsphere-observability) | L4 · Cross-cutting | Java | 4 | 8 | Monitoring, metrics and logging in one suite |
| [Microsphere Dynamic](./microsphere-dynamic) | L4 · Cross-cutting | Java | 3 | 7 | Infrastructure for runtime dynamism |
| [Microsphere Security](./microsphere-security) | L4 · Cross-cutting | Java | 3 | 6 | Security capability extensions |
| [Microsphere Configuration](./microsphere-configuration) | L4 · Cross-cutting | Java | 2 | 10 | Configuration system enhancements |
| [Microsphere AI](./microsphere-ai) | L4 · Cross-cutting | Java | 0 | 1 | An exploratory project for AI scenarios |

