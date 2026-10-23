---
title: Getting Started
description: From importing a BOM to running your first Microsphere feature
outline: [2, 3]
---

# Getting Started

Every Microsphere sub-project can be adopted **on demand**. Below are the three most common starting paths, each with
a minimal working configuration.

## Prerequisites

| Component | Version |
|-----------|---------|
| JDK | 17+ (L2 and above) / 8+ (L1 runtime only) |
| Maven | 3.6+ (3.9+ recommended for Spring Boot projects) |
| Build tool | Maven or Gradle — artifacts are on Maven Central |

## Path 1: the utility library only

For any Java application, with no Spring involved.

```xml
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>io.github.microsphere-projects</groupId>
      <artifactId>microsphere-java-dependencies</artifactId>
      <version>${microsphere-java.version}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>

<dependencies>
  <dependency>
    <groupId>io.github.microsphere-projects</groupId>
    <artifactId>microsphere-java-core</artifactId>
  </dependency>
</dependencies>
```

```java
import io.microsphere.convert.Converters;
import io.microsphere.util.StringUtils;

StringUtils.isBlank("  ");                      // true
Integer n = Converters.convert("42", Integer.class);
List<String> l = Converters.convert("a,b,c", List.class);
```

## Path 2: a Spring / Spring Boot application

Layer enhancements onto an existing Spring Boot app **without changing any existing configuration**.

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
    <dependency>
      <groupId>io.github.microsphere-projects</groupId>
      <artifactId>microsphere-spring-boot-dependencies</artifactId>
      <version>${microsphere-spring-boot.version}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>

<dependencies>
  <dependency>
    <groupId>io.github.microsphere-projects</groupId>
    <artifactId>microsphere-spring-context</artifactId>
  </dependency>
  <dependency>
    <groupId>io.github.microsphere-projects</groupId>
    <artifactId>microsphere-spring-boot-core</artifactId>
  </dependency>
</dependencies>
```

### Step 1: make property sources self-refreshing

```java
@Configuration
@ResourcePropertySource(
        name = "app-config",
        value = "classpath*:/META-INF/config/*.properties",
        autoRefreshed = true)
public class AppConfig { }
```

### Step 2: add TTL to your caches

```java
@Configuration
@EnableTTLCaching
public class CachingConfig { }

@Service
public class ProductService {
    @TTLCacheable(cacheNames = "products", ttl = 300, timeUnit = TimeUnit.SECONDS)
    public Product findById(Long id) { /* ... */ }
}
```

### Step 3: enable SQL tracing transparently

```java
@Configuration
@EnableP6DataSource
public class DataSourceConfig { }
```

After startup, the four extra diagnostic endpoints are available under `/actuator/microsphere/*`.

## Path 3: Spring Cloud microservices

```xml
<dependency>
  <groupId>io.github.microsphere-projects</groupId>
  <artifactId>microsphere-spring-cloud-commons</artifactId>
</dependency>
<dependency>
  <groupId>io.github.microsphere-projects</groupId>
  <artifactId>microsphere-spring-cloud-openfeign</artifactId>
</dependency>
```

```java
@SpringBootApplication
@EnableFeignClients
@EnableFeignAutoRefresh       // refresh Feign components when configuration changes
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

## Verifying it works

| What to check | How |
|---------------|-----|
| Dependency versions aligned | `mvn dependency:tree -Dincludes=io.github.microsphere-projects` |
| Actuator endpoints registered | Visit `/actuator/microsphere/web-endpoint-mappings` |
| Config refresh working | Edit the properties file and look for Feign component rebuild logs |
| Metrics collected | Visit `/actuator/prometheus` and search for the `microsphere_` prefix |

## Next steps

- [Dependencies & BOMs](/guide/dependencies) — the full coordinate list for every sub-project
- [Compatibility matrix](/guide/compatibility) — choosing between `main` and `1.x`
- [Architecture](/architecture) — how the capabilities compose
