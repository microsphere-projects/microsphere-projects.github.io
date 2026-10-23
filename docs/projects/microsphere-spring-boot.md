---
title: Microsphere Spring Boot
description: "围绕配置管理、应用诊断与增强监控，为 Spring Boot 应用补充生产就绪能力：既有开箱即用的默认值，也有把运行时状态暴露得更彻底的 Actuator 端点，还解决了 Spring Boot 2.x 到 4.x 的跨版本兼容问题。"
outline: deep
project:
  slug: microsphere-spring-boot
  name: Microsphere Spring Boot
  layer: framework
  tagline: 配置治理、应用诊断与增强监控
  lang: Java
  stars: 24
  forks: 22
  artifactId: microsphere-spring-boot-core
  bom: microsphere-spring-boot-dependencies
  version: 0.2.34
---

<ProjectHeader />

## 它解决什么问题

围绕配置管理、应用诊断与增强监控，为 Spring Boot 应用补充生产就绪能力：既有开箱即用的默认值，也有把运行时状态暴露得更彻底的 Actuator 端点，还解决了 Spring Boot 2.x 到 4.x 的跨版本兼容问题。

## 核心特性

- **默认属性** — 从 classpath 的 config/default/*.properties 加载优雅停机、MVC 过滤器开关等默认值，可按模块覆盖。
- **高级自动配置管理** — 可配置的导入过滤器，合并多个 microsphere.autoconfigure.exclude 来源而不丢失先前排除项。
- **配置绑定监听** — 事件驱动的 BindListener，在 @ConfigurationProperties 绑定值变化时通知业务 Bean。
- **自定义 Actuator 端点** — 新增四个端点，暴露类路径制品元数据、Web 端点映射、配置元数据与已绑定配置属性。
- **受监控任务调度器** — ThreadPoolTaskScheduler 包装器，通过 Micrometer 记录任务延迟与执行次数。
- **制品冲突检测** — 启动时检测类路径上的重复 JAR 制品，并以描述性 FailureAnalyzer 消息呈现。
- **多版本兼容** — 专用兼容 shim 模块让同一套代码同时跑在 Spring Boot 2.x 至 4.x 上，无需分叉维护。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-spring-boot-core` | 核心：默认属性、自动配置过滤器、绑定监听器、诊断 |
| `microsphere-spring-boot-actuator` | Actuator 扩展：自定义端点、受监控调度器、端点默认值 |
| `microsphere-spring-boot-compatible` | Spring Boot 2.x – 4.x 兼容 shim（不发布至 Maven Central） |
| `microsphere-spring-boot-dependencies` | BOM |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-spring-boot-dependencies</artifactId>
            <version>${microsphere-spring-boot.version}</version>
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
        <artifactId>microsphere-spring-boot-core</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| 项目 | 版本 |
|------|------|
| Java | 17+ |
| Spring Boot | 3.0.x – 4.1.x（main）/ 2.0.x – 2.7.x（1.x） |
| Maven | 3.9+ |

### 版本线

| 分支 | 兼容范围 | 最新版本 |
|------|----------|----------|
| `main` | 3.0.x – 3.5.x, 4.0.x – 4.1.x | `0.2.34` |
| `1.x` | 2.0.x – 2.7.x | `0.1.34` |

::: tip 注意
相比标准 spring.autoconfigure.exclude 的覆盖语义，microsphere.autoconfigure.exclude 采用合并语义，多个配置源的排除项会累加。
:::

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-spring-boot)
- [问题反馈](https://github.com/microsphere-projects/microsphere-spring-boot/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-spring-boot)
- [Maven Central · microsphere-spring-boot-core](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-spring-boot-core)

<ProjectNav />
