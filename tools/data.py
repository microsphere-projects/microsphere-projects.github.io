# -*- coding: utf-8 -*-
"""Canonical data for all Microsphere sub-projects, sourced from each repo's README."""

# layer id, layer title, layer subtitle
LAYERS = [
    ("foundation", "L0 · 工程基座", "Foundation",
     "统一构建与依赖治理。所有子项目的 Maven 父 POM 与 BOM 在这里定义，保证 36 个仓库的构建口径一致。"),
    ("runtime", "L1 · 运行时基座", "Runtime",
     "不依赖任何框架的纯 Java 能力层：字符串与集合、反射、类型转换、事件、日志抽象、Java/Jakarta EE 实现。"),
    ("framework", "L2 · 框架扩展", "Framework",
     "对 Spring、Spring Boot、Spring Cloud 的增强扩展，是整个生态最核心的一层。"),
    ("integration", "L3 · 生态集成", "Integration",
     "面向具体基础设施的适配层：注册中心、数据访问、缓存、RPC、容错、网关。"),
    ("crosscutting", "L4 · 横向能力", "Cross-cutting",
     "贯穿所有层的可观测性、国际化、安全、动态配置、单元化多活等能力。"),
]

# fmt: off
PROJECTS = [
# ---------------------------------------------------------------- L0
dict(
    slug="microsphere-build", name="Microsphere Build", layer="foundation",
    stars=8, forks=29, lang="Maven", artifact="microsphere-build",
    tagline="Microsphere 全系项目的 Maven 父 POM",
    summary="提供统一的构建设置与插件配置，被 Microsphere Java、Microsphere Spring 等所有子项目继承。它把 Java 多 TLS 版本编译、发布签名、覆盖率、文档生成等能力收敛到一处，让各子仓库只关心业务代码。",
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
dict(
    slug="microsphere-bom", name="Microsphere BOM", layer="foundation",
    stars=0, forks=1, lang="Maven", artifact="microsphere-bom",
    tagline="跨项目的 Maven 物料清单",
    summary="集中声明 Microsphere 生态各模块的版本，使用者导入一次即可对齐全部依赖版本，避免多模块之间的版本冲突。",
    features=[
        ("单点版本对齐", "导入 BOM 后无需为每个模块指定 `&lt;version&gt;`。"),
        ("跨仓库一致性", "与各子项目的 dependencies 模块保持版本同步。"),
        ("与 Build 协同", "配合 microsphere-build 父 POM 使用，构建与依赖口径统一。"),
    ],
    modules=[("microsphere-bom", "顶层 BOM，聚合各子项目版本")],
    compat=[("Java", "8+"), ("Maven", "3.6+")],
),
# ---------------------------------------------------------------- L1
dict(
    slug="microsphere-java", name="Microsphere Java", layer="runtime",
    stars=104, forks=52, lang="Java", artifact="microsphere-java-core",
    bom="microsphere-java-dependencies", version="0.2.x",
    tagline="整个生态的地基：可复用的 Java 组件与工具集",
    summary="Microsphere Java Framework 是 Microsphere 生态的骨干基础库。它基于标准 Java API 提供字符串、集合、反射、类型转换、事件分发、类加载与制品探测、网络、I/O、并发等一整套可复用组件，并内置编译期注解处理器。所有其它子项目都构建在它之上。",
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
        ("Java 语言模型与 JDK Tools", "面向 javax.lang.model 的组件，以及桥接 Java 编译器与注解处理工具 API 的辅助类。"),
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
    compat=[("Java", "8 / 11 / 17 / 21 / 25（CI 全覆盖）"), ("Maven", "3.6+")],
),
dict(
    slug="microsphere-logging", name="Microsphere Logging", layer="runtime",
    stars=2, forks=1, lang="Java", artifact="microsphere-logging-commons",
    bom="microsphere-logging-dependencies",
    tagline="跨日志框架的统一运行时管理抽象层",
    summary="在不改动应用代码、不重启服务的前提下，统一管理 JVM 中的日志配置。它通过 SPI 自动装载优先级最高的 Logging 实现，同时支持 JUL、Log4j、Log4j2、Logback 多后端共存。",
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
dict(
    slug="microsphere-java-enterprise", name="Microsphere Java EE", layer="runtime",
    stars=14, forks=18, lang="Java", artifact="microsphere-java-enterprise",
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
dict(
    slug="microsphere-jakarta", name="Microsphere Jakarta", layer="runtime",
    stars=2, forks=6, lang="Java", artifact="microsphere-jakarta",
    tagline="Jakarta EE 规范的 Microsphere 实现",
    summary="面向 Jakarta EE 命名空间（jakarta.*）的实现分支，适配从 Java EE 迁移后的企业应用。",
    features=[
        ("Jakarta 命名空间", "全面适配 jakarta.* 包名。"),
        ("与 Spring 6/7 对齐", "匹配 Spring Framework 6+ 采用的 Jakarta 基线。"),
    ],
    modules=[("microsphere-jakarta", "Jakarta EE 实现聚合模块")],
    compat=[("Java", "17+")],
),
dict(
    slug="microsphere-microprofile", name="Microsphere MicroProfile", layer="runtime",
    stars=1, forks=6, lang="Java", artifact="microsphere-microprofile",
    tagline="Eclipse MicroProfile 支持",
    summary="为 MicroProfile 规范提供 Microsphere 实现，面向云原生微服务的配置、容错、指标等标准化需求。",
    features=[
        ("MicroProfile 规范", "覆盖配置、容错、健康检查等 MicroProfile 能力。"),
        ("微服务友好", "与 Microsphere Spring Cloud 的多注册中心能力互补。"),
    ],
    modules=[("microsphere-microprofile", "MicroProfile 实现聚合模块")],
    compat=[("Java", "8+")],
),
dict(
    slug="microsphere-tools", name="Microsphere Tools", layer="runtime",
    stars=0, forks=5, lang="Java", artifact="microsphere-tools",
    tagline="通用研发工具集",
    summary="沉淀 Microsphere 生态在日常开发与运维中反复使用的工具类，供各子项目共享。",
    features=[("工具复用", "集中收纳跨项目通用的辅助工具。")],
    modules=[("microsphere-tools", "通用工具聚合模块")],
    compat=[("Java", "8+")],
),
dict(
    slug="microsphere-test", name="Microsphere Test", layer="runtime",
    stars=0, forks=0, lang="Java", artifact="microsphere-test",
    tagline="跨项目测试基础设施",
    summary="为 Microsphere 各子项目提供共享的测试基座与断言工具，保证测试风格在全生态内一致。",
    features=[("统一测试基座", "集中提供测试基类与辅助断言。")],
    modules=[("microsphere-test", "测试基础设施聚合模块")],
    compat=[("Java", "8+")],
),
# ---------------------------------------------------------------- L2
dict(
    slug="microsphere-spring", name="Microsphere Spring", layer="framework",
    stars=61, forks=39, lang="Java", artifact="microsphere-spring-context",
    bom="microsphere-spring-dependencies", version="0.2.39",
    tagline="面向生产环境的 Spring Framework 扩展库",
    summary="以模块化方式解决真实生产场景中的 Spring 痛点：增强依赖注入、配置管理、Web 端点处理、事件、缓存与 JDBC 监控。它是纯粹的增量增强，可作为 drop-in 依赖接入任何既有 Spring 应用。",
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
    code="""@Configuration
@ResourcePropertySource(
        name = "app-config",
        value = "classpath*:/META-INF/config/*.properties",
        autoRefreshed = true)      // 任一匹配文件变化即自动重载
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
@EnableP6DataSource          // 透明包裹所有 DataSource，零改代码接入 SQL 追踪
public class DataSourceConfig { }""",
    lang_code="java",
    compat=[("Java", "17+"), ("Spring Framework", "6.0.x – 7.0.x（main）/ 4.3.x – 5.3.x（1.x）"), ("Maven", "3.6+")],
    versions=[("main", "6.0.x – 7.0.x", "0.2.39"), ("1.x", "4.3.x – 5.3.x", "0.1.39")],
),
dict(
    slug="microsphere-spring-boot", name="Microsphere Spring Boot", layer="framework",
    stars=24, forks=22, lang="Java", artifact="microsphere-spring-boot-core",
    bom="microsphere-spring-boot-dependencies", version="0.2.34",
    tagline="配置治理、应用诊断与增强监控",
    summary="围绕配置管理、应用诊断与增强监控，为 Spring Boot 应用补充生产就绪能力：既有开箱即用的默认值，也有把运行时状态暴露得更彻底的 Actuator 端点，还解决了 Spring Boot 2.x 到 4.x 的跨版本兼容问题。",
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
    versions=[("main", "3.0.x – 3.5.x, 4.0.x – 4.1.x", "0.2.34"), ("1.x", "2.0.x – 2.7.x", "0.1.34")],
    note="相比标准 spring.autoconfigure.exclude 的覆盖语义，microsphere.autoconfigure.exclude 采用合并语义，多个配置源的排除项会累加。",
),
dict(
    slug="microsphere-spring-cloud", name="Microsphere Spring Cloud", layer="framework",
    stars=33, forks=30, lang="Java", artifact="microsphere-spring-cloud-commons",
    bom="microsphere-spring-cloud-dependencies", version="0.2.26",
    tagline="免重启的动态运行时配置能力",
    summary="面向 Spring Cloud 的生产就绪扩展库，重点解决分布式系统运维中的常见痛点——尤其是无需重启应用即可完成运行时配置变更。",
    features=[
        ("OpenFeign 自动刷新", "响应 EnvironmentChangeEvent 动态刷新 Feign 客户端的 encoder、decoder、retryer、请求拦截器等配置，无需重启。"),
        ("多注册中心", "通过统一 API 将同一服务实例同时注册到 Nacos、Eureka、Consul、Zookeeper 等多个注册中心。"),
        ("服务注册事件", "经 AOP 发布 RegistrationPreRegisteredEvent、RegistrationRegisteredEvent、RegistrationPreDeregisteredEvent、RegistrationDeregisteredEvent，实现注册状态变更的细粒度可观测。"),
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
    code="""@SpringBootApplication
@EnableFeignClients
@EnableFeignAutoRefresh     // 配置变更时自动刷新 Feign 组件
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}""",
    lang_code="java",
    compat=[("Java", "17+"), ("Spring Boot", "3.0+（main）/ 2.x（1.x）"), ("Spring Cloud", "2022.0.x – 2025.0.x"), ("Maven", "3.6+")],
    versions=[("main", "2022.0.x – 2025.0.x", "0.2.26"), ("1.x", "Hoxton – 2021.0.x", "0.1.26")],
),
# ---------------------------------------------------------------- L3
dict(
    slug="microsphere-gateway", name="Microsphere Gateway", layer="integration",
    stars=5, forks=5, lang="Java", artifact="microsphere-spring-cloud-gateway-server-webflux",
    bom="microsphere-gateway-dependencies",
    tagline="基于服务发现的 Web 端点动态路由",
    summary="扩展 Spring Cloud Gateway 生态，提供 Microsphere 特有的路由、服务发现与刷新行为。通过自定义 we:// 路由协议，把已发现服务的 Web 端点统一暴露在单个网关之后，无需在每个服务里重复定义路由。",
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
    code="""spring:
  cloud:
    gateway:
      routes:
        - id: web-endpoint-mapping
          uri: we://all            # 订阅全部已发现服务
          predicates:
            - Path=/{application}/**
          metadata:
            web-endpoint:
              excludes:
                - patterns: /internal/**
                  methods: GET""",
    lang_code="yaml",
    compat=[("JDK", "17+"), ("Maven", "3.9+"), ("Spring Cloud", "2022 / 2023 / 2024 / 2025")],
    note="目标服务必须发布 Microsphere Web 端点元数据，网关才能发现请求映射并正确重写入站路径。",
),
dict(
    slug="microsphere-redis", name="Microsphere Redis", layer="integration",
    stars=3, forks=11, lang="Java", artifact="microsphere-redis-spring",
    bom="microsphere-redis-dependencies", version="0.2.14",
    tagline="增强版 Spring Data Redis 集成框架",
    summary="在 Spring Data Redis 之上提供企业级增强能力：非侵入式的 Redis 命令拦截、深度 Spring 集成、全面的事件发布与指标采集，以及基于 Kafka 的 Redis 复制支持。",
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
    versions=[("main", "Spring Data Redis 3.0.0 – 3.5.x", "0.2.14"), ("1.x", "Spring Data Redis 2.1.0 – 2.7.x", "0.1.14")],
),
dict(
    slug="microsphere-mybatis", name="Microsphere MyBatis", layer="integration",
    stars=1, forks=3, lang="Java", artifact="microsphere-mybatis-core",
    bom="microsphere-mybatis-dependencies", version="0.2.16",
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
    versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.16"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.16")],
),
dict(
    slug="microsphere-hibernate", name="Microsphere Hibernate", layer="integration",
    stars=0, forks=1, lang="Java", artifact="microsphere-hibernate-core",
    bom="microsphere-hibernate-dependencies", version="0.2.10",
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
    versions=[("main", "Hibernate 6.2 – 7.3", "0.2.10"), ("1.x", "Hibernate 5.0 – 5.6", "0.1.10")],
),
dict(
    slug="microsphere-alibaba-druid", name="Microsphere Alibaba Druid", layer="integration",
    stars=2, forks=3, lang="Java", artifact="microsphere-alibaba-druid-spring-cloud",
    bom="microsphere-alibaba-druid-dependencies", version="0.2.21",
    tagline="为 Druid 连接池注入 SQL 拦截能力",
    summary="增强 Alibaba Druid 高性能 JDBC 连接池，提供细粒度的 SQL 语句拦截与日志能力，并作为 Sentinel、Resilience4j、Observability 等项目的底层扩展支撑。",
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
    versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.21"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.21")],
),
dict(
    slug="microsphere-alibaba-sentinel", name="Microsphere Alibaba Sentinel", layer="integration",
    stars=2, forks=11, lang="Java", artifact="microsphere-alibaba-sentinel-commons",
    bom="microsphere-alibaba-sentinel-dependencies", version="0.2.5",
    tagline="把流控能力透明注入数据库、缓存与 Web",
    summary="在 Alibaba Sentinel 流控框架与常用 Java 技术之间建立无缝集成的抽象层，将 Sentinel 的流控、熔断与系统保护能力透明地施加到数据库操作、缓存与其它基础设施组件上。",
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
    versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.5"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.5")],
),
dict(
    slug="microsphere-resilience4j", name="Microsphere Resilience4j", layer="integration",
    stars=2, forks=9, lang="Java", artifact="microsphere-resilience4j-commons",
    bom="microsphere-resilience4j-dependencies", version="0.2.4",
    tagline="统一的韧性模式落地方案",
    summary="扩展 Resilience4j，让熔断、隔板、限流、重试、超时等韧性模式能够以统一方式作用于 Spring Web MVC 应用、Feign API 客户端以及数据库访问（MyBatis、JDBC + Druid + P6Spy）等不同场景。",
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
    versions=[("main", "Resilience4j 2.0.0 – 2.4.0", "0.2.4"), ("1.x", "Resilience4j 1.3.0 – 1.7.0", "0.1.4")],
),
dict(
    slug="microsphere-netflix", name="Microsphere Netflix", layer="integration",
    stars=2, forks=8, lang="Java", artifact="microsphere-netflix-eureka-client-spring-cloud",
    bom="microsphere-netflix-dependencies", version="0.2.0",
    tagline="Eureka 的高可用集群与增强客户端",
    summary="面向 Netflix OSS 组件的增强集成框架，聚焦 Eureka 服务发现：通过 Apache Tomcat 实现服务端高可用集群，并增强客户端元数据同步与多客户端管理能力。",
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
    versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.0"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.0")],
),
dict(
    slug="microsphere-nacos", name="Microsphere Nacos", layer="integration",
    stars=2, forks=6, lang="Java", artifact="microsphere-nacos",
    bom="microsphere-nacos-dependencies", version="0.2.0",
    tagline="Alibaba Nacos 集成",
    summary="面向 Alibaba Nacos 的 Microsphere 集成项目，与 Spring Cloud 生态中的配置管理和服务发现能力协同。",
    features=[
        ("Nacos 集成", "提供与 Alibaba Nacos 的集成能力。"),
        ("BOM 管理", "通过 dependencies 模块统一版本。"),
        ("双线维护", "main 与 1.x 分支并行维护。"),
    ],
    modules=[("microsphere-nacos-dependencies", "BOM，集中依赖管理")],
    compat=[("Spring Cloud", "2022.0.x – 2025.0.x（main）/ Hoxton – 2021.0.x（1.x）")],
    versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.0"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.0")],
),
dict(
    slug="microsphere-dubbo", name="Microsphere Dubbo", layer="integration",
    stars=4, forks=7, lang="Java", artifact="microsphere-dubbo",
    tagline="Apache Dubbo 集成",
    summary="面向 Apache Dubbo RPC 框架的 Microsphere 集成项目，把生态中的拦截、可观测与容错能力带到 Dubbo 服务调用链路。",
    features=[
        ("Dubbo 集成", "提供与 Apache Dubbo 的集成能力。"),
        ("生态联动", "可与 Observability、Sentinel 等能力组合。"),
    ],
    modules=[("microsphere-dubbo", "Dubbo 集成聚合模块")],
    compat=[("Java", "8+")],
),
dict(
    slug="microsphere-tomcat", name="Microsphere Tomcat", layer="integration",
    stars=2, forks=6, lang="Java", artifact="microsphere-tomcat",
    tagline="Apache Tomcat 集成",
    summary="面向 Apache Tomcat 的集成项目，支撑 Eureka 服务端集群、嵌入式测试容器等场景下的 Tomcat 动态配置与生命周期管理。",
    features=[
        ("Tomcat 集成", "提供与 Apache Tomcat 的集成能力。"),
        ("动态配置", "与 Spring Cloud 容错工具中的 Tomcat 动态配置能力协同。"),
    ],
    modules=[("microsphere-tomcat", "Tomcat 集成聚合模块")],
    compat=[("Java", "8+")],
),
dict(
    slug="microsphere-etcd", name="Microsphere etcd", layer="integration",
    stars=0, forks=7, lang="Java", artifact="microsphere-etcd",
    tagline="etcd 集成",
    summary="面向 etcd 分布式键值存储的 Microsphere 集成项目，可作为配置中心与服务发现的后端选项。",
    features=[("etcd 集成", "提供与 etcd 的集成能力。")],
    modules=[("microsphere-etcd", "etcd 集成聚合模块")],
    compat=[("Java", "8+")],
),
# ---------------------------------------------------------------- L4
dict(
    slug="microsphere-observability", name="Microsphere Observability", layer="crosscutting",
    stars=4, forks=8, lang="Java", artifact="microsphere-observability-metrics-micrometer",
    bom="microsphere-observability-dependencies", version="0.2.3",
    tagline="监控、指标与日志的一体化增强套件",
    summary="全面提升 Java 应用（以 Spring Boot 生态为主）的监控、指标采集与日志能力。除 Micrometer、Prometheus、Log4j2、Alibaba Sentinel 的专项集成外，还提供 CGroups、网络统计等系统级自定义指标。",
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
    versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.3"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.3")],
),
dict(
    slug="microsphere-i18n", name="Microsphere i18n", layer="crosscutting",
    stars=13, forks=18, lang="Java", artifact="microsphere-i18n-core",
    bom="microsphere-i18n-dependencies", version="0.2.21",
    tagline="面向微服务的分层国际化框架",
    summary="一套完整的 Java 国际化框架，并与 Spring 生态深度集成。它提供模块化、可扩展的架构来管理本地化消息，覆盖从独立 Spring 应用到分布式云原生微服务的各类部署形态。",
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
    versions=[("main", "2022.0.x – 2025.0.x", "0.2.21"), ("1.x", "Hoxton – 2021.0.x", "0.1.21")],
),
dict(
    slug="microsphere-multiactive", name="Microsphere Multiactive", layer="crosscutting",
    stars=4, forks=14, lang="Java", artifact="microsphere-multiactive-commons",
    bom="microsphere-multiactive-dependencies", version="0.2.13",
    tagline="多活与单元化部署的分区感知框架",
    summary="面向分布式应用的多活（multi-active）分区感知部署综合框架。应用可自动发现自身所处的部署分区，并实现优先同区调用、跨区兜底的智能路由。",
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
    versions=[("main", "Spring Cloud 2022.0.x – 2025.0.x", "0.2.13"), ("1.x", "Spring Cloud Hoxton – 2021.0.x", "0.1.13")],
),
dict(
    slug="microsphere-security", name="Microsphere Security", layer="crosscutting",
    stars=3, forks=6, lang="Java", artifact="microsphere-security",
    tagline="安全能力扩展",
    summary="为 Microsphere 生态提供安全相关的扩展能力，与 Spring Security 及生态内的拦截机制协同工作。",
    features=[("安全扩展", "提供面向生态的安全能力扩展。")],
    modules=[("microsphere-security", "安全扩展聚合模块")],
    compat=[("Java", "8+")],
),
dict(
    slug="microsphere-dynamic", name="Microsphere Dynamic", layer="crosscutting",
    stars=3, forks=7, lang="Java", artifact="microsphere-dynamic",
    tagline="动态化能力支撑",
    summary="为生态提供动态化基础能力，支撑运行时配置刷新、Feign 组件热更新等免重启变更场景。",
    features=[("动态化支撑", "为运行时动态变更提供基础设施。")],
    modules=[("microsphere-dynamic", "动态化能力聚合模块")],
    compat=[("Java", "8+")],
),
dict(
    slug="microsphere-configuration", name="Microsphere Configuration", layer="crosscutting",
    stars=2, forks=10, lang="Java", artifact="microsphere-configuration",
    tagline="配置体系增强",
    summary="围绕配置体系提供增强能力，与 Spring Environment、@ConfigurationProperties 以及 Spring Cloud 配置刷新机制协同。",
    features=[("配置增强", "提供配置体系相关的增强能力。")],
    modules=[("microsphere-configuration", "配置增强聚合模块")],
    compat=[("Java", "8+")],
),
dict(
    slug="microsphere-ai", name="Microsphere AI", layer="crosscutting",
    stars=0, forks=1, lang="Java", artifact="microsphere-ai",
    tagline="面向 AI 场景的探索项目",
    summary="Microsphere 在人工智能方向的探索性项目，探索生态能力在 AI 应用场景中的延展。",
    features=[("AI 场景探索", "面向 AI 应用场景的能力探索。")],
    modules=[("microsphere-ai", "AI 能力聚合模块")],
    compat=[("Java", "17+")],
),
dict(
    slug="microsphere-devops", name="Microsphere DevOps", layer="crosscutting",
    stars=5, forks=6, lang="Shell", artifact=None,
    tagline="生态的工程效能与运维支撑",
    summary="承载 Microsphere 生态的 DevOps 能力，覆盖构建、发布与环境管理等工程效能环节，并配套独立的 UI 项目。",
    features=[
        ("工程效能", "支撑生态的持续集成与交付流程。"),
        ("配套 UI", "由 microsphere-devops-ui（TypeScript）提供可视化界面。"),
    ],
    modules=[("microsphere-devops", "DevOps 脚本与配置"), ("microsphere-devops-ui", "TypeScript 编写的 DevOps UI")],
    compat=[("Node", "18+（devops-ui）")],
),
]
# fmt: on
