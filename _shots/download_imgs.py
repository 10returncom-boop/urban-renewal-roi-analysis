import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    ("https://aka.doubaocdn.com/s/8o2Mksd6G4", r"D:\_WWW_325\urban_renewal_roi_analysis\_shots\new_img1.jpg"),
    ("https://aka.doubaocdn.com/s/S3r6JwkUbL", r"D:\_WWW_325\urban_renewal_roi_analysis\_shots\new_img2.jpg"),
]

for url, path in urls:
    print(f"Downloading {url}...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx) as resp:
        data = resp.read()
        with open(path, "wb") as f:
            f.write(data)
        print(f"  Saved {path} ({len(data)} bytes)")

print("Done!")
