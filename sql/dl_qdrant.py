# -*- coding: utf-8 -*-
import urllib.request, os, sys

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        print("redirect ->", headers.get('Location'))
        return None

url = "https://github.com/qdrant/qdrant/releases/download/v1.20.0/qdrant-x86_64-pc-windows-msvc.zip"
out = r"D:\رسانامه تکمیلی\qdrant\qdrant.zip"
# Use default opener (follows redirects)
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "*/*"})
opener = urllib.request.build_opener()
resp = opener.open(req, timeout=300)
print("final url:", resp.geturl())
print("content-length:", resp.headers.get('Content-Length'))
n = 0
with open(out, "wb") as f:
    while True:
        b = resp.read(1 << 16)
        if not b: break
        f.write(b); n += len(b)
print("downloaded", n, "bytes")
print("on disk:", os.path.getsize(out))
