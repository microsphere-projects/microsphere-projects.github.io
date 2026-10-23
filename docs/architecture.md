---
title: 架构大图
description: Microsphere Projects 五层架构总览、依赖流向、能力域横切汇总与典型调用链路
outline: [2, 3]
---

# 架构大图

这一页把 **32 个子项目的特性**整合到一张图上。整份架构遵循一条简单规则：**每一层只依赖它下面的层，横向能力可插拔地贯穿全部层级。**

<ArchitectureMap></ArchitectureMap>

## 依赖流向

依赖方向严格自上而下（上层依赖下层），不存在反向依赖：

```
L4 横向能力   observability · i18n · security · dynamic · multiactive · configuration
                    ↓ 织入（可插拔，不产生编译期依赖）
L3 生态集成   gateway · nacos · redis · mybatis · hibernate · druid
              sentinel · resilience4j · netflix · dubbo · tomcat · etcd
                    ↓ 依赖
L2 框架扩展   microsphere-spring · microsphere-spring-boot · microsphere-spring-cloud
                    ↓ 依赖
L1 运行时基座 microsphere-java · logging · java-enterprise · jakarta · microprofile
                    ↓ 依赖
L0 工程基座   microsphere-build（父 POM） · microsphere-bom（版本治理）
```

这条链带来三个实际收益：

1. **可裁剪** — 只用 `microsphere-java` 时，不会引入任何 Spring 依赖。
2. **版本一致** — 所有层共享 L0 的构建口径与版本治理，跨仓库不会出现依赖漂移。
3. **横向能力无侵入** — L4 通过拦截管道与事件机制织入，业务代码零改动即可获得可观测性与韧性。

## 五层职责

| 层 | 职责 | 关键约束 |
|----|------|----------|
| **L0 工程基座** | 统一 Maven 父 POM、插件版本、profile 与 BOM 治理 | 覆盖 Java 8 / 11 / 17 / 21 / 25 五个 TLS 版本 |
| **L1 运行时基座** | 零框架依赖的 Java 能力：工具类、反射、类型转换、事件、日志抽象 | 不得依赖 Spring 或其它应用框架 |
| **L2 框架扩展** | 对 Spring、Spring Boot、Spring Cloud 的增强 | 必须是 drop-in 增量增强，不改变默认行为 |
| **L3 生态集成** | 面向具体基础设施的适配：注册中心、数据访问、缓存、RPC、容错 | 以拦截 / 扩展点接入，不侵入业务代码 |
| **L4 横向能力** | 可观测、国际化、安全、动态配置、多活路由 | 通过 SPI 与事件织入，可独立开关 |

## 能力域横切汇总

把各子项目的特性按**能力域**重新聚合，可以看到同一主题在生态中被拆解到了哪些项目：

### 配置动态化

| 项目 | 贡献 |
|------|------|
| [Spring](/projects/microsphere-spring) | `@ResourcePropertySource` 支持通配符、继承与 `autoRefreshed` 自动重载；`@YamlPropertySource` / `@JsonPropertySource` |
| [Spring Cloud](/projects/microsphere-spring-cloud) | 响应 `EnvironmentChangeEvent` 自动刷新 OpenFeign 的 encoder / decoder / retryer / 拦截器 |
| [Spring Boot](/projects/microsphere-spring-boot) | `BindListener` 在 `@ConfigurationProperties` 绑定值变化时发出通知；`microsphere.autoconfigure.exclude` 采用合并语义 |
| [i18n](/projects/microsphere-i18n) | Spring Cloud 配置驱动的消息运行时更新；`/actuator/i18n` 支持在线读写 |
| [Dynamic](/projects/microsphere-dynamic) | 为运行时动态变更提供基础设施 |

### 可观测性

| 项目 | 贡献 |
|------|------|
| [Observability](/projects/microsphere-observability) | Micrometer `MeterBinder`（Sentinel / P6Spy / 系统指标）、Prometheus Collector、CGroups 与网络指标 |
| [Spring](/projects/microsphere-spring) | `@EnableP6DataSource` 透明包裹 DataSource 实现 SQL 追踪 |
| [Druid](/projects/microsphere-alibaba-druid) | SQL 语句拦截与日志，作为观测数据的采集入口 |
| [MyBatis](/projects/microsphere-mybatis) | SQL 拦截管道，输出日志、指标与链路信息 |
| [Spring Boot](/projects/microsphere-spring-boot) | 四个新增 Actuator 端点暴露类路径制品、Web 端点映射、配置元数据与已绑定属性 |

