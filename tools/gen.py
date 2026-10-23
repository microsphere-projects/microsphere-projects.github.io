# -*- coding: utf-8 -*-
"""Generate one standalone Markdown page per Microsphere sub-project."""
import os, sys, io, json, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import PROJECTS, LAYERS

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "docs", "projects")
os.makedirs(OUT, exist_ok=True)

LAYER_MAP = {l[0]: {"title": l[1], "en": l[2], "desc": l[3]} for l in LAYERS}
LAYER_ORDER = [l[0] for l in LAYERS]


def esc(s):
    return s.replace('"', '\\"')


def safe(s):
    """Escape angle brackets that would otherwise be parsed as raw HTML by Vue."""
    return re.sub(r'<(/?[A-Za-z][A-Za-z0-9-]*)>', r'`&lt;\1&gt;`', str(s))


def maven_block(p):
    bom = p.get("bom")
    art = p.get("artifact")
    if not art:
        return ""
    lines = ["```xml", "<dependencyManagement>", "    <dependencies>", "        <dependency>",
             "            <groupId>io.github.microsphere-projects</groupId>",
             "            <artifactId>%s</artifactId>" % (bom or art),
             "            <version>${%s.version}</version>" % p["slug"],
             "            <type>pom</type>", "            <scope>import</scope>",
             "        </dependency>", "    </dependencies>", "</dependencyManagement>", "```"]
    if bom:
        lines += ["", "然后按需引入模块（版本由 BOM 管理，无需指定）：", "", "```xml", "<dependencies>",
                  "    <dependency>",
                  "        <groupId>io.github.microsphere-projects</groupId>",
                  "        <artifactId>%s</artifactId>" % art,
                  "    </dependency>", "</dependencies>", "```"]
    return "\n".join(lines)


def build_page(p):
    o = io.StringIO()
    w = o.write

    # --- frontmatter (YAML, machine readable) ---
    w("---\n")
    w("title: %s\n" % p["name"])
    w('description: "%s"\n' % esc(p["summary"]))
    w("outline: deep\n")
    w("project:\n")
    w("  slug: %s\n" % p["slug"])
    w("  name: %s\n" % p["name"])
    w("  layer: %s\n" % p["layer"])
    w("  tagline: %s\n" % p["tagline"])
    w("  lang: %s\n" % p["lang"])
    w("  stars: %d\n" % p["stars"])
    w("  forks: %d\n" % p["forks"])
    if p.get("artifact"):
        w("  artifactId: %s\n" % p["artifact"])
    if p.get("bom"):
        w("  bom: %s\n" % p["bom"])
    if p.get("version"):
        w("  version: %s\n" % p["version"])
    w("---\n\n")

    w("<ProjectHeader />\n\n")

    # --- overview ---
    w("## 它解决什么问题\n\n")
    w("%s\n\n" % safe(p["summary"]))

    # --- features ---
    w("## 核心特性\n\n")
    for name, desc in p["features"]:
        w("- **%s** — %s\n" % (safe(name), safe(desc)))
    w("\n")

    # --- code sample ---
    if p.get("code"):
        w("## 用法示例\n\n")
        w("```%s\n%s\n```\n\n" % (p.get("lang_code", "java"), p["code"]))

    # --- modules ---
    w("## 模块构成\n\n")
    w("| 模块 | 说明 |\n|------|------|\n")
    for m, d in p["modules"]:
        w("| `%s` | %s |\n" % (safe(m), safe(d)))
    w("\n")

    # --- dependency ---
    if p.get("artifact"):
        w("## 引入依赖\n\n")
        w(maven_block(p))
        w("\n\n")

    # --- compatibility ---
    w("## 环境要求\n\n")
    w("| 项目 | 版本 |\n|------|------|\n")
    for k, v in p["compat"]:
        w("| %s | %s |\n" % (safe(k), safe(v)))
    w("\n")

    if p.get("versions"):
        w("### 版本线\n\n")
        w("| 分支 | 兼容范围 | 最新版本 |\n|------|----------|----------|\n")
        for br, scope, ver in p["versions"]:
            w("| `%s` | %s | `%s` |\n" % (safe(br), safe(scope), safe(ver)))
        w("\n")

    if p.get("note"):
        w("::: tip 注意\n%s\n:::\n\n" % safe(p["note"]))

    # --- links ---
    w("## 相关链接\n\n")
    w("- [GitHub 仓库](https://github.com/microsphere-projects/%s)\n" % p["slug"])
    w("- [问题反馈](https://github.com/microsphere-projects/%s/issues)\n" % p["slug"])
    w("- [DeepWiki 智能文档](https://deepwiki.com/microsphere-projects/%s)\n" % p["slug"])
    if p.get("artifact"):
        w("- [Maven Central · %s](https://central.sonatype.com/artifact/io.github.microsphere-projects/%s)\n"
          % (p["artifact"], p["artifact"]))
    w("\n")

    # --- prev / next nav ---
    w("<ProjectNav />\n")
    return o.getvalue()


