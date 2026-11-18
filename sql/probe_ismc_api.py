# -*- coding: utf-8 -*-
"""Probe ismc.ir API: discover auth scheme, embedding endpoint, response format, dims."""
import json
import urllib.request
import urllib.error

BASE = "https://ai.ismc.ir/api"
API_KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"

def try_url(url, headers=None, data=None, method="GET"):
    """Try a URL and print status + first 500 chars of body."""
    req = urllib.request.Request(url, headers=headers or {}, method=method)
    if data is not None:
        req.data = json.dumps(data).encode("utf-8")
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            body = r.read().decode("utf-8", errors="replace")
            print(f"  [{r.status}] {url}")
            print(f"  body[:500]: {body[:500]}")
            return r.status, body
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"  [{e.code}] {url}")
        print(f"  body[:300]: {body[:300]}")
        return e.code, body
    except Exception as e:
        print(f"  [ERR] {url}: {e}")
        return None, str(e)

print("=== 1. Root / base ===")
try_url(BASE)
print()
print("=== 2. /models (no auth) ===")
try_url(BASE + "/models")
print()
print("=== 3. /models (Bearer) ===")
try_url(BASE + "/models", headers={"Authorization": f"Bearer {API_KEY}"})
print()
print("=== 4. /v1/models (OpenAI-compat, Bearer) ===")
try_url(BASE + "/v1/models", headers={"Authorization": f"Bearer {API_KEY}"})
print()
print("=== 5. /openai/v1/models ===")
try_url(BASE + "/openai/v1/models", headers={"Authorization": f"Bearer {API_KEY}"})
print()
print("=== 6. /embeddings (OpenAI-compat shape, Bearer) ===")
try_url(
    BASE + "/embeddings",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    data={"model": "Qwen3-Embedding-0.6B", "input": ["سلام", "test"]},
    method="POST",
)
print()
print("=== 7. /v1/embeddings ===")
try_url(
    BASE + "/v1/embeddings",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    data={"model": "Qwen3-Embedding-0.6B", "input": ["سلام", "test"]},
    method="POST",
)
print()
print("=== 8. /embed (alternative) ===")
try_url(
    BASE + "/embed",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    data={"model": "Qwen3-Embedding-0.6B", "input": ["سلام"]},
    method="POST",
)
print()
print("=== 9. /api/v1/embeddings (double api) ===")
try_url(
    "https://ai.ismc.ir/api/v1/embeddings",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    data={"model": "Qwen3-Embedding-0.6B", "input": ["سلام"]},
    method="POST",
)
print()
print("=== 10. /api/v1/models ===")
try_url("https://ai.ismc.ir/api/v1/models", headers={"Authorization": f"Bearer {API_KEY}"})
