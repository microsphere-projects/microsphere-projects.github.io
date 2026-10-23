---
title: Microsphere Java
description: "Microsphere Java Framework is the backbone of the Microsphere ecosystem. Built purely on standard Java APIs, it ships a complete set of reusable components covering strings, collections, reflection, type conversion, event dispatching, class loading and artifact detection, networking, I/O and concurrency — plus a compile-time annotation processor. Every other sub-project builds on top of it."
outline: deep
project:
  slug: microsphere-java
  layer: runtime
---

<ProjectHeader></ProjectHeader>

## Overview

Microsphere Java Framework is the backbone of the Microsphere ecosystem. Built purely on standard Java APIs, it ships a complete set of reusable components covering strings, collections, reflection, type conversion, event dispatching, class loading and artifact detection, networking, I/O and concurrency — plus a compile-time annotation processor. Every other sub-project builds on top of it.

## Key Features

- **String & Collection Utilities** — Null-safe helpers for strings, arrays, lists, sets, maps and deques.
- **Reflection Utilities** — Simplified access to fields, methods, constructors and generic type arguments.
- **Type Conversion** — An extensible Converter SPI with built-in converters for primitives, collections, Duration, InputStream and more.
- **Event Dispatching** — A lightweight EventDispatcher with sequential (direct) and parallel execution modes.
- **Class Loading & Artifact Detection** — Classpath scanning, JAR introspection and Maven/module artifact resolution, including runtime version detection from JAR manifests.
- **Networking & I/O** — A custom URLStreamHandler and URL helpers, plus enhanced file, stream and charset utilities with a file-watch service.
- **Concurrency** — Delegating executor wrappers and a custom ThreadFactory.
- **Configuration Properties** — SPI-based property loading with annotation-driven metadata generation.
- **Compile-time Annotation Processing** — An annotation processor that generates metadata for @ConfigurationProperty.
- **Language Model & JDK Tools** — Components for the Java Language Model API, plus helpers bridging the compiler and annotation-processing tool APIs.
- **Testing Support** — Base classes and utilities for JUnit 5-based unit tests.

## Usage Example

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

## Modules

| Module | |
|------|------|
| `microsphere-java-annotations` | Common annotations: @Nullable, @Nonnull, @Immutable, @Experimental, @Since |
| `microsphere-java-core` | Core utilities: strings, collections, reflection, I/O, concurrency, events, type conversion |
| `microsphere-lang-model` | Components and utilities for the Java Language Model API |
| `microsphere-jdk-tools` | Helpers for the Java compiler and JDK tool APIs |
| `microsphere-annotation-processor` | Compile-time processor generating @ConfigurationProperty metadata |
| `microsphere-java-test` | Models and utilities for JUnit 5-based testing |
| `microsphere-java-dependencies` | BOM managing dependency versions |
| `microsphere-java-parent` | Parent POM with shared build configuration |

## Getting Started

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

Then add only the modules you need — versions are managed by the BOM:

```xml
<dependencies>
    <dependency>
        <groupId>io.github.microsphere-projects</groupId>
        <artifactId>microsphere-java-core</artifactId>
    </dependency>
</dependencies>
```

## Requirements

| | |
|------|------|
| Java | 8 / 11 / 17 / 21 / 25 (all in CI) |
| Maven | 3.6+ |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-java)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-java/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-java)
- [Maven Central · microsphere-java-core](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-java-core)

<ProjectNav></ProjectNav>
