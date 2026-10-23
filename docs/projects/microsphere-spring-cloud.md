---
title: Microsphere Spring Cloud
description: "面向 Spring Cloud 的生产就绪扩展库，重点解决分布式系统运维中的常见痛点——尤其是无需重启应用即可完成运行时配置变更。"
outline: deep
project:
  slug: microsphere-spring-cloud
  name: Microsphere Spring Cloud
  layer: framework
  tagline: 免重启的动态运行时配置能力
  lang: Java
  stars: 33
  forks: 30
  artifactId: microsphere-spring-cloud-commons
  bom: microsphere-spring-cloud-dependencies
  version: 0.2.26
---

<ProjectHeader />

## 它解决什么问题

面向 Spring Cloud 的生产就绪扩展库，重点解决分布式系统运维中的常见痛点——尤其是无需重启应用即可完成运行时配置变更。

## 核心特性

- **OpenFeign 自动刷新** — 响应 EnvironmentChangeEvent 动态刷新 Feign 客户端的 encoder、decoder、retryer、请求拦截器等配置，无需重启。
- **多注册中心** — 通过统一 API 将同一服务实例同时注册到 Nacos、Eureka、Consul、Zookeeper 等多个注册中心。
- **服务注册事件** — 经 AOP 发布 RegistrationPreRegisteredEvent、RegistrationRegisteredEvent、RegistrationPreDeregisteredEvent、RegistrationDeregisteredEvent，实现注册状态变更的细粒度可观测。
- **联合 DiscoveryClient** — 在单一 DiscoveryClient 接口后聚合多个服务发现后端的实例。
- **容错工具** — 加权轮询负载均衡与 Tomcat 动态配置支持，提升韧性。
- **Actuator 端点** — 内置 /service-registration 与 /service-deregistration 端点，支持运行时运维控制。
- **多版本支持** — main 分支兼容 Spring Cloud 2022.x – 2025.x，1.x 分支兼容 Hoxton – 2021.0.x。

## 用法示例

```java
@SpringBootApplication
@EnableFeignClients
@EnableFeignAutoRefresh     // 配置变更时自动刷新 Feign 组件
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-spring-cloud-commons` | 服务发现、注册与容错的通用工具 |
| `microsphere-spring-cloud-openfeign` | OpenFeign 扩展，支持自动刷新 |
| `microsphere-spring-cloud-dependencies` | BOM，集中依赖管理 |
| `microsphere-spring-cloud-parent` | 父 POM，含 Spring Cloud 版本 profile |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-spring-cloud-dependencies</artifactId>
            <version>${microsphere-spring-cloud.version}</version>
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
        <artifactId>microsphere-spring-cloud-commons</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| 项目 | 版本 |
|------|------|
| Java | 17+ |
| Spring Boot | 3.0+（main）/ 2.x（1.x） |
| Spring Cloud | 2022.0.x – 2025.0.x |
| Maven | 3.6+ |

### 版本线

| 分支 | 兼容范围 | 最新版本 |
|------|----------|----------|
| `main` | 2022.0.x – 2025.0.x | `0.2.26` |
| `1.x` | Hoxton – 2021.0.x | `0.1.26` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-spring-cloud)
- [问题反馈](https://github.com/microsphere-projects/microsphere-spring-cloud/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-spring-cloud)
- [Maven Central · microsphere-spring-cloud-commons](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-spring-cloud-commons)

<ProjectNav />
