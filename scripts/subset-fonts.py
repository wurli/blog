# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fonttools==4.62.1",
#   "brotli==1.2.0",
# ]
# ///

"""
Subset fonts to only include characters used in the built site.
Run after `zola build` to reduce font file sizes.
"""

import re
from pathlib import Path
from fontTools.subset import main as subset_main

ROOT = Path(__file__).parent.parent
PUBLIC = ROOT / "public"
FONTS_SRC = ROOT / "static" / "fonts"
FONTS_DST = PUBLIC / "fonts"

# Font files to subset (maps output name to source)
FONTS = [
    "CommitMonoNerdFont-Regular.woff2",
    "CommitMonoNerdFont-Bold.woff2",
    "CommitMonoNerdFont-Italic.woff2",
    "CommitMonoNerdFont-BoldItalic.woff2",
]


def get_used_chars():
    """Scan all HTML files for unique characters."""
    chars = set()
    for html_file in PUBLIC.rglob("*.html"):
        text = html_file.read_text(encoding="utf-8", errors="ignore")
        # Strip HTML tags to get just text content
        text = re.sub(r"<[^>]+>", " ", text)
        chars.update(text)

    # Always include basic ASCII printable range
    chars.update(chr(c) for c in range(0x20, 0x7F))

    return chars


def subset_font(src: Path, dst: Path, chars: set):
    """Subset a font to only include specified characters."""
    # Create unicodes string for pyftsubset
    unicodes = ",".join(f"U+{ord(c):04X}" for c in sorted(chars))

    args = [
        str(src),
        f"--output-file={dst}",
        f"--unicodes={unicodes}",
        "--flavor=woff2",
        "--layout-features=*",  # Keep all OpenType features
        "--no-hinting",  # Smaller file, minimal quality loss on screen
    ]

    subset_main(args)


def main():
    chars = get_used_chars()
    print(f"Found {len(chars)} unique characters in site")

    for font_name in FONTS:
        src = FONTS_SRC / font_name
        dst = FONTS_DST / font_name

        if not src.exists():
            print(f"  Skipping {font_name} (source not found)")
            continue

        old_size = dst.stat().st_size if dst.exists() else 0
        subset_font(src, dst, chars)
        new_size = dst.stat().st_size

        reduction = (1 - new_size / old_size) * 100 if old_size else 0
        print(
            f"  {font_name}: {old_size // 1024}KB -> {new_size // 1024}KB ({reduction:.0f}% smaller)"
        )


if __name__ == "__main__":
    main()
