# -*- coding: utf-8 -*-
"""Get exact embedding dimensions for each model."""
import json
import urllib.request

BASE = "https://ai.ismc.ir/api"
API_KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"

def embed(model, text="سلام دنیا این یک تست ابعادی است"):
    req = urllib.request.Request(
        BASE + "/v1/embeddings",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        data=json.dumps({"model": model, "input": [text]}).encode("utf-8"),
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    vec = d["data"][0]["embedding"]
    return len(vec), d.get("usage"), d.get("model")

for m in ["Qwen3-Embedding-4B", "Qwen3-Embedding-0.6B", "bge-m3"]:
    try:
        dims, usage, echoed = embed(m)
        print(f"{m}: dims={dims}  usage={usage}  echoed_model={echoed}")
    except Exception as e:
        print(f"{m}: ERROR {e}")
