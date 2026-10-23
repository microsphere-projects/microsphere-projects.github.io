---
title: Microsphere Test
description: "为 Microsphere 各子项目提供共享的测试基座与断言工具，保证测试风格在全生态内一致。"
outline: deep
project:
  slug: microsphere-test
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

为 Microsphere 各子项目提供共享的测试基座与断言工具，保证测试风格在全生态内一致。

## 核心特性

- **统一测试基座** — 集中提供测试基类与辅助断言。

## 模块构成

| 模块 | |
|------|------|
| `microsphere-test` | 测试基础设施聚合模块 |

## 引入依赖

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.microsphere-projects</groupId>
            <artifactId>microsphere-test</artifactId>
            <version>${microsphere-test.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## 环境要求

| | |
|------|------|
| Java | 8+ |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-test)
- [问题反馈](https://github.com/microsphere-projects/microsphere-test/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-test)
- [Maven Central · microsphere-test](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-test)

<ProjectNav></ProjectNav>
