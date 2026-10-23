# -*- coding: utf-8 -*-
"""Generate one standalone Markdown page per sub-project, in English and Chinese.

English is the primary locale and lives at docs/projects/.
Chinese is the secondary locale and lives at docs/zh/projects/.

Also emits: bilingual sidebar modules and theme/data/projects.json.
"""
import os, sys, io, json, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import PROJECTS, LAYERS

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DOCS = os.path.join(ROOT, "docs")

LABELS = {
    "en": dict(
        overview="Overview",
        features="Key Features",
        usage="Usage Example",
        modules="Modules",
        getting_started="Getting Started",
        requirements="Requirements",
        versions="Version Lines",
        links="Links",
        note="Note",
        bom_note="Then add only the modules you need — versions are managed by the BOM:",
        repo="GitHub Repository",
        issues="Report an Issue",
        deepwiki="DeepWiki Docs",
        central="Maven Central",
        index_title="All Projects",
        index_desc="The complete Microsphere catalogue — layered, searchable, and sortable",
        layer_heading="How the layers work",
        matrix="Capability Matrix",
        matrix_note="Layers follow dependency order: L1 depends on no framework, L2 extends the Spring stack on top of L1, "
                    "L3 adapts concrete infrastructure, and L4 is a pluggable cross-cutting capability. Any combination is valid.",
        col_project="Project", col_layer="Layer", col_lang="Lang", col_star="Stars",
        col_fork="Forks", col_tagline="In one line",
    ),
    "zh": dict(
        overview="它解决什么问题",
        features="核心特性",
        usage="用法示例",
        modules="模块构成",
        getting_started="引入依赖",
        requirements="环境要求",
        versions="版本线",
        links="相关链接",
        note="注意",
        bom_note="然后按需引入模块（版本由 BOM 管理，无需指定）：",
        repo="GitHub 仓库",
        issues="问题反馈",
        deepwiki="DeepWiki 智能文档",
        central="Maven Central",
        index_title="子项目总览",
        index_desc="Microsphere 全部子项目——分层归类，支持搜索与排序",
        layer_heading="分层说明",
        matrix="能力矩阵",
        matrix_note="分层依据是各项目在生态中的依赖位置：L1 不依赖任何框架，L2 构建于 L1 之上扩展 Spring 全家桶，"
                    "L3 面向具体基础设施做适配，L4 是可插拔的横向能力。实际使用时可按需组合，不存在强制依赖。",
        col_project="子项目", col_layer="分层", col_lang="语言", col_star="Star",
        col_fork="Fork", col_tagline="一句话",
    ),
}

PREFIX = {"en": "", "zh": "/zh"}


def safe(s):
    """Escape bare HTML-looking tags outside inline code spans."""
    parts = str(s).split("`")
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"<(/?[A-Za-z][A-Za-z0-9-]*)>", r"&lt;\1&gt;", parts[i])
    return "`".join(parts)


def yaml_str(s):
    return '"%s"' % str(s).replace('"', '\\"')


def maven_block(p, lang):
    L = LABELS[lang]
    bom, art = p.get("bom"), p.get("artifact")
    if not art:
        return ""
    slug = p["slug"]
    out = [
        "```xml", "<dependencyManagement>", "    <dependencies>", "        <dependency>",
        "            <groupId>io.github.microsphere-projects</groupId>",
        "            <artifactId>%s</artifactId>" % (bom or art),
        "            <version>${%s.version}</version>" % slug,
        "            <type>pom</type>", "            <scope>import</scope>",
        "        </dependency>", "    </dependencies>", "</dependencyManagement>", "```",
    ]
    if bom:
        out += ["", L["bom_note"], "", "```xml", "<dependencies>", "    <dependency>",
                "        <groupId>io.github.microsphere-projects</groupId>",
                "        <artifactId>%s</artifactId>" % art,
                "    </dependency>", "</dependencies>", "```"]
    return "\n".join(out)


def build_page(p, lang):
    L = LABELS[lang]
    d = p[lang]
    pre = PREFIX[lang]
    o = io.StringIO()
    w = o.write

    w("---\n")
    w("title: %s\n" % p["name"])
    w("description: %s\n" % yaml_str(safe(d["summary"])))
    w("outline: deep\n")
    w("project:\n")
    w("  slug: %s\n" % p["slug"])
    w("  layer: %s\n" % p["layer"])
    w("---\n\n")

    w("<ProjectHeader></ProjectHeader>\n\n")

    w("## %s\n\n" % L["overview"])
    w("%s\n\n" % safe(d["summary"]))

    w("## %s\n\n" % L["features"])
    for name, desc in d["features"]:
        w("- **%s** — %s\n" % (safe(name), safe(desc)))
    w("\n")

    if p.get("code"):
        w("## %s\n\n" % L["usage"])
        w("```%s\n%s\n```\n\n" % (p.get("lang_code", "java"), p["code"]))

    w("## %s\n\n" % L["modules"])
    w("| %s | |\n|------|------|\n" % ("Module" if lang == "en" else "模块"))
    for m, desc in d["modules"]:
        w("| `%s` | %s |\n" % (safe(m), safe(desc)))
    w("\n")

    if p.get("artifact"):
        w("## %s\n\n" % L["getting_started"])
        w(maven_block(p, lang))
        w("\n\n")

    w("## %s\n\n" % L["requirements"])
    w("| | |\n|------|------|\n")
    for k, v in d["compat"]:
        w("| %s | %s |\n" % (safe(k), safe(v)))
    w("\n")

    if p.get("versions"):
        w("### %s\n\n" % L["versions"])
        w("| %s | | |\n|------|----------|----------|\n"
          % ("Branch" if lang == "en" else "分支"))
        for br, scope, ver in p["versions"]:
            w("| `%s` | %s | `%s` |\n" % (safe(br), safe(scope), safe(ver)))
        w("\n")

    if d.get("note"):
        w("::: tip %s\n%s\n:::\n\n" % (L["note"], safe(d["note"])))

    w("## %s\n\n" % L["links"])
    w("- [%s](https://github.com/microsphere-projects/%s)\n" % (L["repo"], p["slug"]))
    w("- [%s](https://github.com/microsphere-projects/%s/issues)\n" % (L["issues"], p["slug"]))
    w("- [%s](https://deepwiki.com/microsphere-projects/%s)\n" % (L["deepwiki"], p["slug"]))
    if p.get("artifact"):
        w("- [%s · %s](https://central.sonatype.com/artifact/io.github.microsphere-projects/%s)\n"
          % (L["central"], p["artifact"], p["artifact"]))
    w("\n")

    w("<ProjectNav></ProjectNav>\n")
    return o.getvalue()


