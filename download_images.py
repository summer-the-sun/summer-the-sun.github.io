"""Downloads every image your Squarespace site used into the images/ folder.
Run this ONCE from inside this folder, BEFORE cancelling Squarespace:
    python3 download_images.py        (on Windows: python download_images.py)
"""
import json, os, urllib.request
here = os.path.dirname(os.path.abspath(__file__))
m = json.load(open(os.path.join(here, "images", "manifest.json")))
ok = 0
for i, (path, url) in enumerate(m.items(), 1):
    dest = os.path.join(here, path)
    if os.path.exists(dest):
        ok += 1; continue
    if url.startswith("//"): url = "https:" + url
    try:
        req = urllib.request.Request(url + "?format=1500w", headers={"User-Agent": "Mozilla/5.0"})
        open(dest, "wb").write(urllib.request.urlopen(req, timeout=30).read())
        ok += 1; print(f"[{i}/{len(m)}] {path}")
    except Exception as ex:
        print(f"[{i}/{len(m)}] FAILED {url}: {ex}")
print(f"Done: {ok}/{len(m)} images saved. Re-run if any failed.")
