---
title: Microsphere Spring
description: "以模块化方式解决真实生产场景中的 Spring 痛点：增强依赖注入、配置管理、Web 端点处理、事件、缓存与 JDBC 监控。它是纯粹的增量增强，可作为 drop-in 依赖接入任何既有 Spring 应用。"
outline: deep
project:
  slug: microsphere-spring
  name: Microsphere Spring
  layer: framework
  tagline: 面向生产环境的 Spring Framework 扩展库
  lang: Java
  stars: 61
  forks: 39
  artifactId: microsphere-spring-context
  bom: microsphere-spring-dependencies
  version: 0.2.39
---

<ProjectHeader />

## 它解决什么问题

以模块化方式解决真实生产场景中的 Spring 痛点：增强依赖注入、配置管理、Web 端点处理、事件、缓存与 JDBC 监控。它是纯粹的增量增强，可作为 drop-in 依赖接入任何既有 Spring 应用。

## 核心特性

- **并行 Bean 实例化** — 解析 Bean 依赖图，并发初始化互不依赖的单例，显著缩短启动时间。
- **可监听的 Environment** — 通过 EnvironmentListener / PropertyResolverListener 拦截属性解析与 profile 激活事件。
- **增强的 @PropertySource** — @ResourcePropertySource 支持通配符资源、顺序控制、继承、变更自动刷新，并提供 @YamlPropertySource、@JsonPropertySource。
- **TTL 缓存** — @EnableTTLCaching / @TTLCacheable 为 Spring Cache 增加条目级过期时间，支持 Redis。
- **Web 端点注册表** — 启动时收集 Spring MVC、WebFlux 与经典 Servlet 的 WebEndpointMapping 元数据，供内省与路由使用。
- **Handler 方法拦截** — HandlerMethodInterceptor / HandlerMethodArgumentInterceptor 提供围绕 MVC 与 WebFlux 控制器调用的 AOP 式钩子。
- **P6Spy JDBC 监控** — @EnableP6DataSource 透明包装既有 DataSource Bean，实现 SQL 追踪。
- **Google Guice 集成** — @EnableGuice 把 Guice @Inject 注入点桥接到 Spring Bean 生命周期。
- **丰富的测试工具** — EmbeddedTomcatContextLoader、EnableEmbeddedDatabase、AbstractWebFluxTest 等。

## 用法示例

```java
@Configuration
@ResourcePropertySource(
        name = "app-config",
        value = "classpath*:/META-INF/config/*.properties",
        autoRefreshed = true)      // 任一匹配文件变化即自动重载
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
@EnableP6DataSource          // 透明包裹所有 DataSource，零改代码接入 SQL 追踪
public class DataSourceConfig { }
```

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-spring-context` | 核心上下文与配置扩展：@ResourcePropertySource、@EnableTTLCaching、@EnableConfigurationBeanBinding |
| `microsphere-spring-web` | 共享 Web 抽象：WebEndpointMapping、HandlerMethodInterceptor、@EnableWebExtension、@Idempotent |
| `microsphere-spring-webmvc` | Spring MVC 扩展：@EnableWebMvcExtension、ReversedProxyHandlerMapping |
| `microsphere-spring-webflux` | 响应式扩展：@EnableWebFluxExtension、InterceptingHandlerMethodProcessor |
| `microsphere-spring-jdbc` | JDBC / P6Spy 集成：@EnableP6DataSource |
| `microsphere-spring-guice` | Google Guice 桥接：@EnableGuice |
| `microsphere-spring-test` | 测试工具：@EnableEmbeddedDatabase、EmbeddedTomcatContextLoader |

## 引入依赖

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

然后按需引入模块（版本由 BOM 管理，无需指定）：

```xml
<dependencies>
    <dependency>
        <groupId>io.github.microsphere-projects</groupId>
        <artifactId>microsphere-spring-context</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| 项目 | 版本 |
|------|------|
| Java | 17+ |
| Spring Framework | 6.0.x – 7.0.x（main）/ 4.3.x – 5.3.x（1.x） |
| Maven | 3.6+ |

### 版本线

| 分支 | 兼容范围 | 最新版本 |
|------|----------|----------|
| `main` | 6.0.x – 7.0.x | `0.2.39` |
| `1.x` | 4.3.x – 5.3.x | `0.1.39` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-spring)
- [问题反馈](https://github.com/microsphere-projects/microsphere-spring/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-spring)
- [Maven Central · microsphere-spring-context](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-spring-context)

<ProjectNav />
