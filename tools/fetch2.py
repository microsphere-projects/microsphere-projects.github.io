import urllib.request, base64, os, json

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(OUT, exist_ok=True)

REPOS = [
    "microsphere-security", "microsphere-dynamic", "microsphere-logging",
    "microsphere-mybatis", "microsphere-netflix", "microsphere-hibernate",
    "microsphere-multiactive", "microsphere-resilience4j", "microsphere-alibaba-sentinel",
    "microsphere-alibaba-druid", "microsphere-tools", "microsphere-dubbo",
    "microsphere-tomcat", "microsphere-etcd", "microsphere-jakarta",
    "microsphere-microprofile", "microsphere-ai", "microsphere-devops",
    "microsphere-devops-ui", "microsphere-test", "microsphere-apidocs",
    "microsphere-spring-cloud",
]

def get(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "curl/8",
        "Accept": "application/vnd.github+json",
    })
    return json.loads(urllib.request.urlopen(req, timeout=25).read().decode("utf-8"))

for r in REPOS:
    dest = os.path.join(OUT, r + ".md")
    if os.path.exists(dest) and os.path.getsize(dest) > 200:
        print("skip", r); continue
    try:
        d = get(f"https://api.github.com/repos/microsphere-projects/{r}/readme")
        content = base64.b64decode(d["content"]).decode("utf-8", "replace")
        open(dest, "w", encoding="utf-8").write(content)
        print(f"OK {r}: {len(content)} chars")
    except Exception as e:
        print(f"FAIL {r}: {e}")