# ---------------- generate project pages ----------------
order = sorted(PROJECTS, key=lambda p: (LAYER_ORDER.index(p["layer"]), -p["stars"], p["slug"]))
for i, p in enumerate(order):
    prev_p = order[i - 1] if i > 0 else None
    next_p = order[i + 1] if i < len(order) - 1 else None
    body = build_page(p)
    path = os.path.join(OUT, p["slug"] + ".md")
    open(path, "w", encoding="utf-8").write(body)
    print("wrote", p["slug"] + ".md")

# ---------------- generate projects/index.md ----------------
o = io.StringIO()
w = o.write
w("""---
title: 子项目总览
description: Microsphere Projects 全部子项目的分层总览与能力矩阵
outline: false
---

<ProjectsIndex />

## 分层说明

""")
for lid, title, en, desc in LAYERS:
    w("### %s · %s\n\n%s\n\n" % (title, en, desc))

w("""> 分层依据是各项目在生态中的依赖位置：L1 不依赖任何框架，L2 构建于 L1 之上扩展 Spring 全家桶，
> L3 面向具体基础设施做适配，L4 是可插拔的横向能力。实际使用时可按需组合，不存在强制依赖。

## 能力矩阵

| 子项目 | 分层 | 语言 | Star | Fork | 一句话 |
|--------|------|------|------|------|--------|
""")
for p in order:
    w("| [%s](./%s) | %s | %s | %d | %d | %s |\n"
      % (p["name"], p["slug"], LAYER_MAP[p["layer"]]["en"], p["lang"], p["stars"], p["forks"], safe(p["tagline"])))
w("\n")
open(os.path.join(OUT, "index.md"), "w", encoding="utf-8").write(o.getvalue())
print("wrote projects/index.md")

# ---------------- emit sidebar module ----------------
sb = ['// AUTO-GENERATED by .cache/gen.py — do not edit by hand.',
      'export const projectsSidebar = [']
for lid, title, en, desc in LAYERS:
    items = [p for p in order if p["layer"] == lid]
    sb.append('  {')
    sb.append('    text: "%s",' % title)
    sb.append('    items: [')
    for p in items:
        sb.append('      { text: "%s", link: "/projects/%s" },' % (p["name"].replace("Microsphere ", ""), p["slug"]))
    sb.append('    ],')
    sb.append('  },')
sb.append(']')
sb.append('')
open(os.path.join(ROOT, "docs", ".vitepress", "sidebar.mjs"), "w", encoding="utf-8").write("\n".join(sb))
print("wrote sidebar.mjs")

# ---------------- emit JS data for the overview grid ----------------
js = {"layers": [{"id": l[0], "title": l[1], "en": l[2], "desc": l[3]} for l in LAYERS],
      "projects": [{k: v for k, v in p.items() if k != "code"} for p in order]}
data_dir = os.path.join(ROOT, "docs", ".vitepress", "theme", "data")
os.makedirs(data_dir, exist_ok=True)
open(os.path.join(data_dir, "projects.json"), "w", encoding="utf-8").write(
    json.dumps(js, ensure_ascii=False, indent=2))
print("wrote projects.json (%d projects)" % len(order))
