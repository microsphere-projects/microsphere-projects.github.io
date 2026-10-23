---
title: Compatibility Matrix
description: Supported ranges for the main and 1.x release lines
outline: [2, 3]
---

# Compatibility Matrix

Microsphere maintains **two release lines**: `main` targets the current framework generation, `1.x` serves existing
systems. Both offer the same feature set but compile against different baselines.

::: warning Do not mix lines
Never include both `0.2.x` and `0.1.x` modules in one application — it causes classpath conflicts and unpredictable
auto-configuration behaviour.
:::

## Core frameworks

| Sub-project | `main` (0.2.x) | `1.x` (0.1.x) |
|-------------|----------------|---------------|
| [microsphere-java](/projects/microsphere-java) | Java 8 – 25 | — |
| [microsphere-spring](/projects/microsphere-spring) | Spring Framework 6.0.x – 7.0.x · `0.2.39` | Spring Framework 4.3.x – 5.3.x · `0.1.39` |
| [microsphere-spring-boot](/projects/microsphere-spring-boot) | Spring Boot 3.0.x – 4.1.x · `0.2.34` | Spring Boot 2.0.x – 2.7.x · `0.1.34` |
| [microsphere-spring-cloud](/projects/microsphere-spring-cloud) | Spring Cloud 2022.0.x – 2025.0.x · `0.2.26` | Hoxton – 2021.0.x · `0.1.26` |

## Ecosystem integrations

| Sub-project | `main` | `1.x` |
|-------------|--------|-------|
| [microsphere-gateway](/projects/microsphere-gateway) | Spring Cloud 2022 / 2023 / 2024 / 2025 | Hoxton – 2021.0.x |
| [microsphere-redis](/projects/microsphere-redis) | Spring Data Redis 3.0.0 – 3.5.x · `0.2.14` | Spring Data Redis 2.1.0 – 2.7.x · `0.1.14` |
| [microsphere-mybatis](/projects/microsphere-mybatis) | `0.2.16` | `0.1.16` |
| [microsphere-hibernate](/projects/microsphere-hibernate) | Hibernate Core 6.2.x – 7.3.x · `0.2.10` | Hibernate Core 5.0.x – 5.6.x · `0.1.10` |
| [microsphere-alibaba-druid](/projects/microsphere-alibaba-druid) | `0.2.21` | `0.1.21` |
| [microsphere-alibaba-sentinel](/projects/microsphere-alibaba-sentinel) | `0.2.5` | `0.1.5` |
| [microsphere-resilience4j](/projects/microsphere-resilience4j) | Resilience4j 2.0.0 – 2.4.0 · `0.2.4` | Resilience4j 1.3.0 – 1.7.0 · `0.1.4` |
| [microsphere-netflix](/projects/microsphere-netflix) | `0.2.0` | `0.1.0` |
| [microsphere-nacos](/projects/microsphere-nacos) | `0.2.0` | `0.1.0` |
| [microsphere-multiactive](/projects/microsphere-multiactive) | `0.2.13` | `0.1.13` |
| [microsphere-observability](/projects/microsphere-observability) | `0.2.3` | `0.1.3` |
| [microsphere-i18n](/projects/microsphere-i18n) | `0.2.21` | `0.1.21` |

## JDK support

The `microsphere-build` parent POM covers **Java 8 / 11 / 17 / 21 / 25**, but individual sub-projects have their own
baselines:

| Baseline | Projects |
|----------|----------|
| Java 8+ | `microsphere-java`, `microsphere-logging`, `microsphere-java-enterprise`, `microsphere-test`, `microsphere-tools` |
| Java 17+ | `microsphere-spring`, `microsphere-spring-boot`, `microsphere-spring-cloud`, `microsphere-i18n`, `microsphere-gateway`, `microsphere-hibernate` (0.2.x), `microsphere-multiactive` |

CI verifies the full matrix on Java 17, 21 and 25 against the Spring Cloud 2022 / 2023 / 2024 / 2025 profiles.

## Switching Spring Cloud versions

The `main` branch builds against Spring Cloud 2025.0.x by default. To build or test against an older generation,
activate the corresponding Maven profile:

```bash
./mvnw verify -P spring-cloud-2022
./mvnw verify -P spring-cloud-2023
./mvnw verify -P spring-cloud-2024
```
