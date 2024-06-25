# ansi-python
- Get colors and styles in your console. Inspired by [colors.js](https://www.npmjs.com/package/colors)
- Too lazy to upload this to pip rn. Download `/ansi` directory and import it directly.

# Functions:
### Text colors (`ansi.fg.<color>`)
- `black()`
- `purple()`
- `red()`
- `green()`
- `yellow()`
- `blue()`
- `magenta()`
- `cyan()`
- `white()`
- `grey()` or `gray()`

### Text colors but brighter (`ansi.fg.<color>`)
- `bright_red()`
- `bright_green()`
- `bright_yellow()`
- `bright_blue()`
- `bright_magenta()`
- `bright_cyan()`
- `bright_white()`

### Background colors (`ansi.bg.<color>`)
- `black()`
- `purple()`
- `red()`
- `green()`
- `yellow()`
- `blue()`
- `magenta()`
- `cyan()`
- `white()`
- `gray()` or `grey()`

### Background colors but brighter (`ansi.bg.<color>`)
- `bright_red()`
- `bright_green()`
- `bright_yellow()`
- `bright_blue()`
- `bright_magenta()`
- `bright_cyan()`
- `bright_white()`

### Style (`ansi.<style>`)
- `reset()`
- `bold()`
- `dim()`
- `italic()`
- `underline()`
- `inverse()`
- `hidden()`
- `strikethrough()`

### Extras (`ansi.<extras>`)
- `rainbow()`
- `zebra()`
- `trap()`
- `freaky()`

# Example
```py
import ansi 

# colors >
print(ansi.fg.black("Indent"))    # outputs black
print(ansi.bg.purple("Vein"))     # outputs purple

# style >
print(ansi.italic('hello?'))      # outputs italic
print(ansi.inverse('Boo!'))       # outputs inverse

# extras >
print(ansi.zebra('crossing'))     # outputs zebra color
print(ansi.freaky('freaky vro'))  # outputs 𝓯𝓻𝓮𝓪𝓴𝔂 style
```
