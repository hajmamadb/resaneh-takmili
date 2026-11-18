# -*- coding: utf-8 -*-
import urllib.request, urllib.error, json, time

def req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request("http://localhost:6344" + path,
                               data=data, method=method,
                               headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(errors="replace")
    except Exception as e:
        return "ERR", str(e)

print("== delete U ==")
print(req("DELETE", "/collections/U?wait=true"))

print("\n== create U with prevent_unoptimized=true, small indexing_threshold ==")
cfg = {"vectors": {"size": 4, "distance": "Cosine"},
       "optimizer_config": {"prevent_unoptimized": True,
                            "indexing_threshold": 100,
                            "memmap_threshold": None}}
print(req("PUT", "/collections/U?wait=true", cfg))

print("\n== upsert 3 points (wait=true) ==")
st, d = req("POST", "/collections/U/points?wait=true",
            {"ids": [10, 11, 12],
             "vectors": [[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 0.9, 0.1, 0.2]],
             "payloads": [{"k": 1}, {"k": 2}, {"k": 3}]})
print(st, d)

print("\n== count ==")
print(req("POST", "/collections/U/points/count", {"exact": True}))

print("\n== retrieve ids 10-12 ==")
print(req("POST", "/collections/U/points", {"ids": [10, 11, 12], "with_payload": True}))

print("\n== collection info ==")
st, d = req("GET", "/collections/U")
res = d.get("result", {})
print("points:", res.get("points_count"), "segments:", res.get("segments_count"),
      "indexed:", res.get("indexed_vectors_count"), "queue:", res.get("update_queue"),
      "status:", res.get("status"))

print("\n== payload index (force on-disk write of payload) ==")
print(req("PUT", "/collections/U/index?wait=true", {"field_name": "k", "field_schema": "integer"}))
time.sleep(2)
print("count after index:", req("POST", "/collections/U/points/count", {"exact": True}))

print("\n== search test ==")
print(req("POST", "/collections/U/points/search",
          {"vector": [0.1, 0.2, 0.3, 0.4], "limit": 5, "with_payload": True}))
