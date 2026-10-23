---
title: Microsphere Tomcat
description: "面向 Apache Tomcat 的集成项目，支撑 Eureka 服务端集群、嵌入式测试容器等场景下的 Tomcat 动态配置与生命周期管理。"
outline: deep
project:
  slug: microsphere-tomcat
  name: Microsphere Tomcat
  layer: integration
  tagline: Apache Tomcat 集成
  lang: Java
  stars: 2
  forks: 6
  artifactId: microsphere-tomcat
---

<ProjectHeader />

## 它解决什么问题

面向 Apache Tomcat 的集成项目，支撑 Eureka 服务端集群、嵌入式测试容器等场景下的 Tomcat 动态配置与生命周期管理。

## 核心特性

- **Tomcat 集成** — 提供与 Apache Tomcat 的集成能力。
- **动态配置** — 与 Spring Cloud 容错工具中的 Tomcat 动态配置能力协同。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-tomcat` | Tomcat 集成聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-tomcat</artifactId>
            <version>${microsphere-tomcat.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## 环境要求

| 项目 | 版本 |
|------|------|
| Java | 8+ |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-tomcat)
- [问题反馈](https://github.com/microsphere-projects/microsphere-tomcat/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-tomcat)
- [Maven Central · microsphere-tomcat](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-tomcat)

<ProjectNav />
