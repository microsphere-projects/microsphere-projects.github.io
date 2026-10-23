---
title: Microsphere Gateway
description: "扩展 Spring Cloud Gateway 生态，提供 Microsphere 特有的路由、服务发现与刷新行为。通过自定义 we:// 路由协议，把已发现服务的 Web 端点统一暴露在单个网关之后，无需在每个服务里重复定义路由。"
outline: deep
project:
  slug: microsphere-gateway
  layer: integration
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

扩展 Spring Cloud Gateway 生态，提供 Microsphere 特有的路由、服务发现与刷新行为。通过自定义 we:// 路由协议，把已发现服务的 Web 端点统一暴露在单个网关之后，无需在每个服务里重复定义路由。

## 核心特性

- **双栈支持** — 分别为 Spring Cloud Gateway WebFlux 与 Gateway Server MVC 提供独立模块。
- **we:// 动态路由** — 通过自定义 we:// 路由协议，基于 Spring Cloud 服务发现动态路由已发现的 Web 端点。
- **路由自动保鲜** — 当网关配置、路由定义或服务实例发生变化时自动保持路由最新。
- **精细化暴露规则** — 通过 metadata.web-endpoint.excludes 按路径、方法、请求头、参数、consumes、produces 过滤。
- **统一 BOM 与公共模块** — 提供 BOM 与共享 commons 模块，保证各模块一致接入。

## 用法示例

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: web-endpoint-mapping
          uri: we://all            # subscribe to every discovered service
          predicates:
            - Path=/{application}/**
          metadata:
            web-endpoint:
              excludes:
                - patterns: /internal/**
                  methods: GET
```

## 模块构成

| 模块 | |
|------|------|
| `microsphere-spring-cloud-gateway-commons` | 共享常量、注解与配置绑定 |
| `microsphere-spring-cloud-gateway-server-webflux` | 响应式网关集成 |
| `microsphere-spring-cloud-gateway-server-webmvc` | Servlet 网关集成（Spring Cloud Gateway Server MVC） |
| `microsphere-gateway-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-gateway-dependencies</artifactId>
            <version>${microsphere-gateway.version}</version>
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
        <artifactId>microsphere-spring-cloud-gateway-server-webflux</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| | |
|------|------|
| JDK | 17+ |
| Maven | 3.9+ |
| Spring Cloud | 2022 / 2023 / 2024 / 2025 |

::: tip 注意
目标服务必须发布 Microsphere Web 端点元数据，网关才能发现请求映射并正确重写入站路径。
:::

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-gateway)
- [问题反馈](https://github.com/microsphere-projects/microsphere-gateway/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-gateway)
- [Maven Central · microsphere-spring-cloud-gateway-server-webflux](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-spring-cloud-gateway-server-webflux)

<ProjectNav></ProjectNav>
