.PHONY: build serve clean

# Full build with font subsetting (for production/CI)
build:
	uv run scripts/generate-favicon.py
	zola build
	uv run scripts/subset-fonts.py

# Dev server (uses full fonts, no subsetting)
serve:
	zola serve -O

clean:
	rm -rf public/
