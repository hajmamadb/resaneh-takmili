# -*- coding: utf-8 -*-
import urllib.request, urllib.error, json, time

def req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request("http://localhost:6333" + path,
                               data=data, method=method,
                               headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(errors="replace")
    except Exception as e:
        return "ERR", str(e)

print("== healthz ==")
print(req("GET", "/healthz"))

print("\n== collections ==")
print(req("GET", "/collections"))

print("\n== PUT collection (recreate, wait=true) ==")
cfg = {"vectors": {"size": 2560, "distance": "Cosine"},
       "hnsw_config": {"m": 16, "ef_construct": 100}}
print(req("PUT", "/collections/resaname_knowledge_v1?wait=true", cfg))

print("\n== status after create ==")
print(req("GET", "/collections/resaname_knowledge_v1"))

print("\n== upsert 3 test points (wait=true) ==")
import zlib
ids = []
vecs = []
pays = []
for i in range(3):
    pid = f"TEST-POINT-{i}"
    u = zlib.crc32(pid.encode()) & 0xFFFFFFFF
    u2 = (zlib.crc32(pid.encode() + b"::salt") & 0xFFFFFFFF) << 32 | u
    ids.append(u2)
    vecs.append([0.01 * (i + 1) + 0.0001 * j for j in range(2560)])
    pays.append({"document_id": f"TEST-{i}", "section_id": f"TEST-SEC-{i}", "note": "diag"})
st, d = req("POST", "/collections/resaname_knowledge_v1/points?wait=true",
            {"ids": ids, "vectors": vecs, "payloads": pays})
print(st, d)

print("\n== wait 2s, count ==")
time.sleep(2)
st, d = req("POST", "/collections/resaname_knowledge_v1/points/count", {"exact": True})
print("count:", st, d)

print("\n== count with wait=true param ==")
st, d = req("POST", "/collections/resaname_knowledge_v1/points/count?wait=true", {"exact": True})
print("count2:", st, d)

print("\n== retrieve test point by id ==")
st, d = req("POST", "/collections/resaname_knowledge_v1/points",
            {"ids": [ids[0]], "with_payload": True, "with_vector": False})
print(st, json.dumps(d, ensure_ascii=False)[:500])

print("\n== status after ==")
st, d = req("GET", "/collections/resaname_knowledge_v1")
res = d.get("result", d) if isinstance(d, dict) else d
print("points_count:", res.get("points_count"), "status:", res.get("status"), "update_queue:", res.get("update_queue"))