LAYER_ORDER = [l["id"] for l in LAYERS]
order = sorted(PROJECTS, key=lambda p: (LAYER_ORDER.index(p["layer"]), -p["stars"], p["slug"]))

# ---------------- project pages ----------------
for lang in ("en", "zh"):
    out_dir = os.path.join(DOCS, "projects") if lang == "en" else os.path.join(DOCS, "zh", "projects")
    os.makedirs(out_dir, exist_ok=True)
    for p in order:
        open(os.path.join(out_dir, p["slug"] + ".md"), "w", encoding="utf-8").write(build_page(p, lang))
    print("wrote %d pages -> %s" % (len(order), out_dir))

# ---------------- projects index ----------------
for lang in ("en", "zh"):
    L = LABELS[lang]
    pre = PREFIX[lang]
    o = io.StringIO()
    w = o.write
    w("---\n")
    w("title: %s\n" % L["index_title"])
    w("description: %s\n" % yaml_str(L["index_desc"]))
    w("outline: false\n")
    w("---\n\n")
    w("<ProjectsIndex></ProjectsIndex>\n\n")
    w("## %s\n\n" % L["layer_heading"])
    for l in LAYERS:
        w("### %s\n\n%s\n\n" % (l[lang], l[lang + "_desc"]))
    w("::: tip\n%s\n:::\n\n" % L["matrix_note"])
    w("## %s\n\n" % L["matrix"])
    w("| %s | %s | %s | %s | %s | %s |\n|--------|------|------|------|------|--------|\n"
      % (L["col_project"], L["col_layer"], L["col_lang"], L["col_star"], L["col_fork"], L["col_tagline"]))
    for p in order:
        lay = next(x for x in LAYERS if x["id"] == p["layer"])
        w("| [%s](./%s) | %s | %s | %d | %d | %s |\n"
          % (p["name"], p["slug"], lay[lang], p["lang"], p["stars"], p["forks"], safe(p[lang]["tagline"])))
    w("\n")
    path = os.path.join(DOCS, "projects", "index.md") if lang == "en" else os.path.join(DOCS, "zh", "projects", "index.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(o.getvalue())
print("wrote projects index (en, zh)")

# ---------------- sidebars ----------------
for lang, fname in (("en", "sidebar.mjs"), ("zh", "sidebar.zh.mjs")):
    sb = ["// AUTO-GENERATED by tools/gen.py — do not edit by hand.",
          "export const projectsSidebar = ["]
    for l in LAYERS:
        items = [p for p in order if p["layer"] == l["id"]]
        sb.append("  {")
        sb.append('    text: "%s",' % l[lang])
        sb.append("    items: [")
        for p in items:
            sb.append('      { text: "%s", link: "%s/projects/%s" },'
                      % (p["name"].replace("Microsphere ", ""), PREFIX[lang], p["slug"]))
        sb.append("    ],")
        sb.append("  },")
    sb += ["]", ""]
    open(os.path.join(DOCS, ".vitepress", fname), "w", encoding="utf-8").write("\n".join(sb))
print("wrote sidebars (en, zh)")

# ---------------- theme data ----------------
js = {
    "layers": [dict(id=l["id"], en=l["en"], zh=l["zh"], en_desc=l["en_desc"], zh_desc=l["zh_desc"]) for l in LAYERS],
    "projects": [
        dict(slug=p["slug"], name=p["name"], layer=p["layer"], stars=p["stars"], forks=p["forks"],
             lang=p["lang"], artifact=p.get("artifact"), bom=p.get("bom"), version=p.get("version"),
             en=p["en"], zh=p["zh"])
        for p in order
    ],
}
data_dir = os.path.join(DOCS, ".vitepress", "theme", "data")
os.makedirs(data_dir, exist_ok=True)
open(os.path.join(data_dir, "projects.json"), "w", encoding="utf-8").write(
    json.dumps(js, ensure_ascii=False, indent=2))
print("wrote projects.json (%d projects)" % len(order))
