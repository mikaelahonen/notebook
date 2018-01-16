# d3-examples
Examples of interactive graphics made with d3 javascript library.

[d3js.org tutorial](https://d3js.org/#introduction)

<b>svg.html</b>
Examples of html svg elements without any javascript.
Copied from [here](https://www.dashingd3js.com/basic-building-blocks).

## D3 Functions

### select
Get an html element to a variable.

### append
svg: Frame for objects.
g: Group. Not D3 specific.
circle: A round object.

## Vector graphics in HTML

### Path
Combine lines, curves and arcs to create complex shapes.
[Mozilla tutorial](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths)

The instructions are stored in d attribute of <path />:
* M: Move to a coordinate location
** `M x y` or `m dx dxy`
* L: Line to command
** Normal line `L x y` or `l dx dy`
** Horizontal line `H x`
** Vertical line `V y`
* Z: Close path
** Draw line to start of the path `Z`

Upper case command specifies absolute coordinate in page,
lower case specifies relative coordinates. M and m for example.
Coordinates are always unitless.
