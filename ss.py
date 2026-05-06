import uiautomator2 as u2

SIZE = 50
Xpercent = 0.9
Ypercent = 0.68

d = u2.connect()
img = d.screenshot()
w, h = img.size
center_x, center_y = w * Xpercent, h * Ypercent
offset = SIZE / 2
left = center_x - offset
top = center_y - offset
right = center_x + offset
bottom = center_y + offset

gotit_template = img.crop((left, top, right, bottom))
gotit_template.save("image.png")