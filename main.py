import uiautomator2 as u2
import time
import pytesseract
from pathlib import Path

IMAGES_DIR = Path(__file__).parent / "Images"
appName = "com.ea.gp.pvzheroes"

def imageMatch():
    for p in IMAGES_DIR.iterdir():
        if p.is_file():
            match = d.image.match(str(p))
            if match["similarity"] > 0.99:
                return [p.name, match["point"]]
    return None

def reinstall():
    d.shell(f"pm clear {appName}")
    d.app_start(appName)

def ad():
    initialTime = time.time()
    while time.time() - initialTime < 35:
        img = d.screenshot()
        text = pytesseract.image_to_string(img).lower()
        print(text)
        if ("been" in text and "rewarded" in text) or "granted" in text or "rapidata" in text:
            break
    d.app_stop(appName)
    d.app_start(appName)
    
    

d = u2.connect()

while True:
    match = imageMatch()
    if match:
        print(match[0])
        match match[0]:
            case "watchad.png":
                d.click(match[1][0], match[1][1])
                ad()
            case _:
                d.click(match[1][0], match[1][1])