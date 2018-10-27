# fastplot

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
   
   ## Parameters
   Coming
   
   ## Examples
   Coming
  




