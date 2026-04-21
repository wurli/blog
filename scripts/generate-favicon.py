# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pillow==11.2.1",
# ]
# ///

"""Generate favicon: 'J' in CommitMono on #002b36 background."""

from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.ellipse((0, 0, 255, 255), fill="#002b36")
text = "J"
font = ImageFont.truetype("static/fonts/CommitMonoNerdFont-Bold.woff2", 180)

bbox = draw.textbbox((0, 0), text, font=font)
x = (256 - bbox[2] + bbox[0]) // 2 - bbox[0]
y = (256 - bbox[3] + bbox[1]) // 2 - bbox[1]

draw.text((x, y), text, font=font, fill="#ffffff")
img.save("static/favicon.ico", sizes=[(16, 16), (32, 32)])
