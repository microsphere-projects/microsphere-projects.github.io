---
title: Microsphere i18n
description: "一套完整的 Java 国际化框架，并与 Spring 生态深度集成。它提供模块化、可扩展的架构来管理本地化消息，覆盖从独立 Spring 应用到分布式云原生微服务的各类部署形态。"
outline: deep
project:
  slug: microsphere-i18n
  name: Microsphere i18n
  layer: crosscutting
  tagline: 面向微服务的分层国际化框架
  lang: Java
  stars: 13
  forks: 18
  artifactId: microsphere-i18n-core
  bom: microsphere-i18n-dependencies
  version: 0.2.21
---

<ProjectHeader />

## 它解决什么问题

一套完整的 Java 国际化框架，并与 Spring 生态深度集成。它提供模块化、可扩展的架构来管理本地化消息，覆盖从独立 Spring 应用到分布式云原生微服务的各类部署形态。

## 核心特性

- **分层消息源** — 通过统一的 ServiceMessageSource 抽象，从 classpath 属性文件、Spring Environment 或外部配置系统加载本地化消息。
- **带优先级的组合源** — CompositeServiceMessageSource 组合多个消息源，高优先级源遮蔽低优先级源。
- **动态配置** — 与 Spring Cloud 集成，运行时更新消息而无需重启应用。
- **Spring MessageSource 桥接** — 主 ServiceMessageSource Bean 自动暴露为 Spring 的 MessageSource，与 @Value、Thymeleaf 等无缝协作。
- **Bean Validation 集成** — i18n 感知的 LocalValidatorFactoryBean，经同一消息源翻译约束违规信息。
- **OpenFeign 传播** — Accept-Language 请求拦截器自动把当前 Locale 转发给下游 Feign 客户端。
- **Actuator 端点** — 通过 /actuator/i18n 在运行时读写 i18n 消息。
- **集中式 i18n 服务** — 通过专门的 Spring Cloud Server 模块跨微服务统一提供消息包。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-i18n-core` | 基础 i18n 抽象与消息源实现 |
| `microsphere-i18n-spring` | 与 Spring Framework 的 MessageSource 和 Environment 集成 |
| `microsphere-i18n-spring-boot` | 自动配置与 Actuator 端点 |
| `microsphere-i18n-spring-cloud` | 基于 Spring Cloud Config 的动态配置更新 |
| `microsphere-i18n-spring-cloud-server` | 集中式 i18n 管理服务 |
| `microsphere-i18n-openfeign` | 向 OpenFeign 客户端传播当前 Locale |
| `microsphere-i18n-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-i18n-dependencies</artifactId>
            <version>${microsphere-i18n.version}</version>
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
        <artifactId>microsphere-i18n-core</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| 项目 | 版本 |
|------|------|
| Java | 17+ |
| Spring Framework | 6.x |
| Spring Boot | 3.x |
| Spring Cloud | 2022.0.x – 2025.0.x |

### 版本线

| 分支 | 兼容范围 | 最新版本 |
|------|----------|----------|
| `main` | 2022.0.x – 2025.0.x | `0.2.21` |
| `1.x` | Hoxton – 2021.0.x | `0.1.21` |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-i18n)
- [问题反馈](https://github.com/microsphere-projects/microsphere-i18n/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-i18n)
- [Maven Central · microsphere-i18n-core](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-i18n-core)

<ProjectNav />
