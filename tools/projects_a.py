# -*- coding: utf-8 -*-
"""Bilingual project data — part A: L0 Foundation, L1 Runtime, L2 Framework.

Every user-facing string is a {"en": ..., "zh": ...} pair.
Source of truth: each repository's README on GitHub.
"""

LAYERS = [
    dict(
        id="foundation", en="L0 · Foundation", zh="L0 · 工程基座",
        en_desc="Unified build and dependency governance. The Maven parent POM and BOM that keep all 36 repositories on one baseline.",
        zh_desc="统一构建与依赖治理。所有子项目的 Maven 父 POM 与 BOM 在这里定义，保证 36 个仓库的构建口径一致。",
    ),
    dict(
        id="runtime", en="L1 · Runtime", zh="L1 · 运行时基座",
        en_desc="Framework-free Java capabilities: strings and collections, reflection, type conversion, events, logging abstraction, plus Java / Jakarta EE implementations.",
        zh_desc="不依赖任何框架的纯 Java 能力层：字符串与集合、反射、类型转换、事件、日志抽象、Java / Jakarta EE 实现。",
    ),
    dict(
        id="framework", en="L2 · Framework", zh="L2 · 框架扩展",
        en_desc="Enhancements for Spring, Spring Boot and Spring Cloud — the most central layer of the ecosystem.",
        zh_desc="对 Spring、Spring Boot、Spring Cloud 的增强扩展，是整个生态最核心的一层。",
    ),
    dict(
        id="integration", en="L3 · Integration", zh="L3 · 生态集成",
        en_desc="Adapters for concrete infrastructure: service registries, data access, caching, RPC, resilience and gateways.",
        zh_desc="面向具体基础设施的适配层：注册中心、数据访问、缓存、RPC、容错、网关。",
    ),
    dict(
        id="crosscutting", en="L4 · Cross-cutting", zh="L4 · 横向能力",
        en_desc="Capabilities that cut across every layer: observability, internationalisation, security, dynamic configuration and multi-active routing.",
        zh_desc="贯穿所有层的可观测性、国际化、安全、动态配置、单元化多活等能力。",
    ),
]

