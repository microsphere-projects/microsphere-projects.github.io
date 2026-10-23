---
title: Microsphere Java EE
description: "以 Microsphere 的方式实现 Java EE（Jakarta EE 前身）规范，为需要标准化企业 API 的场景提供与生态一致的编程模型。"
outline: deep
project:
  slug: microsphere-java-enterprise
  name: Microsphere Java EE
  layer: runtime
  tagline: Java EE 规范的 Microsphere 实现
  lang: Java
  stars: 14
  forks: 18
  artifactId: microsphere-java-enterprise
---

<ProjectHeader />

## 它解决什么问题

以 Microsphere 的方式实现 Java EE（Jakarta EE 前身）规范，为需要标准化企业 API 的场景提供与生态一致的编程模型。

## 核心特性

- **规范实现** — 按 Java EE 规范提供对应实现模块。
- **生态一致性** — 复用 Microsphere Java 的反射、类型转换与事件能力。
- **与 Jakarta 分支并行** — 与 microsphere-jakarta 形成 EE / Jakarta 双线支持。

## 模块构成

| 模块 | 说明 |
|------|------|
| `microsphere-java-enterprise` | Java EE 规范实现聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-java-enterprise</artifactId>
            <version>${microsphere-java-enterprise.version}</version>
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

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-java-enterprise)
- [问题反馈](https://github.com/microsphere-projects/microsphere-java-enterprise/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-java-enterprise)
- [Maven Central · microsphere-java-enterprise](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-java-enterprise)

<ProjectNav />
