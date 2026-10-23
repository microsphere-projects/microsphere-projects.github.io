---
title: Community
description: How to get involved with Microsphere Projects, maintainers and code of conduct
outline: [2, 3]
---

# Community

## Getting help

| Channel | Purpose |
|---------|---------|
| [GitHub Issues](https://github.com/microsphere-projects/microsphere-java/issues) | Bug reports and feature requests (search existing issues first) |
| [GitHub Discussions](https://github.com/microsphere-projects/microsphere-java/discussions) | Usage questions and design discussions |
| [DeepWiki](https://deepwiki.com/microsphere-projects/microsphere-java) | AI documentation that answers questions directly from source |
| Email | mercyblitz@gmail.com |

When reporting a bug, always include **Java version, Spring / Spring Boot version, Microsphere version, a minimal
reproducer and the full stack trace**.

## Contributing

1. Fork the repository and create a feature branch from `main`
2. Implement the change with tests
3. Verify locally: `./mvnw test` (on Windows: `mvnw.cmd test`)
4. Open a pull request — **CI (Maven + JUnit) must pass**
5. Read the repository's `CODE_OF_CONDUCT.md` before participating

```bash
git clone https://github.com/microsphere-projects/microsphere-java.git
cd microsphere-java
./mvnw package
```

## Maintainers

| Name | Role | Contact |
|------|------|---------|
| [Mercy Ma (mercyblitz)](https://github.com/mercyblitz) | Lead Architect & Developer | mercyblitz@gmail.com |

## Organisation

| Item | Value |
|------|-------|
| Organisation | [microsphere-projects](https://github.com/microsphere-projects) |
| Created | 2021-12-25 |
| Location | China |
| Public repositories | 36 |
| License | Apache License 2.0 |

## Supporting repositories

Some repositories exist to keep the ecosystem running rather than to provide capabilities:

| Repository | Purpose |
|------------|---------|
| `microsphere-projects.github.io` | The official site (GitHub Pages) |
| `.github` | Organisation-wide templates and workflow configuration |
| `microsphere-devops` / `microsphere-devops-ui` | Engineering efficiency and operations UI (TypeScript) |
| `microsphere-apidocs` | API documentation generation |

## License

All Microsphere Projects code is released under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