PROJECTS = [
    # ---------------------------------------------------------------- L0
    dict(
        slug="microsphere-build", name="Microsphere Build", layer="foundation",
        stars=8, forks=29, lang="Maven", artifact="microsphere-build",
        en=dict(
            tagline="The shared Maven parent POM for the whole ecosystem",
            summary="Supplies unified build settings and plugin configuration inherited by every Microsphere sub-project, "
                    "including Microsphere Java and Microsphere Spring. Multi-TLS compilation, release signing, coverage "
                    "and documentation generation are all centralised here, so each repository only carries business code.",
            features=[
                ("Multi-TLS language support", "A single POM builds against Java 8, 11, 17, 21 and 25."),
                ("Centralised plugin management", "Locks Compiler, Source and Flatten plugin versions so no repository drifts."),
                ("Profile governance", "Six built-in profiles: publish, release, ci, test, coverage and docs, activated on demand."),
                ("Unified publishing channel", "The publish profile integrates the Central Publishing plugin for the new Maven Central portal."),
            ],
            modules=[
                ("Maven Compiler Plugin", "3.16.0 — compilation across multiple Java TLS versions"),
                ("Maven Source Plugin", "3.4.0 — generates source jars"),
                ("Flatten Maven Plugin", "1.7.3 — flattens POMs for publishing"),
                ("Maven JavaDoc Plugin", "3.12.0 — publish / release profile"),
                ("Maven GPG Plugin", "3.2.8 — artifact signing"),
                ("Git Commit Id Plugin", "4.9.10 — injects Git metadata"),
                ("JaCoCo Plugin", "0.8.15 — coverage profile"),
                ("Asciidoctor / Docbkx", "documentation generation under the docs profile"),
            ],
            compat=[("Java", "8 / 11 / 17 / 21 / 25"), ("Maven", "3.6+")],
            note="Since 0.2.0 the publish profile is the recommended path: OSSRH reached end of life on 2025-06-30 "
                 "and every namespace migrated to the Central Publisher Portal.",
        ),
        zh=dict(
            tagline="Microsphere 全系项目的 Maven 父 POM",
            summary="提供统一的构建设置与插件配置，被 Microsphere Java、Microsphere Spring 等所有子项目继承。"
                    "它把 Java 多 TLS 版本编译、发布签名、覆盖率、文档生成等能力收敛到一处，让各子仓库只关心业务代码。",
            features=[
                ("语言版本支持", "同一份 POM 覆盖 Java 8、11、17、21、25 五个 TLS 版本的构建。"),
                ("插件集中管理", "统一锁定 Compiler、Source、Flatten 等默认插件版本，避免各仓库版本漂移。"),
                ("Profile 治理", "内置 publish、release、ci、test、coverage、docs 六套 profile，按需激活。"),
                ("统一发布通道", "publish profile 集成 Central Publishing 插件，对接 Maven Central 新发布门户。"),
            ],
            modules=[
                ("Maven Compiler Plugin", "3.16.0 — 编译，支持多 Java TLS 版本"),
                ("Maven Source Plugin", "3.4.0 — 生成源码 jar"),
                ("Flatten Maven Plugin", "1.7.3 — 扁平化 POM 以便发布"),
                ("Maven JavaDoc Plugin", "3.12.0 — publish / release profile"),
                ("Maven GPG Plugin", "3.2.8 — 制品签名"),
                ("Git Commit Id Plugin", "4.9.10 — 注入 Git 元信息"),
                ("JaCoCo Plugin", "0.8.15 — coverage profile"),
                ("Asciidoctor / Docbkx", "docs profile 下的文档生成"),
            ],
            compat=[("Java", "8 / 11 / 17 / 21 / 25"), ("Maven", "3.6+")],
            note="自 0.2.0 起推荐使用 publish profile：OSSRH 已于 2025-06-30 下线，命名空间全部迁移至 Central Publisher Portal。",
        ),
    ),
    dict(
        slug="microsphere-bom", name="Microsphere BOM", layer="foundation",
        stars=0, forks=1, lang="Maven", artifact="microsphere-bom",
        en=dict(
            tagline="A cross-project Maven bill of materials",
            summary="Declares the versions of every Microsphere module in one place. Import it once to align all "
                    "dependency versions and avoid conflicts across modules.",
            features=[
                ("Single point of version alignment", "No need to declare a version for each module after importing the BOM."),
                ("Cross-repository consistency", "Kept in sync with each sub-project's own dependencies module."),
                ("Works with Build", "Pairs with the microsphere-build parent POM for a single build and dependency baseline."),
            ],
            modules=[("microsphere-bom", "Top-level BOM aggregating every sub-project version")],
            compat=[("Java", "8+"), ("Maven", "3.6+")],
        ),
        zh=dict(
            tagline="跨项目的 Maven 物料清单",
            summary="集中声明 Microsphere 生态各模块的版本，使用者导入一次即可对齐全部依赖版本，避免多模块之间的版本冲突。",
            features=[
                ("单点版本对齐", "导入 BOM 后无需为每个模块指定 `<version>`。"),
                ("跨仓库一致性", "与各子项目的 dependencies 模块保持版本同步。"),
                ("与 Build 协同", "配合 microsphere-build 父 POM 使用，构建与依赖口径统一。"),
            ],
            modules=[("microsphere-bom", "顶层 BOM，聚合各子项目版本")],
            compat=[("Java", "8+"), ("Maven", "3.6+")],
        ),
    ),
    # ---------------------------------------------------------------- L1
    dict(
        slug="microsphere-java", name="Microsphere Java", layer="runtime",
        stars=104, forks=52, lang="Java", artifact="microsphere-java-core",
        bom="microsphere-java-dependencies", version="0.2.x",
        en=dict(
            tagline="The foundation of the ecosystem: reusable Java components and utilities",
            summary="Microsphere Java Framework is the backbone of the Microsphere ecosystem. Built purely on standard "
                    "Java APIs, it ships a complete set of reusable components covering strings, collections, reflection, "
                    "type conversion, event dispatching, class loading and artifact detection, networking, I/O and "
                    "concurrency — plus a compile-time annotation processor. Every other sub-project builds on top of it.",
            features=[
                ("String & Collection Utilities", "Null-safe helpers for strings, arrays, lists, sets, maps and deques."),
                ("Reflection Utilities", "Simplified access to fields, methods, constructors and generic type arguments."),
                ("Type Conversion", "An extensible Converter SPI with built-in converters for primitives, collections, Duration, InputStream and more."),
                ("Event Dispatching", "A lightweight EventDispatcher with sequential (direct) and parallel execution modes."),
                ("Class Loading & Artifact Detection", "Classpath scanning, JAR introspection and Maven/module artifact resolution, including runtime version detection from JAR manifests."),
                ("Networking & I/O", "A custom URLStreamHandler and URL helpers, plus enhanced file, stream and charset utilities with a file-watch service."),
                ("Concurrency", "Delegating executor wrappers and a custom ThreadFactory."),
                ("Configuration Properties", "SPI-based property loading with annotation-driven metadata generation."),
                ("Compile-time Annotation Processing", "An annotation processor that generates metadata for @ConfigurationProperty."),
                ("Language Model & JDK Tools", "Components for the Java Language Model API, plus helpers bridging the compiler and annotation-processing tool APIs."),
                ("Testing Support", "Base classes and utilities for JUnit 5-based unit tests."),
            ],
            modules=[
                ("microsphere-java-annotations", "Common annotations: @Nullable, @Nonnull, @Immutable, @Experimental, @Since"),
                ("microsphere-java-core", "Core utilities: strings, collections, reflection, I/O, concurrency, events, type conversion"),
                ("microsphere-lang-model", "Components and utilities for the Java Language Model API"),
                ("microsphere-jdk-tools", "Helpers for the Java compiler and JDK tool APIs"),
                ("microsphere-annotation-processor", "Compile-time processor generating @ConfigurationProperty metadata"),
                ("microsphere-java-test", "Models and utilities for JUnit 5-based testing"),
                ("microsphere-java-dependencies", "BOM managing dependency versions"),
                ("microsphere-java-parent", "Parent POM with shared build configuration"),
            ],
            compat=[("Java", "8 / 11 / 17 / 21 / 25 (all in CI)"), ("Maven", "3.6+")],
        ),
        zh=dict(
            tagline="整个生态的地基：可复用的 Java 组件与工具集",
            summary="Microsphere Java Framework 是 Microsphere 生态的骨干基础库。它基于标准 Java API 提供字符串、集合、反射、"
                    "类型转换、事件分发、类加载与制品探测、网络、I/O、并发等一整套可复用组件，并内置编译期注解处理器。"
                    "所有其它子项目都构建在它之上。",
            features=[
                ("字符串与集合工具", "对字符串、数组、List、Set、Map、Deque 的空安全（null-safe）辅助方法。"),
                ("反射工具", "简化字段、方法、构造器以及泛型实参的访问，免去大量样板代码。"),
                ("类型转换", "可扩展的 Converter SPI，内置基础类型、集合、Duration、InputStream 等转换器。"),
                ("事件分发", "轻量 EventDispatcher，支持顺序（direct）与并行（parallel）两种执行模式。"),
                ("类加载与制品探测", "类路径扫描、JAR 内省、Maven / 模块制品解析，支持从 JAR manifest 推断运行时版本。"),
                ("网络与 I/O", "自定义 URLStreamHandler 与 URL 工具；增强的文件、流、字符集工具以及文件监听服务。"),
                ("并发", "委派式 Executor 包装器与自定义 ThreadFactory。"),
                ("配置属性", "基于 SPI 的属性加载，配合注解驱动的元数据生成。"),
                ("编译期注解处理", "为 @ConfigurationProperty 生成元数据的 Annotation Processor。"),
                ("语言模型与 JDK Tools", "面向 javax.lang.model 的组件，以及桥接 Java 编译器与注解处理工具 API 的辅助类。"),
                ("测试支持", "面向 JUnit 5 的基类与工具。"),
            ],
            modules=[
                ("microsphere-java-annotations", "通用注解：@Nullable、@Nonnull、@Immutable、@Experimental、@Since"),
                ("microsphere-java-core", "核心工具：字符串、集合、反射、I/O、并发、事件、类型转换"),
                ("microsphere-lang-model", "Java 语言模型 API 的组件与工具"),
                ("microsphere-jdk-tools", "Java 编译器与 JDK 工具 API 辅助"),
                ("microsphere-annotation-processor", "@ConfigurationProperty 元数据的编译期处理器"),
                ("microsphere-java-test", "基于 JUnit 5 的测试模型与工具"),
                ("microsphere-java-dependencies", "BOM，统一管理依赖版本"),
                ("microsphere-java-parent", "父 POM，共享构建配置"),
            ],
            compat=[("Java", "8 / 11 / 17 / 21 / 25（CI 全覆盖）"), ("Maven", "3.6+")],
        ),
        code="""import io.microsphere.util.StringUtils;
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
boolean modern = v.isGreaterThanOrEqualTo("6.0.0");""",
        lang_code="java",
    ),
    dict(
        slug="microsphere-logging", name="Microsphere Logging", layer="runtime",
        stars=2, forks=1, lang="Java", artifact="microsphere-logging-commons",
        bom="microsphere-logging-dependencies",
        en=dict(
            tagline="One abstraction layer for runtime logging management",
            summary="Manage logging configuration across a JVM without touching application code or restarting services. "
                    "It auto-loads the highest-priority Logging implementation via SPI and supports JUL, Log4j, Log4j2 "
                    "and Logback coexisting in the same process.",
            features=[
                ("Runtime level management", "Adjust log levels in production without restarting the service."),
                ("Framework-agnostic API", "Write management code once; it works across every supported backend."),
                ("JMX integration", "Expose and control logging configuration through JMX for operations teams."),
                ("Testing support", "JUnit 4 and JUnit Jupiter 5 extensions to verify behaviour across multiple log levels."),
                ("SPI-based extensibility", "Load the highest-priority Logging implementation automatically via Java ServiceLoader."),
                ("Multi-backend coexistence", "Use several logging backends in one JVM with priority-based resolution."),
            ],
            modules=[
                ("microsphere-logging-commons", "Core API: Logging interface, LoggingUtils, JMX support"),
                ("microsphere-java-logging", "Java Logging (JUL) extension"),
                ("microsphere-logback", "Logback extension"),
                ("microsphere-log4j", "Log4j extension"),
                ("microsphere-log4j2", "Log4j2 extension"),
                ("microsphere-logging-test", "JUnit 4 / JUnit Jupiter 5 test extensions"),
                ("microsphere-logging-examples", "Runnable examples"),
            ],
            compat=[("Java", "8+"), ("SLF4J", "1.7+"), ("Log4j", "1.2+"), ("Logback", "1.2+"), ("Log4j2", "2.4+")],
        ),
        zh=dict(
            tagline="跨日志框架的统一运行时管理抽象层",
            summary="在不改动应用代码、不重启服务的前提下，统一管理 JVM 中的日志配置。它通过 SPI 自动装载优先级最高的 "
                    "Logging 实现，同时支持 JUL、Log4j、Log4j2、Logback 多后端共存。",
            features=[
                ("运行时级别调整", "生产环境动态调整日志级别，无需重启服务。"),
                ("框架无关 API", "管理代码只写一次，跨全部受支持后端生效。"),
                ("JMX 集成", "通过 JMX 暴露并操控日志配置，方便运维介入。"),
                ("测试支持", "提供 JUnit 4 与 JUnit Jupiter 5 扩展，可在多级别下验证日志行为。"),
                ("SPI 可扩展", "通过 Java ServiceLoader 自动加载最高优先级的 Logging 实现。"),
                ("多后端共存", "同一 JVM 内可并行使用多个日志后端，按优先级解析。"),
            ],
            modules=[
                ("microsphere-logging-commons", "核心 API：Logging 接口、LoggingUtils、JMX 支持"),
                ("microsphere-java-logging", "Java Logging（JUL）扩展"),
                ("microsphere-logback", "Logback 扩展"),
                ("microsphere-log4j", "Log4j 扩展"),
                ("microsphere-log4j2", "Log4j2 扩展"),
                ("microsphere-logging-test", "JUnit 4 / JUnit Jupiter 5 测试扩展"),
                ("microsphere-logging-examples", "可运行示例"),
            ],
            compat=[("Java", "8+"), ("SLF4J", "1.7+"), ("Log4j", "1.2+"), ("Logback", "1.2+"), ("Log4j2", "2.4+")],
        ),
    ),
    dict(
        slug="microsphere-java-enterprise", name="Microsphere Java EE", layer="runtime",
        stars=14, forks=18, lang="Java", artifact="microsphere-java-enterprise",
        en=dict(
            tagline="Microsphere's implementation of the Java EE specifications",
            summary="Implements the Java EE (pre-Jakarta) specifications the Microsphere way, offering a programming "
                    "model consistent with the rest of the ecosystem for teams that need standardised enterprise APIs.",
            features=[
                ("Specification implementations", "Provides implementation modules for the corresponding Java EE specifications."),
                ("Ecosystem consistency", "Reuses the reflection, type conversion and event capabilities of Microsphere Java."),
                ("Parallel with the Jakarta line", "Forms a dual EE / Jakarta support track together with microsphere-jakarta."),
            ],
            modules=[("microsphere-java-enterprise", "Aggregator module for the Java EE implementations")],
            compat=[("Java", "8+")],
        ),
        zh=dict(
            tagline="Java EE 规范的 Microsphere 实现",
            summary="以 Microsphere 的方式实现 Java EE（Jakarta EE 前身）规范，为需要标准化企业 API 的场景提供与生态一致的编程模型。",
            features=[
                ("规范实现", "按 Java EE 规范提供对应实现模块。"),
                ("生态一致性", "复用 Microsphere Java 的反射、类型转换与事件能力。"),
                ("与 Jakarta 分支并行", "与 microsphere-jakarta 形成 EE / Jakarta 双线支持。"),
            ],
            modules=[("microsphere-java-enterprise", "Java EE 规范实现聚合模块")],
            compat=[("Java", "8+")],
        ),
    ),
    dict(
        slug="microsphere-jakarta", name="Microsphere Jakarta", layer="runtime",
        stars=2, forks=6, lang="Java", artifact="microsphere-jakarta",
        en=dict(
            tagline="Microsphere's implementation of the Jakarta EE specifications",
            summary="An implementation track targeting the Jakarta EE namespace (jakarta.*), for enterprise applications "
                    "that have completed the migration away from Java EE.",
            features=[
                ("Jakarta namespace", "Fully adapted to the jakarta.* package namespace."),
                ("Aligned with Spring 6/7", "Matches the Jakarta baseline adopted by Spring Framework 6 and later."),
            ],
            modules=[("microsphere-jakarta", "Aggregator module for the Jakarta EE implementations")],
            compat=[("Java", "17+")],
        ),
        zh=dict(
            tagline="Jakarta EE 规范的 Microsphere 实现",
            summary="面向 Jakarta EE 命名空间（jakarta.*）的实现分支，适配从 Java EE 迁移后的企业应用。",
            features=[
                ("Jakarta 命名空间", "全面适配 jakarta.* 包名。"),
                ("与 Spring 6/7 对齐", "匹配 Spring Framework 6+ 采用的 Jakarta 基线。"),
            ],
            modules=[("microsphere-jakarta", "Jakarta EE 实现聚合模块")],
            compat=[("Java", "17+")],
        ),
    ),
    dict(
        slug="microsphere-microprofile", name="Microsphere MicroProfile", layer="runtime",
        stars=1, forks=6, lang="Java", artifact="microsphere-microprofile",
        en=dict(
            tagline="Eclipse MicroProfile support",
            summary="Provides Microsphere implementations of the MicroProfile specifications, targeting the standardised "
                    "configuration, fault tolerance and metrics requirements of cloud-native microservices.",
            features=[
                ("MicroProfile specifications", "Covers MicroProfile configuration, fault tolerance, health checks and more."),
                ("Microservice oriented", "Complements the multi-registry capabilities of Microsphere Spring Cloud."),
            ],
            modules=[("microsphere-microprofile", "Aggregator module for the MicroProfile implementations")],
            compat=[("Java", "8+")],
        ),
        zh=dict(
            tagline="Eclipse MicroProfile 支持",
            summary="为 MicroProfile 规范提供 Microsphere 实现，面向云原生微服务的配置、容错、指标等标准化需求。",
            features=[
                ("MicroProfile 规范", "覆盖配置、容错、健康检查等 MicroProfile 能力。"),
                ("微服务友好", "与 Microsphere Spring Cloud 的多注册中心能力互补。"),
            ],
            modules=[("microsphere-microprofile", "MicroProfile 实现聚合模块")],
            compat=[("Java", "8+")],
        ),
    ),
    dict(
        slug="microsphere-tools", name="Microsphere Tools", layer="runtime",
        stars=0, forks=5, lang="Java", artifact="microsphere-tools",
        en=dict(
            tagline="Shared development tooling",
            summary="Collects the utilities repeatedly used across the ecosystem during day-to-day development and "
                    "operations, shared by every sub-project.",
            features=[("Tool reuse", "A single home for utilities shared across projects.")],
            modules=[("microsphere-tools", "Aggregator module for shared utilities")],
            compat=[("Java", "8+")],
        ),
        zh=dict(
            tagline="通用研发工具集",
            summary="沉淀 Microsphere 生态在日常开发与运维中反复使用的工具类，供各子项目共享。",
            features=[("工具复用", "集中收纳跨项目通用的辅助工具。")],
            modules=[("microsphere-tools", "通用工具聚合模块")],
            compat=[("Java", "8+")],
        ),
    ),
    dict(
        slug="microsphere-test", name="Microsphere Test", layer="runtime",
        stars=0, forks=0, lang="Java", artifact="microsphere-test",
        en=dict(
            tagline="Cross-project testing infrastructure",
            summary="Provides a shared testing baseline and assertion utilities so every Microsphere sub-project follows "
                    "the same testing conventions.",
            features=[("Unified testing baseline", "Centralised test base classes and helper assertions.")],
            modules=[("microsphere-test", "Aggregator module for testing infrastructure")],
            compat=[("Java", "8+")],
        ),
        zh=dict(
            tagline="跨项目测试基础设施",
            summary="为 Microsphere 各子项目提供共享的测试基座与断言工具，保证测试风格在全生态内一致。",
            features=[("统一测试基座", "集中提供测试基类与辅助断言。")],
            modules=[("microsphere-test", "测试基础设施聚合模块")],
            compat=[("Java", "8+")],
        ),
    ),
    # ---------------------------------------------------------------- L2
    dict(
        slug="microsphere-spring", name="Microsphere Spring", layer="framework",
        stars=61, forks=39, lang="Java", artifact="microsphere-spring-context",
        bom="microsphere-spring-dependencies", version="0.2.39",
        en=dict(
            tagline="Production-grade extensions for the Spring Framework",
            summary="Solves real production pain points in a modular way: enhancing dependency injection, configuration "
                    "management, web endpoint handling, events, caching and JDBC monitoring. It is a pure additive "
                    "enhancement — a drop-in dependency for any existing Spring application.",
            features=[
                ("Parallel bean instantiation", "Resolves the bean dependency graph and initialises independent singletons concurrently to cut startup time."),
                ("Listenable Environment", "Intercepts property resolution and profile activation via EnvironmentListener and PropertyResolverListener."),
                ("Enhanced @PropertySource", "@ResourcePropertySource adds wildcard patterns, ordering, inheritance and auto-refresh on change, plus @YamlPropertySource and @JsonPropertySource."),
                ("TTL caching", "@EnableTTLCaching / @TTLCacheable add per-entry time-to-live to Spring Cache, including Redis."),
                ("Web endpoint registry", "Collects WebEndpointMapping metadata from Spring MVC, WebFlux and classic Servlet at startup for introspection and routing."),
                ("Handler method interception", "HandlerMethodInterceptor / HandlerMethodArgumentInterceptor provide AOP-style hooks around MVC and WebFlux controller invocations."),
                ("P6Spy JDBC monitoring", "@EnableP6DataSource transparently wraps existing DataSource beans for SQL tracing."),
                ("Google Guice integration", "@EnableGuice bridges Guice @Inject injection points into the Spring bean lifecycle."),
                ("Rich testing utilities", "EmbeddedTomcatContextLoader, @EnableEmbeddedDatabase, AbstractWebFluxTest and servlet/MVC test helpers."),
            ],
            modules=[
                ("microsphere-spring-context", "Core context and configuration extensions: @ResourcePropertySource, @EnableTTLCaching, @EnableConfigurationBeanBinding"),
                ("microsphere-spring-web", "Shared web abstractions: WebEndpointMapping, HandlerMethodInterceptor, @EnableWebExtension, @Idempotent"),
                ("microsphere-spring-webmvc", "Spring MVC extensions: @EnableWebMvcExtension, ReversedProxyHandlerMapping"),
                ("microsphere-spring-webflux", "Reactive web extensions: @EnableWebFluxExtension, InterceptingHandlerMethodProcessor"),
                ("microsphere-spring-jdbc", "JDBC / P6Spy integration: @EnableP6DataSource"),
                ("microsphere-spring-guice", "Google Guice bridge: @EnableGuice"),
                ("microsphere-spring-test", "Testing utilities: @EnableEmbeddedDatabase, EmbeddedTomcatContextLoader"),
            ],
            compat=[("Java", "17+"), ("Spring Framework", "6.0.x – 7.0.x (main) / 4.3.x – 5.3.x (1.x)"), ("Maven", "3.6+")],
        ),
        zh=dict(
            tagline="面向生产环境的 Spring Framework 扩展库",
            summary="以模块化方式解决真实生产场景中的 Spring 痛点：增强依赖注入、配置管理、Web 端点处理、事件、缓存与 JDBC 监控。"
                    "它是纯粹的增量增强，可作为 drop-in 依赖接入任何既有 Spring 应用。",
            features=[
                ("并行 Bean 实例化", "解析 Bean 依赖图，并发初始化互不依赖的单例，显著缩短启动时间。"),
                ("可监听的 Environment", "通过 EnvironmentListener / PropertyResolverListener 拦截属性解析与 profile 激活事件。"),
                ("增强的 @PropertySource", "@ResourcePropertySource 支持通配符资源、顺序控制、继承、变更自动刷新，并提供 @YamlPropertySource、@JsonPropertySource。"),
                ("TTL 缓存", "@EnableTTLCaching / @TTLCacheable 为 Spring Cache 增加条目级过期时间，支持 Redis。"),
                ("Web 端点注册表", "启动时收集 Spring MVC、WebFlux 与经典 Servlet 的 WebEndpointMapping 元数据，供内省与路由使用。"),
                ("Handler 方法拦截", "HandlerMethodInterceptor / HandlerMethodArgumentInterceptor 提供围绕 MVC 与 WebFlux 控制器调用的 AOP 式钩子。"),
                ("P6Spy JDBC 监控", "@EnableP6DataSource 透明包装既有 DataSource Bean，实现 SQL 追踪。"),
                ("Google Guice 集成", "@EnableGuice 把 Guice @Inject 注入点桥接到 Spring Bean 生命周期。"),
                ("丰富的测试工具", "EmbeddedTomcatContextLoader、EnableEmbeddedDatabase、AbstractWebFluxTest 等。"),
            ],
            modules=[
                ("microsphere-spring-context", "核心上下文与配置扩展：@ResourcePropertySource、@EnableTTLCaching、@EnableConfigurationBeanBinding"),
                ("microsphere-spring-web", "共享 Web 抽象：WebEndpointMapping、HandlerMethodInterceptor、@EnableWebExtension、@Idempotent"),
                ("microsphere-spring-webmvc", "Spring MVC 扩展：@EnableWebMvcExtension、ReversedProxyHandlerMapping"),
                ("microsphere-spring-webflux", "响应式扩展：@EnableWebFluxExtension、InterceptingHandlerMethodProcessor"),
                ("microsphere-spring-jdbc", "JDBC / P6Spy 集成：@EnableP6DataSource"),
                ("microsphere-spring-guice", "Google Guice 桥接：@EnableGuice"),
                ("microsphere-spring-test", "测试工具：@EnableEmbeddedDatabase、EmbeddedTomcatContextLoader"),
            ],
            compat=[("Java", "17+"), ("Spring Framework", "6.0.x – 7.0.x（main）/ 4.3.x – 5.3.x（1.x）"), ("Maven", "3.6+")],
        ),
        code="""@Configuration
@ResourcePropertySource(
        name = "app-config",
        value = "classpath*:/META-INF/config/*.properties",
        autoRefreshed = true)      // reload whenever any matched file changes
public class AppConfig { }

@Configuration
@EnableTTLCaching
public class CachingConfig { }

@TTLCacheable(cacheNames = "products", ttl = 300, timeUnit = TimeUnit.SECONDS)
public Product findById(Long id) { ... }

@Configuration
@EnableWebMvcExtension(interceptHandlerMethods = true, registerWebEndpointMappings = true)
public class WebConfig { }

@Configuration
@EnableP6DataSource          // wraps every DataSource transparently — zero code changes
public class DataSourceConfig { }""",
        lang_code="java",
        versions=[("main", "6.0.x – 7.0.x", "0.2.39"), ("1.x", "4.3.x – 5.3.x", "0.1.39")],
    ),
    dict(
        slug="microsphere-spring-boot", name="Microsphere Spring Boot", layer="framework",
        stars=24, forks=22, lang="Java", artifact="microsphere-spring-boot-core",
        bom="microsphere-spring-boot-dependencies", version="0.2.34",
        en=dict(
            tagline="Configuration governance, diagnostics and enhanced monitoring",
            summary="Adds production-ready capabilities to Spring Boot applications around configuration management, "
                    "application diagnostics and enhanced monitoring: sensible out-of-the-box defaults, Actuator endpoints "
                    "that expose far more runtime state, and cross-version compatibility from Spring Boot 2.x to 4.x.",
            features=[
                ("Default properties", "Loads graceful shutdown, MVC filter toggles and other defaults from config/default/*.properties on the classpath, overridable per module."),
                ("Advanced auto-configuration management", "A configurable import filter that merges multiple microsphere.autoconfigure.exclude sources without losing earlier exclusions."),
                ("Configuration property binding listeners", "Event-driven BindListener hooks notify your beans whenever a @ConfigurationProperties-bound value changes."),
                ("Custom Actuator endpoints", "Four additional endpoints expose classpath artifact metadata, web endpoint mappings, configuration metadata and bound configuration properties."),
                ("Monitored task scheduler", "A ThreadPoolTaskScheduler wrapper that records execution metrics via Micrometer — task latency and counts out of the box."),
                ("Artifact collision detection", "Detects duplicate JAR artifacts on the classpath at startup and surfaces a descriptive FailureAnalyzer message."),
                ("Multi-version compatibility", "A dedicated compatibility shim keeps one codebase running on Spring Boot 2.x through 4.x without forking."),
            ],
            modules=[
                ("microsphere-spring-boot-core", "Core: default properties, auto-configuration filter, bind listeners, diagnostics"),
                ("microsphere-spring-boot-actuator", "Actuator extensions: custom endpoints, monitored scheduler, endpoint defaults"),
                ("microsphere-spring-boot-compatible", "Compatibility shim for Spring Boot 2.x – 4.x (not published to Maven Central)"),
                ("microsphere-spring-boot-dependencies", "BOM"),
            ],
            compat=[("Java", "17+"), ("Spring Boot", "3.0.x – 4.1.x (main) / 2.0.x – 2.7.x (1.x)"), ("Maven", "3.9+")],
            note="Unlike spring.autoconfigure.exclude, which replaces earlier values, microsphere.autoconfigure.exclude "
                 "uses merge semantics: exclusions from multiple sources accumulate.",
        ),
        zh=dict(
            tagline="配置治理、应用诊断与增强监控",
            summary="围绕配置管理、应用诊断与增强监控，为 Spring Boot 应用补充生产就绪能力：既有开箱即用的默认值，"
                    "也有把运行时状态暴露得更彻底的 Actuator 端点，还解决了 Spring Boot 2.x 到 4.x 的跨版本兼容问题。",
            features=[
                ("默认属性", "从 classpath 的 config/default/*.properties 加载优雅停机、MVC 过滤器开关等默认值，可按模块覆盖。"),
                ("高级自动配置管理", "可配置的导入过滤器，合并多个 microsphere.autoconfigure.exclude 来源而不丢失先前排除项。"),
                ("配置绑定监听", "事件驱动的 BindListener，在 @ConfigurationProperties 绑定值变化时通知业务 Bean。"),
                ("自定义 Actuator 端点", "新增四个端点，暴露类路径制品元数据、Web 端点映射、配置元数据与已绑定配置属性。"),
                ("受监控任务调度器", "ThreadPoolTaskScheduler 包装器，通过 Micrometer 记录任务延迟与执行次数。"),
                ("制品冲突检测", "启动时检测类路径上的重复 JAR 制品，并以描述性 FailureAnalyzer 消息呈现。"),
                ("多版本兼容", "专用兼容 shim 模块让同一套代码同时跑在 Spring Boot 2.x 至 4.x 上，无需分叉维护。"),
            ],
            modules=[
                ("microsphere-spring-boot-core", "核心：默认属性、自动配置过滤器、绑定监听器、诊断"),
                ("microsphere-spring-boot-actuator", "Actuator 扩展：自定义端点、受监控调度器、端点默认值"),
                ("microsphere-spring-boot-compatible", "Spring Boot 2.x – 4.x 兼容 shim（不发布至 Maven Central）"),
                ("microsphere-spring-boot-dependencies", "BOM"),
            ],
            compat=[("Java", "17+"), ("Spring Boot", "3.0.x – 4.1.x（main）/ 2.0.x – 2.7.x（1.x）"), ("Maven", "3.9+")],
            note="相比标准 spring.autoconfigure.exclude 的覆盖语义，microsphere.autoconfigure.exclude 采用合并语义，多个配置源的排除项会累加。",
        ),
        versions=[("main", "3.0.x – 3.5.x, 4.0.x – 4.1.x", "0.2.34"), ("1.x", "2.0.x – 2.7.x", "0.1.34")],
    ),
    dict(
        slug="microsphere-spring-cloud", name="Microsphere Spring Cloud", layer="framework",
        stars=33, forks=30, lang="Java", artifact="microsphere-spring-cloud-commons",
        bom="microsphere-spring-cloud-dependencies", version="0.2.26",
        en=dict(
            tagline="Dynamic runtime configuration without restarts",
            summary="A production-ready extension library for Spring Cloud that targets common operational pain points in "
                    "distributed systems — above all, applying runtime configuration changes without restarting the application.",
            features=[
                ("OpenFeign auto-refresh", "Dynamically refreshes Feign client components (encoder, decoder, retryer, request interceptors) in response to EnvironmentChangeEvent — no restart required."),
                ("Multiple service registries", "Registers a single service instance with several registries at once (Nacos, Eureka, Consul, Zookeeper) through one unified API."),
                ("Service registration events", "Rich lifecycle events published via AOP — RegistrationPreRegisteredEvent, RegistrationRegisteredEvent, RegistrationPreDeregisteredEvent and RegistrationDeregisteredEvent."),
                ("Union discovery client", "Aggregates service instances from multiple discovery backends behind a single DiscoveryClient interface."),
                ("Fault tolerance utilities", "Weighted round-robin load balancing and Tomcat dynamic configuration support for improved resilience."),
                ("Actuator endpoints", "Built-in /service-registration and /service-deregistration endpoints for operational control at runtime."),
                ("Multi-version support", "The main branch targets Spring Cloud 2022.x – 2025.x; the 1.x branch covers Hoxton – 2021.0.x."),
            ],
            modules=[
                ("microsphere-spring-cloud-commons", "Common utilities for service discovery, registration and fault tolerance"),
                ("microsphere-spring-cloud-openfeign", "OpenFeign extensions with auto-refresh support"),
                ("microsphere-spring-cloud-dependencies", "BOM centralising dependency management"),
                ("microsphere-spring-cloud-parent", "Parent POM with Spring Cloud version profiles"),
            ],
            compat=[("Java", "17+"), ("Spring Boot", "3.0+ (main) / 2.x (1.x)"), ("Spring Cloud", "2022.0.x – 2025.0.x"), ("Maven", "3.6+")],
        ),
        zh=dict(
            tagline="免重启的动态运行时配置能力",
            summary="面向 Spring Cloud 的生产就绪扩展库，重点解决分布式系统运维中的常见痛点——尤其是无需重启应用即可完成运行时配置变更。",
            features=[
                ("OpenFeign 自动刷新", "响应 EnvironmentChangeEvent 动态刷新 Feign 客户端的 encoder、decoder、retryer、请求拦截器等配置，无需重启。"),
                ("多注册中心", "通过统一 API 将同一服务实例同时注册到 Nacos、Eureka、Consul、Zookeeper 等多个注册中心。"),
                ("服务注册事件", "经 AOP 发布注册生命周期事件，实现注册状态变更的细粒度可观测。"),
                ("联合 DiscoveryClient", "在单一 DiscoveryClient 接口后聚合多个服务发现后端的实例。"),
                ("容错工具", "加权轮询负载均衡与 Tomcat 动态配置支持，提升韧性。"),
                ("Actuator 端点", "内置 /service-registration 与 /service-deregistration 端点，支持运行时运维控制。"),
                ("多版本支持", "main 分支兼容 Spring Cloud 2022.x – 2025.x，1.x 分支兼容 Hoxton – 2021.0.x。"),
            ],
            modules=[
                ("microsphere-spring-cloud-commons", "服务发现、注册与容错的通用工具"),
                ("microsphere-spring-cloud-openfeign", "OpenFeign 扩展，支持自动刷新"),
                ("microsphere-spring-cloud-dependencies", "BOM，集中依赖管理"),
                ("microsphere-spring-cloud-parent", "父 POM，含 Spring Cloud 版本 profile"),
            ],
            compat=[("Java", "17+"), ("Spring Boot", "3.0+（main）/ 2.x（1.x）"), ("Spring Cloud", "2022.0.x – 2025.0.x"), ("Maven", "3.6+")],
        ),
        code="""@SpringBootApplication
@EnableFeignClients
@EnableFeignAutoRefresh     // refresh Feign components when configuration changes
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}""",
        lang_code="java",
        versions=[("main", "2022.0.x – 2025.0.x", "0.2.26"), ("1.x", "Hoxton – 2021.0.x", "0.1.26")],
    ),
]
