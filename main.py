import uiautomator2 as u2
import time
import pytesseract
from pathlib import Path

IMAGES_DIR = Path(__file__).parent / "Images"
appName = "com.ea.gp.pvzheroes"
d = u2.connect()
#1440x2560 and 360dpi

# I need to set a resolution for the image match, cause resizing window breaks ts

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
        if ("been" in text and "rewarded" in text) or "granted" in text or "rapidata" in text or "answer questions to earn a reward" in text:
            break
    d.app_stop(appName)
    d.app_start(appName)

def birth():
    d.click(0.5, 0.51)
    for _ in range(7):
        time.sleep(0.5)
        d.click(0.25, 0.95)
    d.click(0.75, 0.95)
    d.click(0.9, 0.78)
    d.click(0.5, 0.55)

restartTimer = False
restartTime = time.time()
while True:
    if restartTimer and time.time() - restartTime > 40:
        restartTimer = False
        reinstall()
    match = imageMatch()
    if match:
        match match[0]:
            case "watchad.png":
                d.click(match[1][0], match[1][1])
                ad()
                restartTimer = True
                restartTime = time.time()
            case "birth.png":
                birth()
            case "connect.png":
                d.click(match[1][0], match[1][1])
                d.click(0.5, 0.5)
            case "continue.png":
                d.click(match[1][0], match[1][1])
                time.sleep(3)
            case "jonyboypie":
                d.click(match[1][0], match[1][1])
                d.click(0.5, 0.8)
                d.click(0.75, 0.6)
            case _:
                restartTimer = False
                d.click(match[1][0], match[1][1])