+++
title = "Tree-sitter grammar length as a measure language simplicity"
date = 2026-08-27
template = "post.html"
+++

I like simple programming languages, and it turns out a nice proxy for
simplicity is the number of lines in a treesitter grammer:

```
Lang    Grammar LOC
--------------------
Clojure       [528](https://github.com/sogaiu/tree-sitter-clojure/blob/master/grammar.js)
Lua           [634](https://github.com/tree-sitter-grammars/tree-sitter-lua/blob/main/grammar.js)
R             [786](https://github.com/r-lib/tree-sitter-r/blob/main/grammar.js)
Zig           [898](https://github.com/tree-sitter-grammars/tree-sitter-zig/blob/master/grammar.js)
Go            [983](https://github.com/tree-sitter/tree-sitter-go/blob/master/grammar.js)
Python      [1,229](https://github.com/tree-sitter/tree-sitter-python/blob/master/grammar.js)
C++         [1,603](https://github.com/tree-sitter/tree-sitter-cpp/blob/master/grammar.js)
Rust        [1,693](https://github.com/tree-sitter/tree-sitter-rust/blob/master/grammar.js)
```

> Accurate as at `2026-08-27`

Lua and R are probably my 2 favourite languages. I have a love-hate
relationship with Rust - and the hate tends to come down to issues caused by
language complexity. I use Python a lot but I don't like it much at all.

The moral of the story is what I already knew - **I should really try Zig**.


