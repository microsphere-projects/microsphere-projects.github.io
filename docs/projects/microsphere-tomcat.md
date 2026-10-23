---
title: Microsphere Tomcat
description: "An integration project for Apache Tomcat, supporting Tomcat dynamic configuration and lifecycle management in scenarios such as Eureka server clustering and embedded test containers."
outline: deep
project:
  slug: microsphere-tomcat
  layer: integration
---

<ProjectHeader></ProjectHeader>

## Overview

An integration project for Apache Tomcat, supporting Tomcat dynamic configuration and lifecycle management in scenarios such as Eureka server clustering and embedded test containers.

## Key Features

- **Tomcat integration** — Integration with Apache Tomcat.
- **Dynamic configuration** — Works with the Tomcat dynamic configuration support in Spring Cloud fault tolerance utilities.

## Modules

| Module | |
|------|------|
| `microsphere-tomcat` | Aggregator module for the Tomcat integration |

## Getting Started

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

## Requirements

| | |
|------|------|
| Java | 8+ |

## Links

- [GitHub Repository](https://github.com/microsphere-projects/microsphere-tomcat)
- [Report an Issue](https://github.com/microsphere-projects/microsphere-tomcat/issues)
- [DeepWiki Docs](https://deepwiki.com/microsphere-projects/microsphere-tomcat)
- [Maven Central · microsphere-tomcat](https://central.sonatype.com/artifact/io.github.microsphere-projects/microsphere-tomcat)

<ProjectNav></ProjectNav>
