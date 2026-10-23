# -*- coding: utf-8 -*-
"""Bilingual project data — part B: L3 Integration, L4 Cross-cutting."""

PROJECTS = [
    # ---------------------------------------------------------------- L3
    dict(
        slug="microsphere-gateway", name="Microsphere Gateway", layer="integration",
        stars=5, forks=5, lang="Java", artifact="microsphere-spring-cloud-gateway-server-webflux",
        bom="microsphere-gateway-dependencies",
        en=dict(
            tagline="Discovery-driven dynamic routing for web endpoints",
            summary="Extends the Spring Cloud Gateway ecosystem with Microsphere-specific routing, discovery and refresh "
                    "behaviour. A custom we:// route scheme exposes the web endpoints of discovered services behind a single "
                    "gateway, so you never duplicate route definitions in every service.",
            features=[
                ("Both gateway stacks", "Dedicated modules for Spring Cloud Gateway WebFlux and Gateway Server MVC."),
                ("we:// dynamic routing", "Routes discovered web endpoints dynamically through a custom we:// scheme backed by Spring Cloud discovery."),
                ("Self-refreshing routes", "Keeps routes current when gateway configuration, route definitions or service instances change."),
                ("Fine-grained exposure rules", "metadata.web-endpoint.excludes filters by path, method, header, param, consumes and produces."),
                ("Unified BOM and commons", "A shared BOM and commons module keep every gateway module consistent."),
            ],
            modules=[
                ("microsphere-spring-cloud-gateway-commons", "Shared constants, annotations and configuration binding"),
                ("microsphere-spring-cloud-gateway-server-webflux", "Reactive gateway integration"),
                ("microsphere-spring-cloud-gateway-server-webmvc", "Servlet-based integration for Spring Cloud Gateway Server MVC"),
                ("microsphere-gateway-dependencies", "BOM"),
            ],
            compat=[("JDK", "17+"), ("Maven", "3.9+"), ("Spring Cloud", "2022 / 2023 / 2024 / 2025")],
            note="Target services must publish Microsphere web endpoint metadata so the gateway can discover request "
                 "mappings and rewrite incoming paths correctly.",
        ),
        zh=dict(
            tagline="基于服务发现的 Web 端点动态路由",
            summary="扩展 Spring Cloud Gateway 生态，提供 Microsphere 特有的路由、服务发现与刷新行为。通过自定义 we:// 路由协议，"
                    "把已发现服务的 Web 端点统一暴露在单个网关之后，无需在每个服务里重复定义路由。",
            features=[
                ("双栈支持", "分别为 Spring Cloud Gateway WebFlux 与 Gateway Server MVC 提供独立模块。"),
                ("we:// 动态路由", "通过自定义 we:// 路由协议，基于 Spring Cloud 服务发现动态路由已发现的 Web 端点。"),
                ("路由自动保鲜", "当网关配置、路由定义或服务实例发生变化时自动保持路由最新。"),
                ("精细化暴露规则", "通过 metadata.web-endpoint.excludes 按路径、方法、请求头、参数、consumes、produces 过滤。"),
                ("统一 BOM 与公共模块", "提供 BOM 与共享 commons 模块，保证各模块一致接入。"),
            ],
            modules=[
                ("microsphere-spring-cloud-gateway-commons", "共享常量、注解与配置绑定"),
                ("microsphere-spring-cloud-gateway-server-webflux", "响应式网关集成"),
                ("microsphere-spring-cloud-gateway-server-webmvc", "Servlet 网关集成（Spring Cloud Gateway Server MVC）"),
                ("microsphere-gateway-dependencies", "BOM"),
            ],
            compat=[("JDK", "17+"), ("Maven", "3.9+"), ("Spring Cloud", "2022 / 2023 / 2024 / 2025")],
            note="目标服务必须发布 Microsphere Web 端点元数据，网关才能发现请求映射并正确重写入站路径。",
        ),
        code="""spring:
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
                  methods: GET""",
        lang_code="yaml",
    ),
    dict(
        slug="microsphere-redis", name="Microsphere Redis", layer="integration",
        stars=3, forks=11, lang="Java", artifact="microsphere-redis-spring",
        bom="microsphere-redis-dependencies", version="0.2.14",
        en=dict(
            tagline="An enhanced Spring Data Redis integration framework",
            summary="Adds enterprise-grade capabilities on top of Spring Data Redis: non-intrusive command interception, "
                    "deep Spring integration, comprehensive event publishing and metrics collection, and Redis replication "
                    "support backed by Kafka.",
            features=[
                ("Non-intrusive interception", "Monitor and intercept Redis commands without modifying application code."),
                ("Deep Spring integration", "Seamless integration with Spring dependency injection and auto-configuration."),
                ("Enterprise monitoring", "Comprehensive event publishing and metrics collection."),
                ("Redis replication", "Advanced replication features integrated with Kafka."),
                ("Modular architecture", "Multiple Maven modules with clean separation of concerns."),
                ("Metadata generation", "A dedicated generator module produces Redis metadata."),
            ],
            modules=[
                ("microsphere-redis-core", "Foundational components and utilities for Redis operations"),
                ("microsphere-redis-spring", "Spring Framework integration"),
                ("microsphere-redis-spring-boot", "Spring Boot integration"),
                ("microsphere-redis-spring-cloud", "Spring Cloud integration"),
                ("microsphere-redis-replicator-spring", "Redis replication support"),
                ("microsphere-redis-spring-test", "Spring Test integration"),
                ("microsphere-redis-generator", "Redis metadata generation"),
            ],
            compat=[("Spring Data Redis", "3.0.0 – 3.5.x (main) / 2.1.0 – 2.7.x (1.x)")],
        ),
        zh=dict(
            tagline="增强版 Spring Data Redis 集成框架",
            summary="在 Spring Data Redis 之上提供企业级增强能力：非侵入式的 Redis 命令拦截、深度 Spring 集成、"
                    "全面的事件发布与指标采集，以及基于 Kafka 的 Redis 复制支持。",
            features=[
                ("非侵入式操作拦截", "无需修改应用代码即可监控与拦截 Redis 命令。"),
                ("Spring 深度集成", "与 Spring 依赖注入和自动配置无缝衔接。"),
                ("企业级监控", "全面的事件发布与指标采集能力。"),
                ("Redis 复制支持", "高级复制特性，并与 Kafka 集成。"),
                ("模块化架构", "多 Maven 模块清晰分离关注点。"),
                ("元数据生成", "generator 模块负责 Redis 元数据生成。"),
            ],
            modules=[
                ("microsphere-redis-core", "Redis 操作的基础组件与工具"),
                ("microsphere-redis-spring", "Spring Framework 集成"),
                ("microsphere-redis-spring-boot", "Spring Boot 集成"),
                ("microsphere-redis-spring-cloud", "Spring Cloud 集成"),
                ("microsphere-redis-replicator-spring", "Redis 复制支持"),
                ("microsphere-redis-spring-test", "Spring Test 集成"),
                ("microsphere-redis-generator", "Redis 元数据生成"),
            ],
            compat=[("Spring Data Redis", "3.0.0 – 3.5.x（main）/ 2.1.0 – 2.7.x（1.x）")],
        ),
        versions=[("main", "Spring Data Redis 3.0.0 – 3.5.x", "0.2.14"), ("1.x", "Spring Data Redis 2.1.0 – 2.7.x", "0.1.14")],
    ),
    dict(
        slug="microsphere-mybatis", name="Microsphere MyBatis", layer="integration",
        stars=1, forks=3, lang="Java", artifact="microsphere-mybatis-core",
        bom="microsphere-mybatis-dependencies", version="0.2.16",
        en=dict(
            tagline="A lightweight SQL interception framework",
            summary="Provides powerful SQL statement interception through a mature interception pipeline, letting you "
                    "monitor, modify or enhance SQL execution without changing existing MyBatis code.",
            features=[
                ("SQL execution monitoring", "Collect execution details for logging, metrics and observability."),
                ("Cross-cutting concerns", "Attach security, throttling, caching and other concerns to SQL operations."),
                ("SQL enhancement", "Extend SQL execution capabilities without touching business code."),
                ("Ecosystem interop", "Integrates with Sentinel, Resilience4j, Observability and other Microsphere projects."),
            ],
            modules=[
                ("microsphere-mybatis-core", "Core MyBatis framework"),
                ("microsphere-mybatis-spring", "Spring Framework integration and configuration"),
                ("microsphere-mybatis-spring-boot", "Spring Boot auto-configuration and properties"),
                ("microsphere-mybatis-spring-cloud", "Spring Cloud feature integration"),
                ("microsphere-mybatis-test / spring-test", "Testing infrastructure"),
                ("microsphere-mybatis-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x)")],
        ),
        zh=dict(
            tagline="轻量级 SQL 拦截增强框架",
            summary="通过一套成熟的拦截管道为 MyBatis 提供强大的 SQL 语句拦截能力，在不改动既有 MyBatis 代码的前提下监控、修改或增强 SQL 执行。",
            features=[
                ("SQL 执行监控", "为日志、指标与可观测性采集 SQL 执行情况。"),
                ("横切关注点注入", "为 SQL 操作附加安全、限流、缓存等横切逻辑。"),
                ("SQL 执行增强", "在不侵入业务代码的前提下扩展 SQL 执行能力。"),
                ("生态联动", "与 Sentinel、Resilience4j、Observability 等 Microsphere 项目集成。"),
            ],
            modules=[
                ("microsphere-mybatis-core", "核心 MyBatis 框架"),
                ("microsphere-mybatis-spring", "Spring Framework 集成与配置"),
                ("microsphere-mybatis-spring-boot", "Spring Boot 自动配置与属性"),
                ("microsphere-mybatis-spring-cloud", "Spring Cloud 特性集成"),
                ("microsphere-mybatis-test / spring-test", "测试基础设施"),
                ("microsphere-mybatis-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x）")],
        ),
        versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.16"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.16")],
    ),
    dict(
        slug="microsphere-hibernate", name="Microsphere Hibernate", layer="integration",
        stars=0, forks=1, lang="Java", artifact="microsphere-hibernate-core",
        bom="microsphere-hibernate-dependencies", version="0.2.10",
        en=dict(
            tagline="Extensions for Hibernate ORM",
            summary="Provides Microsphere extensions for Hibernate ORM, covering both the Hibernate 6.2 – 7.3 and 5.0 – 5.6 lines.",
            features=[
                ("ORM extensions", "Core extension features for Hibernate ORM."),
                ("Testing framework", "A dedicated test support module for Hibernate ORM."),
                ("Broad version coverage", "0.2.x supports Hibernate 6.2 – 7.3; 0.1.x supports 5.0 – 5.6."),
            ],
            modules=[
                ("microsphere-hibernate-core", "Core extension features for Hibernate ORM"),
                ("microsphere-hibernate-test", "Testing framework for Hibernate ORM"),
                ("microsphere-hibernate-dependencies", "BOM"),
            ],
            compat=[("JDK", "17 – 25"), ("Hibernate Core", "6.2.x – 7.3.x (0.2.x) / 5.0.x – 5.6.x (0.1.x)")],
        ),
        zh=dict(
            tagline="Hibernate ORM 扩展",
            summary="为 Hibernate ORM 提供 Microsphere 扩展能力，覆盖 Hibernate 6.2 – 7.3 与 5.0 – 5.6 两条主要版本线。",
            features=[
                ("ORM 扩展", "提供 Hibernate ORM 的核心扩展特性。"),
                ("测试框架", "专门的 Hibernate ORM 测试支持模块。"),
                ("宽版本覆盖", "0.2.x 支持 Hibernate 6.2 – 7.3，0.1.x 支持 5.0 – 5.6。"),
            ],
            modules=[
                ("microsphere-hibernate-core", "Hibernate ORM 扩展核心特性"),
                ("microsphere-hibernate-test", "Hibernate ORM 测试框架"),
                ("microsphere-hibernate-dependencies", "BOM"),
            ],
            compat=[("JDK", "17 – 25"), ("Hibernate Core", "6.2.x – 7.3.x（0.2.x）/ 5.0.x – 5.6.x（0.1.x）")],
        ),
        versions=[("main", "Hibernate 6.2 – 7.3", "0.2.10"), ("1.x", "Hibernate 5.0 – 5.6", "0.1.10")],
    ),
    dict(
        slug="microsphere-alibaba-druid", name="Microsphere Alibaba Druid", layer="integration",
        stars=2, forks=3, lang="Java", artifact="microsphere-alibaba-druid-spring-cloud",
        bom="microsphere-alibaba-druid-dependencies", version="0.2.21",
        en=dict(
            tagline="SQL interception for the Druid connection pool",
            summary="Enhances Alibaba Druid, a high-performance JDBC connection pool, with fine-grained SQL statement "
                    "interception and logging. It serves as the interception foundation for Sentinel, Resilience4j, "
                    "Observability and other projects.",
            features=[
                ("SQL statement interception", "Intercepts SQL statements at execution time for downstream extensions."),
                ("SQL logging", "Fine-grained recording of SQL execution."),
                ("Full Spring stack", "Covers Spring Framework, Spring Boot auto-configuration and Spring Cloud discovery."),
                ("Ecosystem foundation", "Provides the interception entry point for Sentinel, Resilience4j and Observability."),
            ],
            modules=[
                ("microsphere-alibaba-druid-core", "Foundation classes and filters for Druid integration"),
                ("microsphere-alibaba-druid-spring", "Spring Framework integration and configuration"),
                ("microsphere-alibaba-druid-spring-boot", "Spring Boot auto-configuration and properties"),
                ("microsphere-alibaba-druid-spring-cloud", "Spring Cloud features and service discovery integration"),
                ("microsphere-alibaba-druid-test / spring-test", "Testing utilities"),
                ("microsphere-alibaba-druid-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x)")],
        ),
        zh=dict(
            tagline="为 Druid 连接池注入 SQL 拦截能力",
            summary="增强 Alibaba Druid 高性能 JDBC 连接池，提供细粒度的 SQL 语句拦截与日志能力，并作为 Sentinel、Resilience4j、"
                    "Observability 等项目的底层扩展支撑。",
            features=[
                ("SQL 语句拦截", "在执行阶段拦截 SQL 语句，供上下游项目扩展。"),
                ("SQL 日志记录", "细粒度记录 SQL 执行情况。"),
                ("Spring 全栈集成", "覆盖 Spring Framework、Spring Boot 自动配置、Spring Cloud 服务发现。"),
                ("生态底座", "为 Sentinel、Resilience4j、Observability 提供拦截入口。"),
            ],
            modules=[
                ("microsphere-alibaba-druid-core", "Druid 集成的基础类与过滤器"),
                ("microsphere-alibaba-druid-spring", "Spring Framework 集成与配置"),
                ("microsphere-alibaba-druid-spring-boot", "Spring Boot 自动配置与属性"),
                ("microsphere-alibaba-druid-spring-cloud", "Spring Cloud 特性与服务发现集成"),
                ("microsphere-alibaba-druid-test / spring-test", "测试工具"),
                ("microsphere-alibaba-druid-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x）")],
        ),
        versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.21"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.21")],
    ),
    dict(
        slug="microsphere-alibaba-sentinel", name="Microsphere Alibaba Sentinel", layer="integration",
        stars=2, forks=11, lang="Java", artifact="microsphere-alibaba-sentinel-commons",
        bom="microsphere-alibaba-sentinel-dependencies", version="0.2.5",
        en=dict(
            tagline="Flow control injected transparently into data, cache and web layers",
            summary="An abstraction layer that integrates Alibaba Sentinel's flow control framework with common Java "
                    "technologies, applying Sentinel's flow control, circuit breaking and system protection transparently "
                    "to database operations, caching and other infrastructure components.",
            features=[
                ("Web layer flow control", "Covers Spring WebMVC and Spring WebFlux."),
                ("Data access flow control", "Covers Alibaba Druid, Hibernate, MyBatis and P6Spy."),
                ("Cache layer flow control", "Covers Spring Data Redis."),
                ("Incremental adoption", "Both low-level integration APIs and high-level Spring Boot auto-configuration, so protection can be adopted step by step."),
            ],
            modules=[
                ("microsphere-alibaba-sentinel-commons", "Common features of the Sentinel extension"),
                ("microsphere-alibaba-sentinel-plugins", "Sentinel plugin collection"),
                ("microsphere-alibaba-sentinel-spring", "Alibaba Sentinel Spring integration"),
                ("microsphere-alibaba-sentinel-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x)")],
        ),
        zh=dict(
            tagline="把流控能力透明注入数据库、缓存与 Web",
            summary="在 Alibaba Sentinel 流控框架与常用 Java 技术之间建立无缝集成的抽象层，将 Sentinel 的流控、熔断与系统保护能力"
                    "透明地施加到数据库操作、缓存与其它基础设施组件上。",
            features=[
                ("Web 层流控", "覆盖 Spring WebMVC 与 Spring WebFlux。"),
                ("数据访问层流控", "覆盖 Alibaba Druid、Hibernate、MyBatis、P6Spy。"),
                ("缓存层流控", "覆盖 Spring Data Redis。"),
                ("渐进式接入", "同时提供底层集成 API 与 Spring Boot 高层自动配置，可按需逐步采用。"),
            ],
            modules=[
                ("microsphere-alibaba-sentinel-commons", "Sentinel 扩展通用特性"),
                ("microsphere-alibaba-sentinel-plugins", "Sentinel 插件集合"),
                ("microsphere-alibaba-sentinel-spring", "Alibaba Sentinel Spring 集成"),
                ("microsphere-alibaba-sentinel-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x）")],
        ),
        versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.5"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.5")],
    ),
    dict(
        slug="microsphere-resilience4j", name="Microsphere Resilience4j", layer="integration",
        stars=2, forks=9, lang="Java", artifact="microsphere-resilience4j-commons",
        bom="microsphere-resilience4j-dependencies", version="0.2.4",
        en=dict(
            tagline="A unified way to apply resilience patterns",
            summary="Extends Resilience4j so circuit breaker, bulkhead, rate limiter, retry and time limiter patterns can be "
                    "applied uniformly to Spring Web MVC applications, Feign API clients and database access via MyBatis "
                    "or JDBC with Druid and P6Spy.",
            features=[
                ("Web MVC resilience", "Resilience patterns for Spring Web MVC applications."),
                ("API client resilience", "Fault tolerance for Feign clients."),
                ("Database resilience", "Covers MyBatis and JDBC access on top of Druid and P6Spy."),
                ("Unified programming model", "A consistent Resilience4j integration across different technology stacks."),
            ],
            modules=[
                ("microsphere-resilience4j-commons", "Common features of the Resilience4j extension"),
                ("microsphere-resilience4j-plugins", "Resilience4j plugin collection"),
                ("microsphere-resilience4j-spring", "Resilience4j Spring integration"),
                ("microsphere-resilience4j-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x)"), ("Resilience4j", "2.0.0 – 2.4.0 (0.2.x) / 1.3.0 – 1.7.0 (0.1.x)")],
        ),
        zh=dict(
            tagline="统一的韧性模式落地方案",
            summary="扩展 Resilience4j，让熔断、隔板、限流、重试、超时等韧性模式能够以统一方式作用于 Spring Web MVC 应用、"
                    "Feign API 客户端以及数据库访问（MyBatis、JDBC + Druid + P6Spy）等不同场景。",
            features=[
                ("Web MVC 韧性", "为 Spring Web MVC 应用提供韧性模式支持。"),
                ("API 客户端韧性", "面向 Feign 客户端的容错能力。"),
                ("数据库访问韧性", "覆盖 MyBatis 以及 Druid、P6Spy 之上的 JDBC 访问。"),
                ("统一编程模型", "在不同技术栈上使用一致的 Resilience4j 接入方式。"),
            ],
            modules=[
                ("microsphere-resilience4j-commons", "Resilience4j 扩展通用特性"),
                ("microsphere-resilience4j-plugins", "Resilience4j 插件集合"),
                ("microsphere-resilience4j-spring", "Resilience4j Spring 集成"),
                ("microsphere-resilience4j-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x）"), ("Resilience4j", "2.0.0 – 2.4.0（0.2.x）/ 1.3.0 – 1.7.0（0.1.x）")],
        ),
        versions=[("main", "Resilience4j 2.0.0 – 2.4.0", "0.2.4"), ("1.x", "Resilience4j 1.3.0 – 1.7.0", "0.1.4")],
    ),
    dict(
        slug="microsphere-netflix", name="Microsphere Netflix", layer="integration",
        stars=2, forks=8, lang="Java", artifact="microsphere-netflix-eureka-client-spring-cloud",
        bom="microsphere-netflix-dependencies", version="0.2.0",
        en=dict(
            tagline="Highly available Eureka clusters and an enhanced client",
            summary="An enhanced integration framework for Netflix OSS components, focused on Eureka service discovery: "
                    "high-availability server clustering via Apache Tomcat, enhanced client metadata synchronisation and "
                    "multi-client management.",
            features=[
                ("Eureka server clustering", "High-availability Eureka Server clustering backed by Apache Tomcat."),
                ("Enhanced metadata sync", "Enhanced metadata synchronisation on top of the standard Eureka client."),
                ("Multiple client management", "Manage several Eureka clients within a single application."),
                ("Standalone core module", "eureka-client-core does not depend on Spring Cloud and can be used on its own."),
            ],
            modules=[
                ("microsphere-netflix-eureka-client-core", "Foundational Eureka client capabilities independent of Spring Cloud"),
                ("microsphere-netflix-eureka-client-spring-cloud", "Spring Cloud integration with enhanced features and multi-client support"),
                ("microsphere-netflix-eureka-server-spring-cloud", "High-availability Eureka server with Tomcat clustering"),
                ("microsphere-netflix-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x)")],
        ),
        zh=dict(
            tagline="Eureka 的高可用集群与增强客户端",
            summary="面向 Netflix OSS 组件的增强集成框架，聚焦 Eureka 服务发现：通过 Apache Tomcat 实现服务端高可用集群，"
                    "并增强客户端元数据同步与多客户端管理能力。",
            features=[
                ("Eureka 服务端集群", "基于 Apache Tomcat 的高可用 Eureka Server 集群能力。"),
                ("增强客户端元数据同步", "在标准 Eureka 客户端之上增强元数据同步。"),
                ("多客户端管理", "支持在同一应用内管理多个 Eureka 客户端。"),
                ("独立核心模块", "eureka-client-core 不依赖 Spring Cloud，可独立使用。"),
            ],
            modules=[
                ("microsphere-netflix-eureka-client-core", "不依赖 Spring Cloud 的基础 Eureka 客户端能力"),
                ("microsphere-netflix-eureka-client-spring-cloud", "Spring Cloud 集成，增强特性与多客户端支持"),
                ("microsphere-netflix-eureka-server-spring-cloud", "具备 Tomcat 集群能力的高可用 Eureka 服务端"),
                ("microsphere-netflix-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x）")],
        ),
        versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.0"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.0")],
    ),
    dict(
        slug="microsphere-nacos", name="Microsphere Nacos", layer="integration",
        stars=2, forks=6, lang="Java", artifact="microsphere-nacos",
        bom="microsphere-nacos-dependencies", version="0.2.0",
        en=dict(
            tagline="Alibaba Nacos integration",
            summary="A Microsphere integration project for Alibaba Nacos, working alongside the configuration management "
                    "and service discovery capabilities of the Spring Cloud ecosystem.",
            features=[
                ("Nacos integration", "Integration with Alibaba Nacos."),
                ("BOM management", "Unified versioning through the dependencies module."),
                ("Dual release lines", "main and 1.x branches maintained in parallel."),
            ],
            modules=[("microsphere-nacos-dependencies", "BOM centralising dependency management")],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x)")],
        ),
        zh=dict(
            tagline="Alibaba Nacos 集成",
            summary="面向 Alibaba Nacos 的 Microsphere 集成项目，与 Spring Cloud 生态中的配置管理和服务发现能力协同。",
            features=[
                ("Nacos 集成", "提供与 Alibaba Nacos 的集成能力。"),
                ("BOM 管理", "通过 dependencies 模块统一版本。"),
                ("双线维护", "main 与 1.x 分支并行维护。"),
            ],
            modules=[("microsphere-nacos-dependencies", "BOM，集中依赖管理")],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x）")],
        ),
        versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.0"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.0")],
    ),
    dict(
        slug="microsphere-dubbo", name="Microsphere Dubbo", layer="integration",
        stars=4, forks=7, lang="Java", artifact="microsphere-dubbo",
        en=dict(
            tagline="Apache Dubbo integration",
            summary="A Microsphere integration project for the Apache Dubbo RPC framework, bringing the ecosystem's "
                    "interception, observability and resilience capabilities into Dubbo call chains.",
            features=[
                ("Dubbo integration", "Integration with Apache Dubbo."),
                ("Ecosystem interop", "Combines with Observability, Sentinel and other capabilities."),
            ],
            modules=[("microsphere-dubbo", "Aggregator module for the Dubbo integration")],
            compat=[("Java", "8+")],
        ),
        zh=dict(
            tagline="Apache Dubbo 集成",
            summary="面向 Apache Dubbo RPC 框架的 Microsphere 集成项目，把生态中的拦截、可观测与容错能力带到 Dubbo 服务调用链路。",
            features=[
                ("Dubbo 集成", "提供与 Apache Dubbo 的集成能力。"),
                ("生态联动", "可与 Observability、Sentinel 等能力组合。"),
            ],
            modules=[("microsphere-dubbo", "Dubbo 集成聚合模块")],
            compat=[("Java", "8+")],
        ),
    ),
    dict(
        slug="microsphere-tomcat", name="Microsphere Tomcat", layer="integration",
        stars=2, forks=6, lang="Java", artifact="microsphere-tomcat",
        en=dict(
            tagline="Apache Tomcat integration",
            summary="An integration project for Apache Tomcat, supporting Tomcat dynamic configuration and lifecycle "
                    "management in scenarios such as Eureka server clustering and embedded test containers.",
            features=[
                ("Tomcat integration", "Integration with Apache Tomcat."),
                ("Dynamic configuration", "Works with the Tomcat dynamic configuration support in Spring Cloud fault tolerance utilities."),
            ],
            modules=[("microsphere-tomcat", "Aggregator module for the Tomcat integration")],
            compat=[("Java", "8+")],
        ),
        zh=dict(
            tagline="Apache Tomcat 集成",
            summary="面向 Apache Tomcat 的集成项目，支撑 Eureka 服务端集群、嵌入式测试容器等场景下的 Tomcat 动态配置与生命周期管理。",
            features=[
                ("Tomcat 集成", "提供与 Apache Tomcat 的集成能力。"),
                ("动态配置", "与 Spring Cloud 容错工具中的 Tomcat 动态配置能力协同。"),
            ],
            modules=[("microsphere-tomcat", "Tomcat 集成聚合模块")],
            compat=[("Java", "8+")],
        ),
    ),
    dict(
        slug="microsphere-etcd", name="Microsphere etcd", layer="integration",
        stars=0, forks=7, lang="Java", artifact="microsphere-etcd",
        en=dict(
            tagline="etcd integration",
            summary="A Microsphere integration project for the etcd distributed key-value store, usable as a backend for "
                    "configuration management and service discovery.",
            features=[("etcd integration", "Integration with etcd.")],
            modules=[("microsphere-etcd", "Aggregator module for the etcd integration")],
            compat=[("Java", "8+")],
        ),
        zh=dict(
            tagline="etcd 集成",
            summary="面向 etcd 分布式键值存储的 Microsphere 集成项目，可作为配置中心与服务发现的后端选项。",
            features=[("etcd 集成", "提供与 etcd 的集成能力。")],
            modules=[("microsphere-etcd", "etcd 集成聚合模块")],
            compat=[("Java", "8+")],
        ),
    ),
    # ---------------------------------------------------------------- L4
    dict(
        slug="microsphere-observability", name="Microsphere Observability", layer="crosscutting",
        stars=4, forks=8, lang="Java", artifact="microsphere-observability-metrics-micrometer",
        bom="microsphere-observability-dependencies", version="0.2.3",
        en=dict(
            tagline="Monitoring, metrics and logging in one suite",
            summary="Improves the monitoring, metrics collection and logging capabilities of Java applications, with a "
                    "primary focus on the Spring Boot ecosystem. Beyond dedicated integrations for Micrometer, Prometheus, "
                    "Log4j2 and Alibaba Sentinel, it ships custom metrics for system-level resources such as CGroups and "
                    "network statistics.",
            features=[
                ("Micrometer integration", "Custom MeterBinder implementations covering Sentinel, JDBC (P6Spy) and system metrics."),
                ("Prometheus bridge", "Custom Collectors convert Sentinel and other metrics into Prometheus format."),
                ("Logging abstraction", "The logging module provides core abstractions and dynamic layouts, including a lambda-friendly LoggerUtils."),
                ("Sentinel metrics", "Dedicated Sentinel metric logic and constants."),
                ("System-level metrics", "Collects CGroups, network statistics and other system resource metrics."),
                ("Single BOM entry point", "The dependencies module manages logging, micrometer, prometheus and all internal module versions."),
                ("OpenTelemetry alignment", "The parent POM imports the OpenTelemetry Instrumentation BOM."),
            ],
            modules=[
                ("microsphere-observability-logging", "Core logging abstraction and dynamic layouts, including a lambda-based LoggerUtils"),
                ("microsphere-observability-metrics-commons", "Foundational metric types and definitions"),
                ("microsphere-observability-metrics-alibaba-sentinel", "Sentinel-specific metric logic and constants"),
                ("microsphere-observability-metrics-micrometer", "Custom MeterBinders: Sentinel, JDBC (P6Spy), system metrics"),
                ("microsphere-observability-metrics-prometheus", "Prometheus Collector bridge"),
                ("microsphere-observability-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x)")],
        ),
        zh=dict(
            tagline="监控、指标与日志的一体化增强套件",
            summary="全面提升 Java 应用（以 Spring Boot 生态为主）的监控、指标采集与日志能力。除 Micrometer、Prometheus、Log4j2、"
                    "Alibaba Sentinel 的专项集成外，还提供 CGroups、网络统计等系统级自定义指标。",
            features=[
                ("Micrometer 集成", "自定义 MeterBinder 实现，覆盖 Sentinel、JDBC（P6Spy）与系统指标。"),
                ("Prometheus 桥接", "通过自定义 Collector 把 Sentinel 及其它指标转换为 Prometheus 格式。"),
                ("日志抽象", "logging 模块提供核心日志抽象与动态 layout，含支持 lambda 的 LoggerUtils。"),
                ("Sentinel 指标", "专门的 Sentinel 指标逻辑与常量定义。"),
                ("系统级指标", "采集 CGroups、网络统计等系统资源指标。"),
                ("BOM 统一入口", "dependencies 模块集中管理 logging、micrometer、prometheus 等所有内部模块版本。"),
                ("OpenTelemetry 对齐", "父 POM 导入 OpenTelemetry Instrumentation BOM。"),
            ],
            modules=[
                ("microsphere-observability-logging", "核心日志抽象与动态 layout，含 lambda 版 LoggerUtils"),
                ("microsphere-observability-metrics-commons", "基础指标类型与定义"),
                ("microsphere-observability-metrics-alibaba-sentinel", "Sentinel 专项指标逻辑与常量"),
                ("microsphere-observability-metrics-micrometer", "自定义 MeterBinder：Sentinel、JDBC(P6Spy)、系统指标"),
                ("microsphere-observability-metrics-prometheus", "Prometheus Collector 桥接"),
                ("microsphere-observability-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x）")],
        ),
        versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.3"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.3")],
    ),
    dict(
        slug="microsphere-i18n", name="Microsphere i18n", layer="crosscutting",
        stars=13, forks=18, lang="Java", artifact="microsphere-i18n-core",
        bom="microsphere-i18n-dependencies", version="0.2.21",
        en=dict(
            tagline="A layered internationalisation framework for microservices",
            summary="A comprehensive i18n framework for Java applications with deep Spring integration. Its modular, "
                    "extensible architecture manages localised messages across deployment scenarios ranging from standalone "
                    "Spring applications to distributed, cloud-native microservices.",
            features=[
                ("Layered message sources", "Load localised messages from classpath properties files, the Spring Environment or external configuration systems through a unified ServiceMessageSource abstraction."),
                ("Composite sources with priority", "CompositeServiceMessageSource combines multiple sources; higher-priority sources shadow lower-priority ones."),
                ("Dynamic configuration", "Spring Cloud integration enables runtime message updates without restarting the application."),
                ("Spring MessageSource bridge", "The primary ServiceMessageSource bean is exposed as Spring's MessageSource, working transparently with @Value, Thymeleaf and more."),
                ("Bean Validation integration", "An i18n-aware LocalValidatorFactoryBean translates constraint violation messages through the same source."),
                ("OpenFeign propagation", "An Accept-Language request interceptor forwards the current locale to downstream Feign clients."),
                ("Actuator endpoint", "Read and write i18n messages at runtime through /actuator/i18n."),
                ("Centralised i18n server", "A dedicated Spring Cloud server module serves consolidated message bundles across microservices."),
            ],
            modules=[
                ("microsphere-i18n-core", "Fundamental i18n abstractions and message source implementations"),
                ("microsphere-i18n-spring", "Integration with Spring's MessageSource and Environment"),
                ("microsphere-i18n-spring-boot", "Auto-configuration and Actuator endpoint"),
                ("microsphere-i18n-spring-cloud", "Dynamic configuration updates via Spring Cloud Config"),
                ("microsphere-i18n-spring-cloud-server", "Centralised i18n management server"),
                ("microsphere-i18n-openfeign", "Propagates the current locale to OpenFeign clients"),
                ("microsphere-i18n-dependencies", "BOM"),
            ],
            compat=[("Java", "17+"), ("Spring Framework", "6.x"), ("Spring Boot", "3.x"), ("Spring Cloud", "2022.0.x – 2025.0.x")],
        ),
        zh=dict(
            tagline="面向微服务的分层国际化框架",
            summary="一套完整的 Java 国际化框架，并与 Spring 生态深度集成。它提供模块化、可扩展的架构来管理本地化消息，"
                    "覆盖从独立 Spring 应用到分布式云原生微服务的各类部署形态。",
            features=[
                ("分层消息源", "通过统一的 ServiceMessageSource 抽象，从 classpath 属性文件、Spring Environment 或外部配置系统加载本地化消息。"),
                ("带优先级的组合源", "CompositeServiceMessageSource 组合多个消息源，高优先级源遮蔽低优先级源。"),
                ("动态配置", "与 Spring Cloud 集成，运行时更新消息而无需重启应用。"),
                ("Spring MessageSource 桥接", "主 ServiceMessageSource Bean 自动暴露为 Spring 的 MessageSource，与 @Value、Thymeleaf 等无缝协作。"),
                ("Bean Validation 集成", "i18n 感知的 LocalValidatorFactoryBean，经同一消息源翻译约束违规信息。"),
                ("OpenFeign 传播", "Accept-Language 请求拦截器自动把当前 Locale 转发给下游 Feign 客户端。"),
                ("Actuator 端点", "通过 /actuator/i18n 在运行时读写 i18n 消息。"),
                ("集中式 i18n 服务", "通过专门的 Spring Cloud Server 模块跨微服务统一提供消息包。"),
            ],
            modules=[
                ("microsphere-i18n-core", "基础 i18n 抽象与消息源实现"),
                ("microsphere-i18n-spring", "与 Spring Framework 的 MessageSource 和 Environment 集成"),
                ("microsphere-i18n-spring-boot", "自动配置与 Actuator 端点"),
                ("microsphere-i18n-spring-cloud", "基于 Spring Cloud Config 的动态配置更新"),
                ("microsphere-i18n-spring-cloud-server", "集中式 i18n 管理服务"),
                ("microsphere-i18n-openfeign", "向 OpenFeign 客户端传播当前 Locale"),
                ("microsphere-i18n-dependencies", "BOM"),
            ],
            compat=[("Java", "17+"), ("Spring Framework", "6.x"), ("Spring Boot", "3.x"), ("Spring Cloud", "2022.0.x – 2025.0.x")],
        ),
        versions=[("main", "2022.0.x – 2025.0.x", "0.2.21"), ("1.x", "Hoxton – 2021.0.x", "0.1.21")],
    ),
    dict(
        slug="microsphere-multiactive", name="Microsphere Multiactive", layer="crosscutting",
        stars=4, forks=14, lang="Java", artifact="microsphere-multiactive-commons",
        bom="microsphere-multiactive-dependencies", version="0.2.13",
        en=dict(
            tagline="Zone-aware routing for multi-active deployments",
            summary="A comprehensive framework for implementing multi-active, zone-aware deployments in distributed "
                    "applications. Applications discover their own deployment zone and route intelligently — preferring "
                    "same-zone instances while providing cross-zone fallback.",
            features=[
                ("Automatic zone discovery", "Applications identify the deployment zone they belong to."),
                ("Same-zone preference", "Prefers same-zone instances with graceful fallback for cross-zone scenarios."),
                ("Cloud and middleware adapters", "Modules for AWS zone discovery and Netflix OSS integration."),
                ("Full Spring stack", "Covers Spring Framework, Spring Boot and Spring Cloud integration levels."),
            ],
            modules=[
                ("microsphere-multiactive-commons", "Core zone management abstractions"),
                ("microsphere-multiactive-aws", "AWS zone discovery"),
                ("microsphere-multiactive-netflix", "Netflix OSS integration"),
                ("microsphere-multiactive-spring", "Spring Framework integration"),
                ("microsphere-multiactive-spring-boot", "Spring Boot integration"),
                ("microsphere-multiactive-spring-cloud", "Spring Cloud integration"),
                ("microsphere-multiactive-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x (main) / Hoxton – 2021.0.x (1.x)")],
        ),
        zh=dict(
            tagline="多活与单元化部署的分区感知框架",
            summary="面向分布式应用的多活（multi-active）分区感知部署综合框架。应用可自动发现自身所处的部署分区，"
                    "并实现优先同区调用、跨区兜底的智能路由。",
            features=[
                ("分区自动发现", "应用自动识别自身所属的部署 zone。"),
                ("同区优先路由", "优先选择同区实例，并在跨区场景提供降级兜底能力。"),
                ("多云与中间件适配", "提供 AWS 分区发现与 Netflix OSS 集成模块。"),
                ("全栈 Spring 支持", "覆盖 Spring Framework、Spring Boot 与 Spring Cloud 三个集成层级。"),
            ],
            modules=[
                ("microsphere-multiactive-commons", "核心分区管理抽象"),
                ("microsphere-multiactive-aws", "AWS 分区发现"),
                ("microsphere-multiactive-netflix", "Netflix OSS 集成"),
                ("microsphere-multiactive-spring", "Spring Framework 集成"),
                ("microsphere-multiactive-spring-boot", "Spring Boot 集成"),
                ("microsphere-multiactive-spring-cloud", "Spring Cloud 集成"),
                ("microsphere-multiactive-dependencies", "BOM"),
            ],
            compat=[("Spring Cloud", "2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x）")],
        ),
        versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.13"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.13")],
    ),
    dict(
        slug="microsphere-security", name="Microsphere Security", layer="crosscutting",
        stars=3, forks=6, lang="Java", artifact="microsphere-security",
        en=dict(
            tagline="Security capability extensions",
            summary="Provides security-related extensions for the Microsphere ecosystem, working alongside Spring Security "
                    "and the ecosystem's interception mechanisms.",
            features=[("Security extensions", "Security capability extensions for the ecosystem.")],
            modules=[("microsphere-security", "Aggregator module for the security extensions")],
            compat=[("Java", "8+")],
        ),
        zh=dict(
            tagline="安全能力扩展",
            summary="为 Microsphere 生态提供安全相关的扩展能力，与 Spring Security 及生态内的拦截机制协同工作。",
            features=[("安全扩展", "提供面向生态的安全能力扩展。")],
            modules=[("microsphere-security", "安全扩展聚合模块")],
            compat=[("Java", "8+")],
        ),
    ),
    dict(
        slug="microsphere-dynamic", name="Microsphere Dynamic", layer="crosscutting",
        stars=3, forks=7, lang="Java", artifact="microsphere-dynamic",
        en=dict(
            tagline="Infrastructure for runtime dynamism",
            summary="Provides the dynamism foundation for the ecosystem, supporting restart-free change scenarios such as "
                    "runtime configuration refresh and hot updates of Feign components.",
            features=[("Dynamic foundation", "Infrastructure for runtime dynamic changes.")],
            modules=[("microsphere-dynamic", "Aggregator module for dynamic capabilities")],
            compat=[("Java", "8+")],
        ),
        zh=dict(
            tagline="动态化能力支撑",
            summary="为生态提供动态化基础能力，支撑运行时配置刷新、Feign 组件热更新等免重启变更场景。",
            features=[("动态化支撑", "为运行时动态变更提供基础设施。")],
            modules=[("microsphere-dynamic", "动态化能力聚合模块")],
            compat=[("Java", "8+")],
        ),
    ),
    dict(
        slug="microsphere-configuration", name="Microsphere Configuration", layer="crosscutting",
        stars=2, forks=10, lang="Java", artifact="microsphere-configuration",
        en=dict(
            tagline="Configuration system enhancements",
            summary="Enhancements around the configuration system, working with the Spring Environment, "
                    "@ConfigurationProperties and Spring Cloud configuration refresh mechanisms.",
            features=[("Configuration enhancements", "Enhancements for the configuration system.")],
            modules=[("microsphere-configuration", "Aggregator module for configuration enhancements")],
            compat=[("Java", "8+")],
        ),
        zh=dict(
            tagline="配置体系增强",
            summary="围绕配置体系提供增强能力，与 Spring Environment、@ConfigurationProperties 以及 Spring Cloud 配置刷新机制协同。",
            features=[("配置增强", "提供配置体系相关的增强能力。")],
            modules=[("microsphere-configuration", "配置增强聚合模块")],
            compat=[("Java", "8+")],
        ),
    ),
    dict(
        slug="microsphere-ai", name="Microsphere AI", layer="crosscutting",
        stars=0, forks=1, lang="Java", artifact="microsphere-ai",
        en=dict(
            tagline="An exploratory project for AI scenarios",
            summary="Microsphere's exploratory track in artificial intelligence, investigating how ecosystem capabilities "
                    "extend into AI application scenarios.",
            features=[("AI exploration", "Exploration of capabilities for AI application scenarios.")],
            modules=[("microsphere-ai", "Aggregator module for AI capabilities")],
            compat=[("Java", "17+")],
        ),
        zh=dict(
            tagline="面向 AI 场景的探索项目",
            summary="Microsphere 在人工智能方向的探索性项目，探索生态能力在 AI 应用场景中的延展。",
            features=[("AI 场景探索", "面向 AI 应用场景的能力探索。")],
            modules=[("microsphere-ai", "AI 能力聚合模块")],
            compat=[("Java", "17+")],
        ),
    ),
    dict(
        slug="microsphere-devops", name="Microsphere DevOps", layer="crosscutting",
        stars=5, forks=6, lang="Shell", artifact=None,
        en=dict(
            tagline="Engineering efficiency and operations support",
            summary="Carries the DevOps capabilities of the ecosystem, covering build, release and environment management, "
                    "with a companion TypeScript UI project.",
            features=[
                ("Engineering efficiency", "Supports the continuous integration and delivery flows of the ecosystem."),
                ("Companion UI", "microsphere-devops-ui (TypeScript) provides a visual interface."),
            ],
            modules=[("microsphere-devops", "DevOps scripts and configuration"), ("microsphere-devops-ui", "DevOps UI written in TypeScript")],
            compat=[("Node", "18+ (devops-ui)")],
        ),
        zh=dict(
            tagline="生态的工程效能与运维支撑",
            summary="承载 Microsphere 生态的 DevOps 能力，覆盖构建、发布与环境管理等工程效能环节，并配套独立的 UI 项目。",
            features=[
                ("工程效能", "支撑生态的持续集成与交付流程。"),
                ("配套 UI", "由 microsphere-devops-ui（TypeScript）提供可视化界面。"),
            ],
            modules=[("microsphere-devops", "DevOps 脚本与配置"), ("microsphere-devops-ui", "TypeScript 编写的 DevOps UI")],
            compat=[("Node", "18+（devops-ui）")],
        ),
    ),
]
