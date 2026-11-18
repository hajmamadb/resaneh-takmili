# -*- coding: utf-8 -*-
"""Download qdrant.exe using DoH (dns.google) to bypass local DNS block on github.com."""
import socket, urllib.request, json, os, ssl

def doh_resolve(host):
    url = f"https://dns.google/resolve?name={host}&type=A"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    d = json.load(urllib.request.urlopen(req, timeout=15))
    ips = [a["data"] for a in d.get("Answer", []) if a.get("type") == 1]
    if not ips:
        raise socket.gaierror(f"DoH: no A record for {host}")
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (ip, 443)) for ip in ips]

_orig = socket.getaddrinfo
def patched(host, port, *a, **kw):
    if host in ("github.com", "objects.githubusercontent.com", "raw.githubusercontent.com"):
        try:
            return doh_resolve(host)
        except Exception:
            pass
    return _orig(host, port, *a, **kw)
socket.getaddrinfo = patched

url = "https://github.com/qdrant/qdrant/releases/download/v1.20.0/qdrant-x86_64-pc-windows-msvc.zip"
out = r"D:\رسانامه تکمیلی\qdrant\qdrant.zip"
if os.path.exists(out):
    os.remove(out)
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "*/*"})
ctx = ssl.create_default_context()
resp = urllib.request.urlopen(req, timeout=300, context=ctx)
print("final url:", resp.geturl())
print("content-length:", resp.headers.get("Content-Length"))
n = 0
with open(out, "wb") as f:
    while True:
        b = resp.read(1 << 16)
        if not b: break
        f.write(b); n += len(b)
print("downloaded", n, "bytes")
print("on disk:", os.path.getsize(out))
