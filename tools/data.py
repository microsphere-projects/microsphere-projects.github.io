# -*- coding: utf-8 -*-
"""Aggregated bilingual project data."""

from projects_a import LAYERS
from projects_a import PROJECTS as _A
from projects_b import PROJECTS as _B

PROJECTS = _A + _B

# sanity: every project must carry both locales
for _p in PROJECTS:
    assert "en" in _p and "zh" in _p, _p["slug"]
    for _k in ("tagline", "summary", "features", "modules", "compat"):
        assert _k in _p["en"], (_p["slug"], _k)
        assert _k in _p["zh"], (_p["slug"], _k)
    assert len(_p["en"]["features"]) == len(_p["zh"]["features"]), _p["slug"]
    assert len(_p["en"]["modules"]) == len(_p["zh"]["modules"]), _p["slug"]
