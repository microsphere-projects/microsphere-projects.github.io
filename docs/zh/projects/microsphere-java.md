---
title: Microsphere Java
description: "Microsphere Java Framework 是 Microsphere 生态的骨干基础库。它基于标准 Java API 提供字符串、集合、反射、类型转换、事件分发、类加载与制品探测、网络、I/O、并发等一整套可复用组件，并内置编译期注解处理器。所有其它子项目都构建在它之上。"
outline: deep
project:
  slug: microsphere-java
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## 它解决什么问题

Microsphere Java Framework 是 Microsphere 生态的骨干基础库。它基于标准 Java API 提供字符串、集合、反射、类型转换、事件分发、类加载与制品探测、网络、I/O、并发等一整套可复用组件，并内置编译期注解处理器。所有其它子项目都构建在它之上。

## 核心特性

- **字符串与集合工具** — 对字符串、数组、List、Set、Map、Deque 的空安全（null-safe）辅助方法。
- **反射工具** — 简化字段、方法、构造器以及泛型实参的访问，免去大量样板代码。
- **类型转换** — 可扩展的 Converter SPI，内置基础类型、集合、Duration、InputStream 等转换器。
- **事件分发** — 轻量 EventDispatcher，支持顺序（direct）与并行（parallel）两种执行模式。
- **类加载与制品探测** — 类路径扫描、JAR 内省、Maven / 模块制品解析，支持从 JAR manifest 推断运行时版本。
- **网络与 I/O** — 自定义 URLStreamHandler 与 URL 工具；增强的文件、流、字符集工具以及文件监听服务。
- **并发** — 委派式 Executor 包装器与自定义 ThreadFactory。
- **配置属性** — 基于 SPI 的属性加载，配合注解驱动的元数据生成。
- **编译期注解处理** — 为 @ConfigurationProperty 生成元数据的 Annotation Processor。
- **语言模型与 JDK Tools** — 面向 javax.lang.model 的组件，以及桥接 Java 编译器与注解处理工具 API 的辅助类。
- **测试支持** — 面向 JUnit 5 的基类与工具。

## 用法示例

```java
import io.microsphere.util.StringUtils;
import io.microsphere.convert.Converters;
import io.microsphere.event.EventDispatcher;
import io.microsphere.util.Version;

StringUtils.isBlank("  ");                    // true
Integer n = Converters.convert("42", Integer.class);
List<String> l = Converters.convert("a,b,c", List.class);

EventDispatcher d = EventDispatcher.newDefault();
d.addEventListener((EventListener<MyEvent>) e -> System.out.println(e));
d.dispatch(new MyEvent("hello"));

Version v = Version.ofVersion(org.springframework.core.SpringVersion.class);
boolean modern = v.isGreaterThanOrEqualTo("6.0.0");
```

## 模块构成

| 模块 | |
|------|------|
| `microsphere-java-annotations` | 通用注解：@Nullable、@Nonnull、@Immutable、@Experimental、@Since |
| `microsphere-java-core` | 核心工具：字符串、集合、反射、I/O、并发、事件、类型转换 |
| `microsphere-lang-model` | Java 语言模型 API 的组件与工具 |
| `microsphere-jdk-tools` | Java 编译器与 JDK 工具 API 辅助 |
| `microsphere-annotation-processor` | @ConfigurationProperty 元数据的编译期处理器 |
| `microsphere-java-test` | 基于 JUnit 5 的测试模型与工具 |
| `microsphere-java-dependencies` | BOM，统一管理依赖版本 |
| `microsphere-java-parent` | 父 POM，共享构建配置 |

## 引入依赖

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
```

然后按需引入模块（版本由 BOM 管理，无需指定）：

```xml
<dependencies>
    <dependency>
        <groupId>io.github.microsphere-projects</groupId>
        <artifactId>microsphere-java-core</artifactId>
    </dependency>
</dependencies>
```

## 环境要求

| | |
|------|------|
| Java | 8 / 11 / 17 / 21 / 25（CI 全覆盖） |
| Maven | 3.6+ |

## 相关链接

- [GitHub 仓库](https://github.com/microsphere-projects/microsphere-java)
- [问题反馈](https://github.com/microsphere-projects/microsphere-java/issues)
- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/microsphere-java)
- [Maven Central · microsphere-java-core](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-java-core)

<ProjectNav></ProjectNav>
