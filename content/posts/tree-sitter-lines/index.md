+++
title = "Tree-sitter grammar length as a measure of language simplicity"
date = 2026-08-27
template = "post.html"
+++

I like simple programming languages, and it turns out a nice proxy for
simplicity is the number of lines in a treesitter grammar:

| Lang        | Grammar LOC | `grammar.js`                                                                                      |
| ----------- | --:         | --                                                                                                |
| Clojure     | 528         | [tree-sitter-clojure](https://github.com/sogaiu/tree-sitter-clojure/blob/master/grammar.js)       |
| Lua         | 634         | [tree-sitter-lua](https://github.com/tree-sitter-grammars/tree-sitter-lua/blob/main/grammar.js)   |
| R           | 786         | [tree-sitter-r](https://github.com/r-lib/tree-sitter-r/blob/main/grammar.js)                      |
| Zig         | 898         | [tree-sitter-zig](https://github.com/tree-sitter-grammars/tree-sitter-zig/blob/master/grammar.js) |
| Go          | 983         | [tree-sitter-go](https://github.com/tree-sitter/tree-sitter-go/blob/master/grammar.js)            |
| Python      | 1,229       | [tree-sitter-python](https://github.com/tree-sitter/tree-sitter-python/blob/master/grammar.js)    |
| C++         | 1,603       | [tree-sitter-cpp](https://github.com/tree-sitter/tree-sitter-cpp/blob/master/grammar.js)          |
| Rust        | 1,693       | [tree-sitter-rust](https://github.com/tree-sitter/tree-sitter-rust/blob/master/grammar.js)        |

> Figures as of `2026-08-27`

Lua and R are probably my 2 favourite languages. I have a love-hate
relationship with Rust - and the hate tends to come down to issues caused by
language complexity. I use Python a lot but I wish I didn't.

Perhaps the moral of the story is what I already knew - **I should really try Zig**.

