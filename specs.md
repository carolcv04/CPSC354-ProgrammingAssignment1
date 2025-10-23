# Calculator Parser Specifications

## Overview

This calculator parses and evaluates mathematical expressions using a **custom Lark grammar** and a **transformer**. It supports:

- Arithmetic operations (`+`, `-`, `*`, `/`, `^`)
- Unary negation (`-`)
- Logarithms with custom bases (`log <arg> base <base>`)
- Variables and assignment (`x = expression`)

The calculator reads an equation from the command line:

```bash
python3 calculator_cfg.py "equation HERE"
```