### 韧性与流控

| 项目 | 贡献 |
|------|------|
| [Sentinel](/projects/microsphere-alibaba-sentinel) | 流控 / 熔断 / 系统保护，覆盖 WebMVC、WebFlux、Druid、Hibernate、MyBatis、P6Spy、Redis |
| [Resilience4j](/projects/microsphere-resilience4j) | 熔断、隔板、限流、重试、超时，覆盖 Web MVC、Feign、MyBatis、JDBC |
| [Spring Cloud](/projects/microsphere-spring-cloud) | 加权轮询负载均衡与 Tomcat 动态配置 |
| [Multiactive](/projects/microsphere-multiactive) | 同区优先路由 + 跨区兜底，故障域隔离 |

### 服务治理

| 项目 | 贡献 |
|------|------|
| [Spring Cloud](/projects/microsphere-spring-cloud) | 多注册中心注册（Nacos / Eureka / Consul / Zookeeper）、注册生命周期事件、联合 DiscoveryClient |
| [Gateway](/projects/microsphere-gateway) | `we://` 协议基于服务发现动态路由 Web 端点，支持按路径 / 方法 / 头 / 参数过滤 |
| [Netflix](/projects/microsphere-netflix) | Eureka 客户端元数据同步增强、Tomcat 集群高可用服务端 |
| [Nacos](/projects/microsphere-nacos) | Alibaba Nacos 集成 |

### 数据访问

| 项目 | 贡献 |
|------|------|
| [MyBatis](/projects/microsphere-mybatis) | SQL 拦截管道，支持注入安全、限流、缓存等横切逻辑 |
| [Hibernate](/projects/microsphere-hibernate) | ORM 扩展，覆盖 Hibernate 6.2–7.3 与 5.0–5.6 |
| [Druid](/projects/microsphere-alibaba-druid) | 连接池级 SQL 拦截与日志 |
| [Redis](/projects/microsphere-redis) | Redis 命令非侵入拦截、事件与指标、基于 Kafka 的复制 |
| [Spring](/projects/microsphere-spring) | `@EnableTTLCaching` / `@TTLCacheable` 提供条目级 TTL 缓存 |
| [ETCD](/projects/microsphere-etcd) | etcd 键值存储集成 |

### 国际化与安全

| 项目 | 贡献 |
|------|------|
| [i18n](/projects/microsphere-i18n) | 分层消息源、优先级组合、`MessageSource` 桥接、Bean Validation 翻译、OpenFeign `Accept-Language` 传播、集中式 i18n Server |
| [Security](/projects/microsphere-security) | 安全能力扩展 |
| [Spring](/projects/microsphere-spring) | `@Idempotent` 幂等注解、`HandlerMethodInterceptor` 拦截器钩子 |

### 工程治理

| 项目 | 贡献 |
|------|------|
| [Build](/projects/microsphere-build) | 统一父 POM：多 TLS 版本、插件锁定、六套 profile、Central Portal 发布 |
| [BOM](/projects/microsphere-bom) | 跨项目版本对齐 |
| [Logging](/projects/microsphere-logging) | 跨 JUL / Log4j / Log4j2 / Logback 的统一日志管理抽象，支持运行时改级别与 JMX |
| [DevOps](/projects/microsphere-devops) | 工程效能与运维支撑，含 TypeScript UI |

## 典型调用链路

一次跨服务请求在启用 Gateway + Spring Cloud + 可观测性后的完整链路：

