# FastPlot

Create publication-quality plots with a simple interface over matplotlib.
Are you bored of copying and pasting the code to make a plot every time? Try this!

This module provides only one (highly customizable) function to plot some data. It use `matplotlib` in its internal, but, using arguments, helps in setting all graphical and plot paramenters (tick rotate, font, size, etc.).

For information about this Readme file and this tool please write to
[martino.trevisan@polito.it](mailto:martino.trevisan@polito.it)

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
 * `CDF`: plot a CDF given the samples. `data` must be a list of scalars.
 * `CDF_multi`: plot many CDFs given the samples. `data` must be a list of two-sized tuples like (name, [samples]). `name` is used in the legend.
  * `boxplot`: plota boxplot given the samples. `data` must be a list of two-sized tuples like (name, [samples]). `name` is used in the xticks labels.
  * `timeseries`: plot a time series. `data` must be a pandas series, with a DateTime index.
  * `timeseries_multi`: plot many time series. `data` must be a list of two-sized tuples like (name, timeseries). `name` is used in the legend.
   * `timeseries_stacked`: plot many time series, stacked. `data` must be a pandas dataframe, with a DateTime index. Each column will be plotted stacked to the others. Column names are used in the legend.
   * `bars`: plot a bar plot. `data` must be a list of (name, value). `name` is used for the legend.
   * `bars_multi`: plot grouped bars. `data` must be a padas dataframe. Each row is results in a group of bars, while columns determine bars within each group.
   
   ## Arguments
   Arguments of the `plot` function are divided in many categories. Only `core` are mandatory.
   
**Core**
* `data`: the input data to plot
* `path`: the output path for the plot
* `mode`: which type of plot to create (lines, bars, etc.). More details later. Default `line`

**Look**
* `style`: which graphical style to use. Can be `serif`, `sans-serif` or `latex`. For latex, it enables matplotlib latex engine. Default `sans-serif`
* `figsize`: the size of the output figure. Default: `(4,2.25)`
* `cycler`: the style cycler to use. By default, it changes across main colors, and different linestyles. Change it if you want to change color, line, or point style. I provide some useful cycler in the code (see Cycler section). Default `CYCLER_LINES`
* `fontsize`: just the overall font size. Default `11`

**Grid**
* `grid`: whether to display grid. Default `False`
* `grid_which`: ticks for the grid (major/minor). Default `major`
* `grid_axis`: axis for the grid. Default `both`
* `grid_linestyle`: gird linestyle. Default `dotted`
* `grid_color`: grid color. Default `black`

**Scale**
* `xscale`: scale for x axis (linear/log). Default `linear`
* `yscale`: scale for y axis (linear/log). Default `linear`
         
**Axis**
* `xlim`: Optional x limit, as a tuple (low, high)
* `ylim`: Optional y limit, as a tuple (low, high)
* `xlabel`: Label for x axis
* `ylabel`: Label for y axis
* `xticks`: Custom x ticks, in the form ([x1, x2, ...], [label1, label2, ...])
* `yticks`:  Custom y ticks, in the form ([y1, y2, ...], [label1, label2, ...])
* `xticks_rotate`: Rotation for x ticks. Default `0`
* `yticks_rotate`:  Rotation for y ticks. Default `0`
* `xticks_fontsize`: X ticks font size. Default `medium`
* `yticks_fontsize`: Y ticks font size. Default `medium`
* `xtick_direction`: xtick marker direction. Default 'in'
* `xtick_width`: xticks marker width. Default `1`
* `xtick_length`:  xticks marker length. Default `4`
* `ytick_direction`:  ytick marker direction. Default 'in'
* `ytick_width`: yticks marker width. Default `1`
* `ytick_length`:  yticks marker length. Default `4` 
         
**Legend**
* `legend`: whether to show the legend. Default `False`
* `legend_loc`: location for legend. Default `best`
* `legend_ncol`: number of columns. Default `1`
* `legend_fontsize`: legend fontsize. Default `medium`
* `legend_border`: whether to show legend border. Default `False`
* `legend_frameon`: whether to show legend frame. Default `True`

**Specific**
This arguments are specific for some `modes`.
* `linewidth`: linewidth when lines are used. Default: `1`
* `boxplot_sym`: symbol for outliers in boxplots. Default `''`
* `boxplot_whis`: whisker spec for boxplot.  Default `[5,95]`
* `timeseries_format`: format for printing dates in timeseries. Default `%Y/%m/%d`
* `bars_width`: width of bars when bars are plotted. Default `0.6`
* `callback`: function to call instead of plotting, when `mode=callback`
   
 ## Cyclers
 
 ## Examples
 Coming
  




