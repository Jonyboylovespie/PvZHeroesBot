import uiautomator2 as u2
from pathlib import Path
IMAGES_DIR = Path(__file__).parent / "Images"

def imageMatch():
    for p in IMAGES_DIR.iterdir():
        if p.is_file():
            match = d.image.match(str(p))
            if match["similarity"] > 0.99:
                return [p.name, match["point"]]
    return None

def reinstall():
    d.shell("pm clear com.ea.gp.pvzheroes")
    d.app_start("com.ea.gp.pvzheroes")

d = u2.connect()

reinstall()
while True:
    match = imageMatch()
    if match:
        match match[0]:
            case _:
                print(match[0])
                d.click(match[1][0], match[1][1])