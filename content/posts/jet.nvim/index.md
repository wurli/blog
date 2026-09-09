+++
title = "jet.nvim: a Jupyter kernel supervisor for Neovim ✈️"
date = 2026-09-09
template = "post.html"
image = "ui.png"
+++

{{ video(src="jet-nvim.mp4") }}

Repo: <https://github.com/wurli/jet.nvim>

## Features

*   A repl which runs in Neovim's built-in terminal
*   An LSP server which provides live completions from the kernel
*   A Lua API with fine-grained control over running kernels, down to the level
    of individual Jupyter messages
*   Ability to connect to kernel sessions running outside of Neovim
*   AI-friendly: agents can use the Jet CLI to interact with your kernel
    sessions
*   Detailed (non-vibed) vimdoc documentation
*   Plug and play - No remote plugin stuff. No python requirements. 

**Not yet implemented**
*   Notebooks
*   Windows support (contributions welcome!)

## Why jet.nvim?

No existing Jupyter plugins did what I wanted:

- I don't want to think about setting up Python infrastructure for every
  project which uses a Jupyter kernel. Stuff should just work.
- I want a more native-feeling repl than other plugins could provide
- I want to be able to hook into Jupyter mechanisms such as 'comms' to expose
  non-standard features in Neovim, e.g. the Ark R Kernel's LSP server
- I want a Lua API which is well documented and typed
- I wanted a Neovim plugin for the Ark R kernel (this now
  [exists](https://github.com/wurli/jet.ark) as a jet.nvim extension)

jet.nvim achieves all this stuff by building on
[Jet](https://github.com/wurli/jet), a custom Rust backend built to power this
plugin, but which does some other sick stuff too.

## jet.nvim is bare-bones

There are a billion different kernels out there - jet.nvim doesn't favour any
particular one. Instead, jet.nvim aims to provide tools which can be used to
create full-featured extension plugins for R, Python, Julia, etc. Existing
extensions I'm already using are [jet.ark](https://github.com/wurli/jet.ark)
(R) and [jet.ipy](https://github.com/wurli/jet.ipy) (Python).

Benefits of this architecture:

- A small scope will allow jet.nvim to reach maturity much faster
- Niche features (and associated code churn) can live in extension plugins,
  affecting only the folks who opt in

## Why Jupyter?

Jupyter != notebooks. Jupyter is a standard/protocol which interactive
languages can use to tell editors about state and execution results. It's cool.
Jupyter kernels wrap interactive languages to implement the protocol; frontends
need to implement a Jupyter 'client' to talk to kernels (this is non-trivial
because you have to handle ØMQ, tonnes of different message types, etc).
jet.nvim implements a Jupyter client using Rust for low-level stuff and
Neovim's Lua for the high-level API. jet.nvim extensions can now build on this
foundation to talk to kernels and implement language-specific behaviour which
was previously not possible. E.g. [jet.ark](https://github.com/wurli/jet.ark)
implements a plots pane where plots automatically redraw to fit the window
dimensions. Similarly, [jet.ipy](https://github.com/wurli/jet.ipy) silently
updates the Pandas setting which controls terminal width whenever the nvim
terminal window is resized.

## jet.nvim needs _you_!

Testers wanted! I've been dogfooding this plugin for like 2 months and it works
very nicely, but I've only been using it in anger for Python and R. All
feedback is very appreciated, but especially if you use Julia or some other
esoteric kernel. No gripe is too small to report!

-------

> Originally [posted on
> Reddit](https://www.reddit.com/r/neovim/comments/1wa47va/jetnvim_a_jupyter_kernel_supervisor_for_neovim/)
> on 7 September 2026
