---
title: 子项目总览
description: Microsphere Projects 全部子项目的分层总览与能力矩阵
outline: false
---

<ProjectsIndex />

## 分层说明

### L0 · 工程基座 · Foundation

统一构建与依赖治理。所有子项目的 Maven 父 POM 与 BOM 在这里定义，保证 36 个仓库的构建口径一致。

### L1 · 运行时基座 · Runtime

不依赖任何框架的纯 Java 能力层：字符串与集合、反射、类型转换、事件、日志抽象、Java/Jakarta EE 实现。

### L2 · 框架扩展 · Framework

对 Spring、Spring Boot、Spring Cloud 的增强扩展，是整个生态最核心的一层。

### L3 · 生态集成 · Integration

面向具体基础设施的适配层：注册中心、数据访问、缓存、RPC、容错、网关。

### L4 · 横向能力 · Cross-cutting

贯穿所有层的可观测性、国际化、安全、动态配置、单元化多活等能力。

> 分层依据是各项目在生态中的依赖位置：L1 不依赖任何框架，L2 构建于 L1 之上扩展 Spring 全家桶，
> L3 面向具体基础设施做适配，L4 是可插拔的横向能力。实际使用时可按需组合，不存在强制依赖。

## 能力矩阵

| 子项目 | 分层 | 语言 | Star | Fork | 一句话 |
|--------|------|------|------|------|--------|
| [Microsphere Build](./microsphere-build) | Foundation | Maven | 8 | 29 | Microsphere 全系项目的 Maven 父 POM |
| [Microsphere BOM](./microsphere-bom) | Foundation | Maven | 0 | 1 | 跨项目的 Maven 物料清单 |
| [Microsphere Java](./microsphere-java) | Runtime | Java | 104 | 52 | 整个生态的地基：可复用的 Java 组件与工具集 |
| [Microsphere Java EE](./microsphere-java-enterprise) | Runtime | Java | 14 | 18 | Java EE 规范的 Microsphere 实现 |
| [Microsphere Jakarta](./microsphere-jakarta) | Runtime | Java | 2 | 6 | Jakarta EE 规范的 Microsphere 实现 |
| [Microsphere Logging](./microsphere-logging) | Runtime | Java | 2 | 1 | 跨日志框架的统一运行时管理抽象层 |
| [Microsphere MicroProfile](./microsphere-microprofile) | Runtime | Java | 1 | 6 | Eclipse MicroProfile 支持 |
| [Microsphere Test](./microsphere-test) | Runtime | Java | 0 | 0 | 跨项目测试基础设施 |
| [Microsphere Tools](./microsphere-tools) | Runtime | Java | 0 | 5 | 通用研发工具集 |
| [Microsphere Spring](./microsphere-spring) | Framework | Java | 61 | 39 | 面向生产环境的 Spring Framework 扩展库 |
| [Microsphere Spring Cloud](./microsphere-spring-cloud) | Framework | Java | 33 | 30 | 免重启的动态运行时配置能力 |
| [Microsphere Spring Boot](./microsphere-spring-boot) | Framework | Java | 24 | 22 | 配置治理、应用诊断与增强监控 |
| [Microsphere Gateway](./microsphere-gateway) | Integration | Java | 5 | 5 | 基于服务发现的 Web 端点动态路由 |
| [Microsphere Dubbo](./microsphere-dubbo) | Integration | Java | 4 | 7 | Apache Dubbo 集成 |
| [Microsphere Redis](./microsphere-redis) | Integration | Java | 3 | 11 | 增强版 Spring Data Redis 集成框架 |
| [Microsphere Alibaba Druid](./microsphere-alibaba-druid) | Integration | Java | 2 | 3 | 为 Druid 连接池注入 SQL 拦截能力 |
| [Microsphere Alibaba Sentinel](./microsphere-alibaba-sentinel) | Integration | Java | 2 | 11 | 把流控能力透明注入数据库、缓存与 Web |
| [Microsphere Nacos](./microsphere-nacos) | Integration | Java | 2 | 6 | Alibaba Nacos 集成 |
| [Microsphere Netflix](./microsphere-netflix) | Integration | Java | 2 | 8 | Eureka 的高可用集群与增强客户端 |
| [Microsphere Resilience4j](./microsphere-resilience4j) | Integration | Java | 2 | 9 | 统一的韧性模式落地方案 |
| [Microsphere Tomcat](./microsphere-tomcat) | Integration | Java | 2 | 6 | Apache Tomcat 集成 |
| [Microsphere MyBatis](./microsphere-mybatis) | Integration | Java | 1 | 3 | 轻量级 SQL 拦截增强框架 |
| [Microsphere etcd](./microsphere-etcd) | Integration | Java | 0 | 7 | etcd 集成 |
| [Microsphere Hibernate](./microsphere-hibernate) | Integration | Java | 0 | 1 | Hibernate ORM 扩展 |
| [Microsphere i18n](./microsphere-i18n) | Cross-cutting | Java | 13 | 18 | 面向微服务的分层国际化框架 |
| [Microsphere DevOps](./microsphere-devops) | Cross-cutting | Shell | 5 | 6 | 生态的工程效能与运维支撑 |
| [Microsphere Multiactive](./microsphere-multiactive) | Cross-cutting | Java | 4 | 14 | 多活与单元化部署的分区感知框架 |
| [Microsphere Observability](./microsphere-observability) | Cross-cutting | Java | 4 | 8 | 监控、指标与日志的一体化增强套件 |
| [Microsphere Dynamic](./microsphere-dynamic) | Cross-cutting | Java | 3 | 7 | 动态化能力支撑 |
| [Microsphere Security](./microsphere-security) | Cross-cutting | Java | 3 | 6 | 安全能力扩展 |
| [Microsphere Configuration](./microsphere-configuration) | Cross-cutting | Java | 2 | 10 | 配置体系增强 |
| [Microsphere AI](./microsphere-ai) | Cross-cutting | Java | 0 | 1 | 面向 AI 场景的探索项目 |

