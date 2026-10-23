---
title: 快速开始
description: 从引入 BOM 到跑通第一个 Microsphere 特性
outline: [2, 3]
---

# 快速开始

Microsphere 的所有子项目都可以**按需引入**。下面按最常见的三条路径给出最小可用配置。

## 前置条件

| 组件 | 版本 |
|------|------|
| JDK | 17+（L2 及以上）/ 8+（仅 L1 运行时基座） |
| Maven | 3.6+（Spring Boot 相关项目建议 3.9+） |
| 构建工具 | Maven 或 Gradle 均可，制品已发布至 Maven Central |

## 路径一：只用 Java 工具库

适合任何 Java 应用，不引入 Spring。

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

## 路径二：Spring / Spring Boot 应用

在既有 Spring Boot 应用上叠加增强能力，**无需修改任何现有配置**。

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

### 第一步：让配置源可自动刷新

```java
@Configuration
@ResourcePropertySource(
        name = "app-config",
        value = "classpath*:/META-INF/config/*.properties",
        autoRefreshed = true)
public class AppConfig { }
```

### 第二步：给缓存加上 TTL

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

### 第三步：透明开启 SQL 追踪

```java
@Configuration
@EnableP6DataSource
public class DataSourceConfig { }
```

启动后访问 `/actuator/microsphere/*` 可以看到新增的四个诊断端点。

## 路径三：Spring Cloud 微服务

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
@EnableFeignAutoRefresh       // 配置变更时自动刷新 Feign 组件
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

## 验证是否生效

| 检查项 | 方法 |
|--------|------|
| 依赖版本是否对齐 | `mvn dependency:tree -Dincludes=io.github.microsphere-projects` |
| Actuator 端点是否注册 | 访问 `/actuator/microsphere/web-endpoint-mappings` |
| 配置刷新是否工作 | 修改属性文件，观察日志中出现 Feign 组件重建记录 |
| 指标是否采集 | 访问 `/actuator/prometheus`，检索 `microsphere_` 前缀 |

## 下一步

- [依赖与 BOM](/zh/guide/dependencies) — 各子项目的 BOM 与模块坐标全集
- [版本兼容矩阵](/zh/guide/compatibility) — 选择 `main` 还是 `1.x`
- [架构大图](/zh/architecture) — 理解各能力之间的组合方式
