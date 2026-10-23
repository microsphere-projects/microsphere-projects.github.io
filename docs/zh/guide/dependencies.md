---
title: 依赖与 BOM
description: 全部子项目的 BOM 坐标与推荐引入模块
outline: [2, 3]
---

# 依赖与 BOM

所有制品的 Group ID 统一为 `io.github.microsphere-projects`，已发布至 Maven Central。

## 为什么每个项目都有自己的 BOM

Microsphere 采用**按子项目划分 BOM** 的策略，而不是一个巨型 BOM。原因是各子项目面向不同的 Spring 代际，
版本节奏并不一致——`microsphere-spring` 更新到 `0.2.39` 时，`microsphere-i18n` 可能停在 `0.2.21`。
分开管理可以让每个 BOM 独立演进，使用者按需导入即可。

如果你希望一次性对齐多个子项目，可以同时导入多个 BOM，Maven 会按声明顺序解析。

## BOM 坐标

| 子项目 | BOM Artifact ID | 推荐入口模块 |
|--------|-----------------|--------------|
| [microsphere-java](/zh/projects/microsphere-java) | `microsphere-java-dependencies` | `microsphere-java-core` |
| [microsphere-spring](/zh/projects/microsphere-spring) | `microsphere-spring-dependencies` | `microsphere-spring-context` |
| [microsphere-spring-boot](/zh/projects/microsphere-spring-boot) | `microsphere-spring-boot-dependencies` | `microsphere-spring-boot-core` |
| [microsphere-spring-cloud](/zh/projects/microsphere-spring-cloud) | `microsphere-spring-cloud-dependencies` | `microsphere-spring-cloud-commons` |
| [microsphere-i18n](/zh/projects/microsphere-i18n) | `microsphere-i18n-dependencies` | `microsphere-i18n-core` |
| [microsphere-observability](/zh/projects/microsphere-observability) | `microsphere-observability-dependencies` | `microsphere-observability-metrics-micrometer` |
| [microsphere-gateway](/zh/projects/microsphere-gateway) | `microsphere-gateway-dependencies` | `microsphere-spring-cloud-gateway-server-webflux` |
| [microsphere-redis](/zh/projects/microsphere-redis) | `microsphere-redis-dependencies` | `microsphere-redis-spring` |
| [microsphere-mybatis](/zh/projects/microsphere-mybatis) | `microsphere-mybatis-dependencies` | `microsphere-mybatis-core` |
| [microsphere-hibernate](/zh/projects/microsphere-hibernate) | `microsphere-hibernate-dependencies` | `microsphere-hibernate-core` |
| [microsphere-alibaba-druid](/zh/projects/microsphere-alibaba-druid) | `microsphere-alibaba-druid-dependencies` | `microsphere-alibaba-druid-spring-cloud` |
| [microsphere-alibaba-sentinel](/zh/projects/microsphere-alibaba-sentinel) | `microsphere-alibaba-sentinel-dependencies` | `microsphere-alibaba-sentinel-commons` |
| [microsphere-resilience4j](/zh/projects/microsphere-resilience4j) | `microsphere-resilience4j-dependencies` | `microsphere-resilience4j-commons` |
| [microsphere-netflix](/zh/projects/microsphere-netflix) | `microsphere-netflix-dependencies` | `microsphere-netflix-eureka-client-spring-cloud` |
| [microsphere-nacos](/zh/projects/microsphere-nacos) | `microsphere-nacos-dependencies` | — |
| [microsphere-multiactive](/zh/projects/microsphere-multiactive) | `microsphere-multiactive-dependencies` | `microsphere-multiactive-commons` |
| [microsphere-logging](/zh/projects/microsphere-logging) | `microsphere-logging-dependencies` | `microsphere-logging-commons` |

## Gradle 写法

```kotlin
dependencies {
    implementation(platform("io.github.microsphere-projects:microsphere-java-dependencies:$msJavaVersion"))
    implementation("io.github.microsphere-projects:microsphere-java-core")
}
```

## 继承父 POM（适用于 Microsphere 生态内部项目）

如果你在开发一个 Microsphere 子项目，直接继承统一父 POM 即可获得全部构建配置：

```xml
<parent>
  <groupId>io.github.microsphere-projects</groupId>
  <artifactId>microsphere-build</artifactId>
  <version>${microsphere-build.version}</version>
</parent>
```

详见 [microsphere-build](/zh/projects/microsphere-build)。

## 排除依赖

::: tip 自动配置排除用合并语义
`microsphere.autoconfigure.exclude` 会合并多个配置源的排除项，而 Spring Boot 原生的
`spring.autoconfigure.exclude` 是覆盖语义。若你在多处配置排除项，请优先使用前者。
:::
