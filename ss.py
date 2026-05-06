import uiautomator2 as u2

d = u2.connect()

# 1. Take the exact screenshot the library sees
img = d.screenshot()

# 2. Use the Weditor coordinates you know work (.5, .6)
# We will crop a box around the center of the screen
w, h = img.size
center_x, center_y = w * 0.75, h * 0.6

# Define how big you want the template to be (e.g., 200x80 pixels)
# This captures the "Got It" button perfectly from the source
left = center_x - 50
top = center_y - 50
right = center_x + 50
bottom = center_y + 50

# 3. Save this as your new master template
gotit_template = img.crop((left, top, right, bottom))
gotit_template.save("image.png")