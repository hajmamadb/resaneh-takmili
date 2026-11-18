# -*- coding: utf-8 -*-
import urllib.request, urllib.error, json, time, zlib

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

# 1. delete test collection
print("== delete collection ==")
print(req("DELETE", "/collections/resaname_knowledge_v1?wait=true"))

# 2. recreate
print("\n== create ==")
cfg = {"vectors": {"size": 2560, "distance": "Cosine"}}
print(req("PUT", "/collections/resaname_knowledge_v1?wait=true", cfg))

# 3. upsert 3 points
ids, vecs, pays = [], [], []
for i in range(3):
    pid = f"DIAG2-{i}"
    u = zlib.crc32(pid.encode()) & 0xFFFFFFFF
    u2 = (zlib.crc32(pid.encode() + b"::salt") & 0xFFFFFFFF) << 32 | u
    ids.append(u2)
    vecs.append([0.01 * (i + 1) + 0.0001 * j for j in range(2560)])
    pays.append({"document_id": f"DIAG2-{i}", "section_id": None, "n": i})
st, d = req("POST", "/collections/resaname_knowledge_v1/points?wait=true",
            {"ids": ids, "vectors": vecs, "payloads": pays})
print("\n== upsert ==", st, d)

# 4. count right away
st, d = req("POST", "/collections/resaname_knowledge_v1/points/count", {"exact": True})
print("count t+0:", st, d)

# 5. force optimize (flush)
st, d = req("POST", "/collections/resaname_knowledge_v1/points/optimize?wait=true", None)
print("optimize:", st, str(d)[:300])

time.sleep(2)
st, d = req("POST", "/collections/resaname_knowledge_v1/points/count", {"exact": True})
print("count after optimize:", st, d)

st, d = req("GET", "/collections/resaname_knowledge_v1")
res = d.get("result", {})
print("points_count:", res.get("points_count"), "segments:", res.get("segments_count"),
      "status:", res.get("status"), "queue:", res.get("update_queue"))

# 6. retrieve by id
st, d = req("POST", "/collections/resaname_knowledge_v1/points",
            {"ids": [ids[0]], "with_payload": True, "with_vector": False})
print("retrieve:", st, json.dumps(d, ensure_ascii=False)[:400])
