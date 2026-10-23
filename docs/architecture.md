---
title: Architecture
description: The five-layer architecture of Microsphere Projects, dependency flow, cross-cutting capability map and a typical request path
outline: [2, 3]
---

# Architecture

This page consolidates the capabilities of all **32 sub-projects** into a single picture. The whole architecture
follows one rule: **each layer depends only on the layers below it, while cross-cutting capabilities plug into every
layer.**

<ArchitectureMap />

## Dependency flow

Dependencies point strictly downward — no layer ever depends on a layer above it:

```
L4 Cross-cutting   observability · i18n · security · dynamic · multiactive · configuration
                        ↓ weave in (pluggable, no compile-time dependency)
L3 Integration     gateway · nacos · redis · mybatis · hibernate · druid
                   sentinel · resilience4j · netflix · dubbo · tomcat · etcd
                        ↓ depends on
L2 Framework       microsphere-spring · microsphere-spring-boot · microsphere-spring-cloud
                        ↓ depends on
L1 Runtime         microsphere-java · logging · java-enterprise · jakarta · microprofile
                        ↓ depends on
L0 Foundation      microsphere-build (parent POM) · microsphere-bom (version governance)
```

This chain delivers three concrete benefits:

1. **Trimmable** — using `microsphere-java` alone pulls in no Spring dependency whatsoever.
2. **Consistent versions** — every layer shares L0's build baseline and version governance, so repositories never drift.
3. **Non-intrusive cross-cutting capabilities** — L4 weaves in through interception pipelines and events, so
   observability and resilience arrive without touching business code.

## Layer responsibilities

| Layer | Responsibility | Key constraint |
|-------|----------------|----------------|
| **L0 Foundation** | Maven parent POM, plugin versions, profiles and BOM governance | Covers five Java TLS versions: 8 / 11 / 17 / 21 / 25 |
| **L1 Runtime** | Framework-free Java capabilities: utilities, reflection, type conversion, events, logging abstraction | Must not depend on Spring or any application framework |
| **L2 Framework** | Enhancements for Spring, Spring Boot and Spring Cloud | Must stay a drop-in additive enhancement that never changes default behaviour |
| **L3 Integration** | Adapters for concrete infrastructure: registries, data access, caching, RPC, resilience | Hooks in via interception and extension points, never touching business code |
| **L4 Cross-cutting** | Observability, i18n, security, dynamic configuration, multi-active routing | Woven in via SPI and events, individually switchable |

## Cross-cutting capability map

Regrouping sub-project features by **capability domain** shows how one theme is distributed across the ecosystem:

### Configuration dynamism

| Project | Contribution |
|---------|--------------|
| [Spring](/projects/microsphere-spring) | `@ResourcePropertySource` with wildcards, inheritance and `autoRefreshed`; `@YamlPropertySource` / `@JsonPropertySource` |
| [Spring Cloud](/projects/microsphere-spring-cloud) | Responds to `EnvironmentChangeEvent` by refreshing OpenFeign encoders, decoders, retryers and interceptors |
| [Spring Boot](/projects/microsphere-spring-boot) | `BindListener` fires when `@ConfigurationProperties` values change; `microsphere.autoconfigure.exclude` uses merge semantics |
| [i18n](/projects/microsphere-i18n) | Runtime message updates driven by Spring Cloud config; `/actuator/i18n` reads and writes live |
| [Dynamic](/projects/microsphere-dynamic) | Infrastructure for runtime dynamic changes |

### Observability

| Project | Contribution |
|---------|--------------|
| [Observability](/projects/microsphere-observability) | Micrometer `MeterBinder`s (Sentinel / P6Spy / system), Prometheus collectors, CGroups and network metrics |
| [Spring](/projects/microsphere-spring) | `@EnableP6DataSource` wraps DataSources transparently for SQL tracing |
| [Druid](/projects/microsphere-alibaba-druid) | SQL statement interception and logging as the collection entry point |
| [MyBatis](/projects/microsphere-mybatis) | SQL interception pipeline emitting logs, metrics and trace data |
| [Spring Boot](/projects/microsphere-spring-boot) | Four extra Actuator endpoints expose classpath artifacts, web endpoint mappings, config metadata and bound properties |

