---@param x Emph
function Emph(x)
	-- For emphasis (italic): wrap content with visible underscores while keeping italics
	local result = {}
	table.insert(result, pandoc.RawInline("html", "_<i>"))

	-- Add all content from the emphasis element
	for _, item in ipairs(x.content) do
		table.insert(result, item)
	end

	table.insert(result, pandoc.RawInline("html", "</i>_"))
	return result
end

---@param x Strong
function Strong(x)
	-- For strong (bold): wrap content with visible asterisks while keeping bold
	local result = {}
	table.insert(result, pandoc.RawInline("html", "**<b>"))

	-- Add all content from the strong element
	for _, item in ipairs(x.content) do
		table.insert(result, item)
	end

	table.insert(result, pandoc.RawInline("html", "</b>**"))
	return result
end
