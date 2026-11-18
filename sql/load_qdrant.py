# -*- coding: utf-8 -*-
"""Phase 6d: load vectors.json into Qdrant resaname_knowledge_v1 (standalone, no Docker).
Uses ijson streaming (vectors.json is 644MB).
point_id = hash of chunk_id as uint64 (Qdrant requires uint or UUID).
"""
import ijson, json, urllib.request, urllib.error, sys, time, zlib

QDRANT = "http://localhost:6333"
COLL = "resaname_knowledge_v1"
DIM = 2560
BATCH = 32

def req(method, path, body=None):
    data = json.dumps(body).encode('utf-8') if body is not None else None
    r = urllib.request.Request(QDRANT + path, data=data, method=method,
                               headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r, timeout=120) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', 'replace')[:400]

# wait for qdrant
for i in range(15):
    try:
        with urllib.request.urlopen(QDRANT + "/healthz", timeout=3) as r:
            if r.status == 200:
                print("qdrant up", flush=True); break
    except Exception:
        time.sleep(2)
else:
    print("Qdrant not reachable at localhost:6333"); sys.exit(1)

# ensure collection
st, d = req("GET", f"/collections/{COLL}")
if st != 200:
    print("creating collection", flush=True)
    st, d = req("PUT", f"/collections/{COLL}", {"vectors": {"size": DIM, "distance": "Cosine"}})
    print("create:", st, str(d)[:200], flush=True)

# stream and load
n = 0
loaded = 0
t0 = time.time()
batch = []

def flush(batch):
    global loaded
    if not batch:
        return
    # Qdrant upsert format: {ids:[], vectors:[], payloads:[]}
    payload = {
        "ids": [p["id"] for p in batch],
        "vectors": [p["vector"] for p in batch],
        "payloads": [p["payload"] for p in batch],
    }
    st, d = req("POST", f"/collections/{COLL}/points?wait=true", payload)
    if st not in (200, 201):
        print(f"  batch FAILED {st}: {str(d)[:200]}", flush=True)
        time.sleep(3)
        st, d = req("POST", f"/collections/{COLL}/points?wait=true", payload)
        if st not in (200, 201):
            print(f"  retry FAILED @{loaded}: {st} {str(d)[:200]}", flush=True)
            sys.exit(1)
    loaded += len(batch)
    el = time.time() - t0
    print(f"  {loaded} points  {el:.0f}s  ({loaded/max(el,1):.1f} pts/s)", flush=True)

with open('vectors.json', 'rb') as f:
    for p in ijson.items(f, 'item'):
        # uint64 from chunk_id
        pid = p['point_id']
        uid = zlib.crc32(pid.encode('utf-8')) & 0xFFFFFFFF
        # extend to make more unique
        uid2 = (zlib.crc32(pid.encode('utf-8') + b'::salt') & 0xFFFFFFFF) << 32 | uid
        # ijson returns floats as Decimal — convert to plain float
        vec = [float(x) for x in p['vector']]
        batch.append({"id": uid2, "vector": vec, "payload": p['payload']})
        n += 1
        if len(batch) >= BATCH:
            flush(batch)
            batch = []

if batch:
    flush(batch)

# verify
st, d = req("POST", f"/collections/{COLL}/points/count", {"exact": True})
cnt = d.get("result", {}).get("count") if isinstance(d, dict) else d
print(f"server point count: {cnt}", flush=True)
print(f"streamed: {n} points, loaded: {loaded}", flush=True)
print("DONE", flush=True)
