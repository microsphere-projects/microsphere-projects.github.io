---
layout: page
title: Microsphere Projects — a layered enhancement system for Java and Spring
description: The official site of Microsphere Projects — 32 sub-projects across five architectural layers, with unified BOMs and a full compatibility matrix.
outline: false
---

<HomeHero />

---

## Microsphere in one minute

Microsphere Projects is an open-source organisation of **36 GitHub repositories** that provides layered
enhancements for the Java and Spring ecosystem. It is not a single framework but a **composable capability matrix**:
you can use `microsphere-java` purely as a utility library, add Spring Cloud extensions to get restart-free Feign
refresh, or stack observability, internationalisation and multi-active routing on top.

Every project shares the same engineering contract:

- **One Group ID** — `io.github.microsphere-projects`
- **One BOM convention** — every sub-project ships a `*-dependencies` module, so importing once aligns all versions
- **One build baseline** — the `microsphere-build` parent POM covers Java 8 / 11 / 17 / 21 / 25
- **Two release lines** — `main` targets the current generation (Spring Boot 3/4, Spring Cloud 2022–2025),
  while `1.x` serves existing systems (Spring Boot 2, Hoxton–2021)

## Where it fits

| If you need to… | Capability | Entry point |
|-----------------|------------|-------------|
| Cut slow startup caused by serial bean creation | Resolve the dependency graph and build independent singletons concurrently | [Spring](/projects/microsphere-spring) |
| Stop redeploying for every configuration change | Hot-refresh Feign, property sources and i18n messages on change | [Spring Cloud](/projects/microsphere-spring-cloud) |
| See where slow SQL goes in production | Intercept SQL non-intrusively and feed Micrometer | [Observability](/projects/microsphere-observability) |
| Add rate limiting and circuit breaking | One model across web, database and Redis | [Sentinel](/projects/microsphere-alibaba-sentinel) |
| Centralise messages for many locales | Layered message sources plus a centralised i18n server | [i18n](/projects/microsphere-i18n) |
| Register one instance with several registries | Unified multi-registry API and a union discovery client | [Spring Cloud](/projects/microsphere-spring-cloud) |
| Prefer same-zone calls in an active-active setup | Zone-aware routing with cross-zone fallback | [Multiactive](/projects/microsphere-multiactive) |
| Avoid duplicating gateway routes per service | The `we://` scheme routes discovered endpoints dynamically | [Gateway](/projects/microsphere-gateway) |

## Next steps

- [Architecture](/architecture) — the five layers and how every sub-project fits together, fully interactive
- [All projects](/projects/) — the complete catalogue with search, layer filters and sorting
- [Getting started](/guide/getting-started) — from importing a BOM to your first feature