<ClientOnly>
<div class="flow">
  <svg viewBox="0 0 900 250" role="img" aria-label="Microsphere 典型调用链路">
    <defs>
      <linearGradient id="fg" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="#7c5cf0" />
        <stop offset="100%" stop-color="#0ea5e9" />
      </linearGradient>
      <marker id="fh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M0 0L10 5L0 10z" fill="currentColor" />
      </marker>
    </defs>

    <g font-family="ui-sans-serif, system-ui, sans-serif" font-size="12.5" fill="currentColor">
      <!-- row 1 -->
      <rect x="10" y="18" width="150" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:var(--vp-c-divider)"/>
      <text x="85" y="39" text-anchor="middle" font-weight="700">客户端请求</text>
      <text x="85" y="55" text-anchor="middle" font-size="11" opacity=".65">HTTP</text>

      <rect x="196" y="18" width="164" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#10b981"/>
      <text x="278" y="39" text-anchor="middle" font-weight="700">microsphere-gateway</text>
      <text x="278" y="55" text-anchor="middle" font-size="11" opacity=".65">we:// 动态路由 + 端点过滤</text>

      <rect x="396" y="18" width="164" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#7c5cf0"/>
      <text x="478" y="39" text-anchor="middle" font-weight="700">服务发现</text>
      <text x="478" y="55" text-anchor="middle" font-size="11" opacity=".65">多注册中心 · 同区优先</text>

      <rect x="596" y="18" width="164" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#7c5cf0"/>
      <text x="678" y="39" text-anchor="middle" font-weight="700">目标服务实例</text>
      <text x="678" y="55" text-anchor="middle" font-size="11" opacity=".65">MVC / WebFlux 控制器</text>

      <rect x="796" y="18" width="94" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:var(--vp-c-divider)"/>
      <text x="843" y="39" text-anchor="middle" font-weight="700">响应</text>
      <text x="843" y="55" text-anchor="middle" font-size="11" opacity=".65">i18n 本地化</text>

      <!-- arrows row 1 -->
      <g stroke="currentColor" fill="none" stroke-width="1.6" marker-end="url(#fh)" opacity=".8">
        <path d="M162 41h28" /><path d="M362 41h28" /><path d="M562 41h28" /><path d="M762 41h28" />
      </g>

      <!-- down connector -->
      <path d="M678 66v34" stroke="currentColor" fill="none" stroke-width="1.6" stroke-dasharray="4 4" opacity=".5"/>

      <!-- row 2 -->
      <rect x="396" y="104" width="364" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#f59e0b"/>
      <text x="578" y="125" text-anchor="middle" font-weight="700">OpenFeign 客户端（自动刷新）</text>
      <text x="578" y="141" text-anchor="middle" font-size="11" opacity=".65">EnvironmentChangeEvent 驱动热更新 · Accept-Language 透传</text>

      <rect x="10" y="104" width="164" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:var(--vp-c-divider)"/>
      <text x="92" y="125" text-anchor="middle" font-weight="700">拦截管道</text>
      <text x="92" y="141" text-anchor="middle" font-size="11" opacity=".65">Handler / SQL / Redis</text>

      <rect x="210" y="104" width="150" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#f43f5e"/>
      <text x="285" y="125" text-anchor="middle" font-weight="700">流控与熔断</text>
      <text x="285" y="141" text-anchor="middle" font-size="11" opacity=".65">Sentinel · Resilience4j</text>

      <g stroke="currentColor" fill="none" stroke-width="1.6" marker-end="url(#fh)" opacity=".8">
        <path d="M176 127h28" /><path d="M362 127h28" />
      </g>

      <!-- row 3 -->
      <rect x="396" y="186" width="364" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:#0ea5e9"/>
      <text x="578" y="207" text-anchor="middle" font-weight="700">Micrometer / Prometheus 指标导出</text>
      <text x="578" y="223" text-anchor="middle" font-size="11" opacity=".65">SQL、Redis、Feign、CGroups、网络统计</text>

      <rect x="10" y="186" width="364" height="46" rx="10" style="fill:var(--vp-c-bg-soft);stroke:var(--vp-c-divider)"/>
      <text x="192" y="207" text-anchor="middle" font-weight="700">日志抽象层（JUL / Log4j2 / Logback）</text>
      <text x="192" y="223" text-anchor="middle" font-size="11" opacity=".65">运行时级别调整 · JMX 管控</text>

      <path d="M578 152v30" stroke="currentColor" fill="none" stroke-width="1.6" stroke-dasharray="4 4" opacity=".5"/>
      <path d="M192 186v-6" stroke="currentColor" fill="none" stroke-width="1.6" opacity=".3"/>
    </g>
  </svg>
</div>
</ClientOnly>

链路上的每个环节都可以独立开关：不需要网关就只用 Spring Cloud，不需要流控就不引入 Sentinel，
可观测性通过 Micrometer 自动装配，全程不改业务代码。

## 选型建议

::: tip 从小处开始
不要一次性引入全部依赖。推荐路径是：

1. 先引入 `microsphere-java-dependencies`，把工具库用起来；
2. 有 Spring 应用后叠加 `microsphere-spring-dependencies`，解决配置与启动问题；
3. 微服务化后再引入 `microsphere-spring-cloud-dependencies`；
4. 最后按痛点接入 L3 / L4 —— 观测、流控、国际化各取所需。
:::

::: warning 版本线不要混用
`main`（0.2.x）与 `1.x`（0.1.x）面向不同的 Spring 代际，**同一个应用里不要混用两条线的模块**。
详见[版本兼容矩阵](/guide/compatibility)。
:::
