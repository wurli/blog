# Fonts

This directory contains CommitMono Nerd Font in WOFF2 format.

## Converting OTF to WOFF2

Download OTF files from https://github.com/ryanoasis/nerd-fonts/releases, then convert:

```bash
pip install fonttools brotli

python3 -c "
from fontTools.ttLib import TTFont
for name in ['Regular', 'Bold', 'Italic', 'BoldItalic']:
    font = TTFont(f'CommitMonoNerdFont-{name}.otf')
    font.flavor = 'woff2'
    font.save(f'CommitMonoNerdFont-{name}.woff2')
"
```

## Safari/Edge PUA Fix

For Nerd Font icons (Private Use Area characters) to render in Safari/Edge, add to your CSS:

```css
pre, code {
  font-family: inherit;
}
```

Without this, browsers' default `font-family: monospace` on these elements breaks PUA character rendering from web fonts.