### Resilience and flow control

| Project | Contribution |
|---------|--------------|
| [Sentinel](/projects/microsphere-alibaba-sentinel) | Flow control, circuit breaking and system protection across WebMVC, WebFlux, Druid, Hibernate, MyBatis, P6Spy and Redis |
| [Resilience4j](/projects/microsphere-resilience4j) | Circuit breaker, bulkhead, rate limiter, retry and time limiter across Web MVC, Feign, MyBatis and JDBC |
| [Spring Cloud](/projects/microsphere-spring-cloud) | Weighted round-robin load balancing and Tomcat dynamic configuration |
| [Multiactive](/projects/microsphere-multiactive) | Same-zone preference with cross-zone fallback to isolate failure domains |

### Service governance

| Project | Contribution |
|---------|--------------|
| [Spring Cloud](/projects/microsphere-spring-cloud) | Multi-registry registration (Nacos / Eureka / Consul / Zookeeper), registration lifecycle events, union discovery client |
| [Gateway](/projects/microsphere-gateway) | The `we://` scheme routes discovered web endpoints dynamically, filterable by path, method, header and param |
| [Netflix](/projects/microsphere-netflix) | Enhanced Eureka client metadata sync and a Tomcat-clustered highly available server |
| [Nacos](/projects/microsphere-nacos) | Alibaba Nacos integration |

### Data access

| Project | Contribution |
|---------|--------------|
| [MyBatis](/projects/microsphere-mybatis) | SQL interception pipeline supporting security, throttling and caching concerns |
| [Hibernate](/projects/microsphere-hibernate) | ORM extensions covering Hibernate 6.2–7.3 and 5.0–5.6 |
| [Druid](/projects/microsphere-alibaba-druid) | Connection-pool-level SQL interception and logging |
| [Redis](/projects/microsphere-redis) | Non-intrusive Redis command interception, events and metrics, Kafka-backed replication |
| [Spring](/projects/microsphere-spring) | `@EnableTTLCaching` / `@TTLCacheable` for per-entry TTL caching |
| [ETCD](/projects/microsphere-etcd) | etcd key-value store integration |

### Internationalisation and security

| Project | Contribution |
|---------|--------------|
| [i18n](/projects/microsphere-i18n) | Layered message sources, priority composition, `MessageSource` bridge, Bean Validation translation, OpenFeign `Accept-Language` propagation, centralised i18n server |
| [Security](/projects/microsphere-security) | Security capability extensions |
| [Spring](/projects/microsphere-spring) | `@Idempotent`, plus `HandlerMethodInterceptor` hooks |

### Engineering governance

| Project | Contribution |
|---------|--------------|
| [Build](/projects/microsphere-build) | Unified parent POM: multi-TLS versions, locked plugins, six profiles, Central Portal publishing |
| [BOM](/projects/microsphere-bom) | Cross-project version alignment |
| [Logging](/projects/microsphere-logging) | One abstraction over JUL / Log4j / Log4j2 / Logback with runtime level changes and JMX |
| [DevOps](/projects/microsphere-devops) | Engineering efficiency and operations support, including a TypeScript UI |

## A typical request path

Here is a full cross-service request with Gateway, Spring Cloud and Observability enabled:

