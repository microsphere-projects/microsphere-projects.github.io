---
title: Microsphere etcd
description: "面向 etcd 分布式键值存储的 Microsphere 集成项目，可作为配置中心与服务发现的后端选项。"
outline: deep
project:
  slug: microsphere-etcd
  name: Microsphere etcd
  layer: integration
  tagline: etcd 集成
  lang: Java
  stars: 0
  forks: 7
  artifactId: microsphere-etcd
---

<ProjectHeader />

## 它解决什么问题

面向 etcd 分布式键值存储的 Microsphere 集成项目，可作为配置中心与服务发现的后端选项。

## 核心特性

- **etcd 集成** — 提供与 etcd 的集成能力。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-etcd` | etcd 集成聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-etcd</artifactId>
            <version>${microsphere-etcd.version}</version>
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

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-etcd)
- [问题反馈](https://github.com/microsphere-projects/microsphere-etcd/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-etcd)
- [Maven Central · microsphere-etcd](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-etcd)

<ProjectNav />
