---
title: Dependencies & BOMs
description: BOM coordinates and recommended entry modules for every sub-project
outline: [2, 3]
---

# Dependencies & BOMs

Every artifact uses the Group ID `io.github.microsphere-projects` and is published to Maven Central.

## Why each project has its own BOM

Microsphere uses **per-sub-project BOMs** rather than one giant BOM. Each sub-project targets a different Spring
generation and they do not share a release cadence — `microsphere-spring` may be at `0.2.39` while `microsphere-i18n`
sits at `0.2.21`. Managing them separately lets each BOM evolve independently, and you import only what you need.

If you want to align several sub-projects at once, import multiple BOMs; Maven resolves them in declaration order.

## BOM coordinates

| Sub-project | BOM artifact | Recommended entry module |
|-------------|--------------|--------------------------|
| [microsphere-java](/projects/microsphere-java) | `microsphere-java-dependencies` | `microsphere-java-core` |
| [microsphere-spring](/projects/microsphere-spring) | `microsphere-spring-dependencies` | `microsphere-spring-context` |
| [microsphere-spring-boot](/projects/microsphere-spring-boot) | `microsphere-spring-boot-dependencies` | `microsphere-spring-boot-core` |
| [microsphere-spring-cloud](/projects/microsphere-spring-cloud) | `microsphere-spring-cloud-dependencies` | `microsphere-spring-cloud-commons` |
| [microsphere-i18n](/projects/microsphere-i18n) | `microsphere-i18n-dependencies` | `microsphere-i18n-core` |
| [microsphere-observability](/projects/microsphere-observability) | `microsphere-observability-dependencies` | `microsphere-observability-metrics-micrometer` |
| [microsphere-gateway](/projects/microsphere-gateway) | `microsphere-gateway-dependencies` | `microsphere-spring-cloud-gateway-server-webflux` |
| [microsphere-redis](/projects/microsphere-redis) | `microsphere-redis-dependencies` | `microsphere-redis-spring` |
| [microsphere-mybatis](/projects/microsphere-mybatis) | `microsphere-mybatis-dependencies` | `microsphere-mybatis-core` |
| [microsphere-hibernate](/projects/microsphere-hibernate) | `microsphere-hibernate-dependencies` | `microsphere-hibernate-core` |
| [microsphere-alibaba-druid](/projects/microsphere-alibaba-druid) | `microsphere-alibaba-druid-dependencies` | `microsphere-alibaba-druid-spring-cloud` |
| [microsphere-alibaba-sentinel](/projects/microsphere-alibaba-sentinel) | `microsphere-alibaba-sentinel-dependencies` | `microsphere-alibaba-sentinel-commons` |
| [microsphere-resilience4j](/projects/microsphere-resilience4j) | `microsphere-resilience4j-dependencies` | `microsphere-resilience4j-commons` |
| [microsphere-netflix](/projects/microsphere-netflix) | `microsphere-netflix-dependencies` | `microsphere-netflix-eureka-client-spring-cloud` |
| [microsphere-nacos](/projects/microsphere-nacos) | `microsphere-nacos-dependencies` | — |
| [microsphere-multiactive](/projects/microsphere-multiactive) | `microsphere-multiactive-dependencies` | `microsphere-multiactive-commons` |
| [microsphere-logging](/projects/microsphere-logging) | `microsphere-logging-dependencies` | `microsphere-logging-commons` |

## Gradle

```kotlin
dependencies {
    implementation(platform("io.github.microsphere-projects:microsphere-java-dependencies:$msJavaVersion"))
    implementation("io.github.microsphere-projects:microsphere-java-core")
}
```

## Inheriting the parent POM

If you are developing a Microsphere sub-project itself, inherit the shared parent POM to get the full build setup:

```xml
<parent>
  <groupId>io.github.microsphere-projects</groupId>
  <artifactId>microsphere-build</artifactId>
  <version>${microsphere-build.version}</version>
</parent>
```

See [microsphere-build](/projects/microsphere-build).

## Excluding dependencies

::: tip Auto-configuration exclusions merge
`microsphere.autoconfigure.exclude` merges exclusions from multiple configuration sources, while Spring Boot's
native `spring.autoconfigure.exclude` replaces them. If you declare exclusions in more than one place, prefer the
former.
:::
