# fastplot

Create publication-quality plots with a simple interface over matplotlib.
Are you bored of copying and pasting the code to make a plot every time? Try this!

This module provides only one (highly customizable) function to plot some data. It use `matplotlib` in its internal, but, using arguments, helps in setting all graphical and plot paramenters (tick rotate, font, size, etc.)

## Installation

Simply clone this repo or use:
```
pip install git+https://github.com/marty90/fastplot
```

Dependencies are: `matplotlib numpy pandas statsmodels`.

## Usage
This module has only one function, called `plot`. You must call it to make a plot, providing the data, the output file name, and other parameters. A figure will be saved on disk.

The most important arguments are:
* `data`: the actual data to plot
* `path`: the output path for the plot
* `mode`: which type of plot to create (lines, bars, etc.). More details later.
* `stlye`: which graphical style to use. Can be `serif`, `sans-serif` or `latex`.

## Modes

The modes are the type of plots fastplot allows to use. Some are simple (just a line), other are more advanced (bars, etc.).
 * `line`: plot a simple line. `data` must be a two-sized tuple of lists, for x and y. E.g., ([x1,x2,x3],[y1,y2,y3])
 * `line_multi`: plot multiple lines. Data must have the form [ (line1, ([x1,x2], [y1,y2])), (line2, ([x1,x2], [y1,y2]) ) ]. The names `line1` and `line2` are put in the legend.
 * `CDF`: plot 



