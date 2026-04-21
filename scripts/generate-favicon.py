# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pillow==11.2.1",
# ]
# ///

"""Generate favicons: 'J' in CommitMono on #002b36 background.

Outputs:
- static/favicon.ico             (16, 32 — browser tab)
- static/apple-touch-icon.png    (180 — iOS home screen)
- static/android-chrome-192x192.png  (Android/PWA)
- static/android-chrome-512x512.png  (Android/PWA)
"""

from PIL import Image, ImageDraw, ImageFont

BG = "#002b36"
FG = "#ffffff"
FONT_PATH = "static/fonts/CommitMonoNerdFont-Bold.woff2"
TEXT = "J"


def render(size: int, *, circle: bool) -> Image.Image:
    """Render the 'J' glyph centered. Circle masked for .ico; square (no
    transparency) for iOS/Android, which dislike transparent touch icons."""
    if circle:
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.ellipse((0, 0, size - 1, size - 1), fill=BG)
    else:
        img = Image.new("RGB", (size, size), BG)
        draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(FONT_PATH, int(size * 180 / 256))
    bbox = draw.textbbox((0, 0), TEXT, font=font)
    x = (size - bbox[2] + bbox[0]) // 2 - bbox[0]
    y = (size - bbox[3] + bbox[1]) // 2 - bbox[1]
    draw.text((x, y), TEXT, font=font, fill=FG)
    return img


# Browser favicon: multi-size ICO with transparent circle.
render(256, circle=True).save("static/favicon.ico", sizes=[(16, 16), (32, 32)])

# iOS home screen: 180x180, opaque.
render(180, circle=False).save("static/apple-touch-icon.png")

# Android / PWA.
render(192, circle=False).save("static/android-chrome-192x192.png")
render(512, circle=False).save("static/android-chrome-512x512.png")