<ClientOnly>
<div class="flow">
  <svg viewBox="0 0 900 250" role="img" aria-label="A typical Microsphere request path">
    <defs>
      <marker id="fh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M0 0L10 5L0 10z" fill="currentColor" />
      </marker>
    </defs>

    <g font-family="ui-sans-serif, system-ui, sans-serif" font-size="12.5" fill="currentColor">
      <!-- row 1 -->
      <rect x="10" y="18" width="150" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:var(--vp-c-divider)"/>
      <text x="85" y="39" text-anchor="middle" font-weight="700">Client request</text>
      <text x="85" y="55" text-anchor="middle" font-size="11" opacity=".65">HTTP</text>

      <rect x="196" y="18" width="164" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#10b981"/>
      <text x="278" y="39" text-anchor="middle" font-weight="700">microsphere-gateway</text>
      <text x="278" y="55" text-anchor="middle" font-size="11" opacity=".65">we:// routing + endpoint filters</text>

      <rect x="396" y="18" width="164" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#7c5cf0"/>
      <text x="478" y="39" text-anchor="middle" font-weight="700">Service discovery</text>
      <text x="478" y="55" text-anchor="middle" font-size="11" opacity=".65">multi-registry · same-zone first</text>

      <rect x="596" y="18" width="164" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#7c5cf0"/>
      <text x="678" y="39" text-anchor="middle" font-weight="700">Target instance</text>
      <text x="678" y="55" text-anchor="middle" font-size="11" opacity=".65">MVC / WebFlux controller</text>

      <rect x="796" y="18" width="94" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:var(--vp-c-divider)"/>
      <text x="843" y="39" text-anchor="middle" font-weight="700">Response</text>
      <text x="843" y="55" text-anchor="middle" font-size="11" opacity=".65">i18n localised</text>

      <!-- arrows row 1 -->
      <g stroke="currentColor" fill="none" stroke-width="1.6" marker-end="url(#fh)" opacity=".8">
        <path d="M162 41h28" /><path d="M362 41h28" /><path d="M562 41h28" /><path d="M762 41h28" />
      </g>

      <path d="M678 66v34" stroke="currentColor" fill="none" stroke-width="1.6" stroke-dasharray="4 4" opacity=".5"/>

      <!-- row 2 -->
      <rect x="396" y="104" width="364" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#f59e0b"/>
      <text x="578" y="125" text-anchor="middle" font-weight="700">OpenFeign client (auto-refresh)</text>
      <text x="578" y="141" text-anchor="middle" font-size="11" opacity=".65">hot refresh on EnvironmentChangeEvent · Accept-Language</text>

      <rect x="10" y="104" width="164" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:var(--vp-c-divider)"/>
      <text x="92" y="125" text-anchor="middle" font-weight="700">Interception pipeline</text>
      <text x="92" y="141" text-anchor="middle" font-size="11" opacity=".65">Handler / SQL / Redis</text>

      <rect x="210" y="104" width="150" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#f43f5e"/>
      <text x="285" y="125" text-anchor="middle" font-weight="700">Flow control</text>
      <text x="285" y="141" text-anchor="middle" font-size="11" opacity=".65">Sentinel · Resilience4j</text>

      <g stroke="currentColor" fill="none" stroke-width="1.6" marker-end="url(#fh)" opacity=".8">
        <path d="M176 127h28" /><path d="M362 127h28" />
      </g>

      <!-- row 3 -->
      <rect x="396" y="186" width="364" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#0ea5e9"/>
      <text x="578" y="207" text-anchor="middle" font-weight="700">Micrometer / Prometheus export</text>
      <text x="578" y="223" text-anchor="middle" font-size="11" opacity=".65">SQL, Redis, Feign, CGroups, network stats</text>

      <rect x="10" y="186" width="364" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:var(--vp-c-divider)"/>
      <text x="192" y="207" text-anchor="middle" font-weight="700">Logging abstraction (JUL / Log4j2 / Logback)</text>
      <text x="192" y="223" text-anchor="middle" font-size="11" opacity=".65">runtime level changes · JMX control</text>

      <path d="M578 152v30" stroke="currentColor" fill="none" stroke-width="1.6" stroke-dasharray="4 4" opacity=".5"/>
      <path d="M192 186v-6" stroke="currentColor" fill="none" stroke-width="1.6" opacity=".3"/>
    </g>
  </svg>
</div>
</ClientOnly>

Every hop on this path is independently switchable: skip the gateway and use Spring Cloud alone, skip Sentinel if
you don't need flow control, and let Micrometer auto-configure observability — all without changing business code.

## Choosing your starting point

::: tip Start small
Don't pull in everything at once. The recommended path is:

1. Start with `microsphere-java-dependencies` and use the utility library;
2. Add `microsphere-spring-dependencies` once you have a Spring app to fix configuration and startup problems;
3. Move to `microsphere-spring-cloud-dependencies` when you go distributed;
4. Finally adopt L3 / L4 by pain point — observability, flow control and i18n as needed.
:::

::: warning Don't mix release lines
`main` (0.2.x) and `1.x` (0.1.x) target different Spring generations. **Never mix modules from both lines in one
application.** See the [compatibility matrix](/guide/compatibility).
:::
