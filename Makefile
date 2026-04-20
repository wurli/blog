.PHONY: build serve clean

# Full build with font subsetting (for production/CI)
build:
	zola build
	uv run scripts/subset-fonts.py

# Dev server (uses full fonts, no subsetting)
serve:
	zola serve

clean:
	rm -rf public/
