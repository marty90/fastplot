# FastPlot

Create publication-quality plots with a simple interface over matplotlib.
Are you bored of copying and pasting the code to make a plot every time? Try this!

This module provides only one (highly customizable) function to plot some data. It uses `matplotlib` in its internal, but helps in setting all graphical and plot paramenters (tick rotate, font, size, etc.).

For information about this Readme file and this tool please write to
[martino.trevisan@polito.it](mailto:martino.trevisan@polito.it)

## Table of Content
<!---
Done with https://github.com/ekalinin/github-markdown-toc )
-->
   * [Installation](#installation)
   * [Usage](#usage)
   * [Modes](#modes)
   * [Arguments](#arguments)
   * [Cyclers](#cyclers)
   * [Examples](#examples)

## Installation

Simply clone this repo or use:
```
pip3 install fastplot
```

Dependencies are: `matplotlib numpy pandas statsmodels`. FastPlot requires updated versions of such libraries, so, in case of error try first to upgrade them.
For `serif` fonts you need `Times New Roman`, that, on Ubuntu, can be installed with:
```
sudo apt-get install msttcorefonts
```

## Usage
This module has only one function, called `plot`. You must call it to make a plot, providing the data, the output file name, and other parameters.
* If you provide a `path`, the figure will be saved on disk, and no value returned by the function.
* If `path` is `None`, the function returns the current `plt` object for further processing or interactive `show()`.
* Note: if you want to use the `show()` method of matplotlib for interactive view, you must import `pyplot` before importing `fastplot`, like:
```
import matplotlib.pyplot as plt
import fastplot
```

#### Usage with Jupyter Notebook
In this way, you can run `fastplot` also inside a Jupyter Notebook:
<img src="https://github.com/marty90/fastplot/raw/master/examples/jupyter.png"  height="300">

Note: If you want to both `show()` and `savefig()`, please do `savefig()` before, to prevent matplotlib from clearing the figure.

Note: You may need to add the IPython magic `%matplotlib inline` to be able to visualize inline plots.

#### Basic arguments

The most important arguments are:
* `data`: the actual data to plot
* `path`: the output path for the plot. The format is automatically inferred by matplotlib, looking at the extension of the path. Put it to `None` to have the current `plt` object returned and no file written.
* `mode`: which type of plot to create (lines, bars, etc.). More details later.
* `style`: which graphical style to use. Can be:
    * `sans-serif`: classical sans-serif, Arial-like font.
    * `serif`: use Times New Roman. Good for IEEE papers. You must have Times New Roman installed.
    * `latex`: tells `matplotlib` to use latex to render text. You must have `latex` installed. FastPlot has a utlity function called `fastplot.tex_escape()` to easily escape Tex strings.
    * Note: if you want to use the Linux Libertine font (e.g., used in ACM papers), you can use the `latex` style and pass the argument `rcParams={'text.latex.preamble'}: r'\usepackage{libertine}'}` to the `fastplot.plot()` function.
    * Note 2: if you want to use `Times New Roman` with Latex (very good for IEEE papers), you can use the `latex` style and pass the argument `rcParams={'text.latex.preamble': r'\usepackage{mathptmx}'}` to the `fastplot.plot()` function.
    * Note 3: if you want to use `Palladio` with Latex (some Latex classes use it), you can use the `latex` style and pass the argument `rcParams={'text.latex.preamble': r'\usepackage{mathpazo}'}` to the `fastplot.plot()` function.    


## Modes

The modes are the type of plots fastplot allows to use. Some are simple (just a line), other are more advanced (bars, etc.).
* `line`: plot a simple line. `data` must be a two-sized tuple of lists, for x and y. E.g., ([x1,x2,x3],[y1,y2,y3])
* `line_multi`: plot multiple lines. Data must have the form [ (line1, ([x1,x2], [y1,y2])), (line2, ([x1,x2], [y1,y2]) ) ]. The names `line1` and `line2` are put in the legend.
* `CDF`: plot a CDF given the samples. `data` must be a list of scalars. Note: if your CDF is too coarse grained, you can increase the resolution increasing `fastplot.NUM_BIN_CDF`.
* `CDF_multi`: plot many CDFs given the samples. `data` must be a list of two-sized tuples like (name, [samples]). `name` is used in the legend.
* `boxplot`: plot a boxplot given the samples. `data` must be a list of two-sized tuples like (name, [samples]). `name` is used in the xticks labels.
* `boxplot_multi`: plot a boxplot given the samples, clustered in groups. `data` a pandas dataframe, where each cell is a list. A groups are defined by each row, elements of each groups by columns.
* `timeseries`: plot a time series. `data` must be a pandas series, with a DateTime index.
* `timeseries_multi`: plot many time series. `data` must be a list of two-sized tuples like (name, timeseries). `name` is used in the legend.
* `timeseries_stacked`: plot many time series, stacked. `data` must be a pandas dataframe, with a DateTime index. Each column will be plotted stacked to the others. Column names are used in the legend.
* `bars`: plot a bar plot. `data` must be a list of (name, value). `name` is used for the legend.
* `bars_multi`: plot grouped bars. `data` must be a padas dataframe. Each row is results in a group of bars, while columns determine bars within each group.
* `bars_stacked`: plot stacked bars. `data` must be a padas dataframe. Rows go on x axis, while each column is a level in the bars.
* `callback`: call a user function instead of plotting `data`. You must provide a function pointer in the `callback` argument, that will be called passing `plt` as paramenter in order to perform a user defined plot. No matter what you put in `data`.

Note: you can use `callback` mode to draw data with `seaborn` and profit from all the features of `fastplot`. See the examples.

### Lorenz curve and Gini Index
`fastplot` provides utility functions to compute Lorenz curve and Gini Index.

To compute Gini index and Lorenz curve for a single set of samples call the `fastplot.lorenz_gini()` function, whose sole arguments is a set of samples. It returns `(lorenz_x, lorenz_y), gini_index`, that you can plot with the mode `line`.

To compute Gini index and Lorenz curve for multiple set of samples, call `fastplot.lorenz_gini_multi()`. It takes as input a list of two-sized tuples like (name, [samples]). It provides as output like: [ (name, ([x1,x2], [y1,y2])), (name, ([x1,x2], [y1,y2]) ) ]. The optional argument `name_format="{} (GI={:0.2f})"` is string format to transform names to include the value of the Gini index. The output of this function can be directly used as input to `fastplot` with mode `line_multi`

## Arguments
Arguments of the `plot` function are divided in many categories. Only `core` are mandatory.
   
**Core**
* `data`: the input data to plot
* `path`: the output path for the plot. The format is automatically inferred by matplotlib, looking at the extension of the path. Put it to `None` to have the current `plt` object returned and no file written.
* `mode`: which type of plot to create (lines, bars, etc.). More details later. Default `line`
* `plot_args`: an optional dictionary of arguments to pass the `matplotlib` plot() function. E.g., use `plot_args={"markersize":0.5}` to reduce the marker/point size.

**Look**
* `style`: which graphical style to use. Can be `serif`, `sans-serif` or `latex`. For latex, it enables matplotlib latex engine. Default `sans-serif`
* `figsize`: the size of the output figure. Default: `(4,2.25)`
* `cycler`: the style cycler to use. By default, it changes across main colors, and different linestyles. Change it if you want to change color, line, or point style. I provide some useful cycler in the code (see Cycler section). Default `CYCLER_LINES`
* `fontsize`: just the overall font size. Default `11`
* `dpi`: DPI for the output image. Default `300`
* `classic_autolimit`: Use classic autolimit feature (find 'nice' round numbers as view limits that enclosed the data limits), instead of v2 (sets the view limits to 5% wider than the data range). Default `True`
* `rcParams`: optional dictionary of rcParams to set before plotting


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
* `xlim`: Optional x limit, as a tuple (low, high). You can set `low` or `high` to `None` if you don't want to modify it.
* `ylim`: Optional y limit, as a tuple (low, high). You can set `low` or `high` to `None` if you don't want to modify it.
* `xlabel`: Label for x axis
* `ylabel`: Label for y axis
* `xticks`: Custom x ticks, in the form `([x1, x2, ...], [label1, label2, ...])`. You can pass `([x1, x2, ...], None)` if you just want to set the xticks, without specifying the labels.
* `yticks`:  Custom y ticks, in the form `([y1, y2, ...], [label1, label2, ...])` You can pass `([y1, y2, ...], None)` if you just want to set the yticks, without specifying the labels.
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
* `legend_fancybox`: whether to use round corner on legend frame. Default `False`
* `legend_alpha`: transparency of legend frame. Default `1.0`
* `legend_args`: an optional dictionary of arguments to pass the `matplotlib` legend() function. For example you might want to manually set legend location by passing `legend_args={'bbox_to_anchor' : (0.9, 0.1)}`.

**Specific**
This arguments are specific for some `modes`.
* `linewidth`: linewidth when lines are used. Default: `1`
* `boxplot_sym`: symbol for outliers in boxplots. Default `''`
* `boxplot_whis`: whisker spec for boxplot.  Default `[5,95]`
* `boxplot_numerousness`: plot the number of samples on the top-x axis.  Default `False`
* `boxplot_numerousness_fontsize`: size of sample groups labels.  Default `x-small`
* `boxplot_numerousness_rotate`: rotation for numerousness text.  Default `0`
* `boxplot_palette`: palette to be used with seaborn.  Default is seaborn default
* `boxplot_empty`: Wether to plot boxplot without filling it.  Default is `False`
* `timeseries_format`: format for printing dates in timeseries. Default `%Y/%m/%d`
* `bars_width`: width of bars when bars are plotted. Default `0.6`
* `callback`: function to call instead of plotting, when `mode=callback`
* `timeseries_stacked_right_legend_order`: for `timeseries_stacked`, plot legend in the same order as colors are shown in the plot. Default is `True`.
* `CDF_complementary`: for `CDF` and `CDF_multi`, plot complementary CDF instead of the plain one. Default is `False`.

 ## Cyclers

FastPlot provides simple cyclers to obtain nice lines, points, and linespoints in both color and B/W.

The list of available cyclers is:
* `fastplot.CYCLER_LINES`: Lines, with colors
* `fastplot.CYCLER_LINESPOINTS`: Linespoints, with colors
* `fastplot.CYCLER_POINTS`: Points, with colors
* `fastplot.CYCLER_LINES_BLACK`: Black lines
* `fastplot.CYCLER_LINESPOINTS_BLACK`: Black linespoints
* `fastplot.CYCLER_POINTS_BLACK`: Black points
 
 ## Examples

**line**
```
x = range(11)
y=[4,150,234,465,745,612,554,43,565,987,154]
fastplot.plot((x, y),  'examples/1_line.png', xlabel = 'X', ylabel = 'Y')
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/1_line.png"  height="200">


**line_multi**
```
x = range(11)
y1=[4,150,234,465,645,612,554,43,565,987,154]
y2=[434,15,24,556,75,345,54,443,56,97,854]
fastplot.plot([ ('First', (x, y1) ), ('Second', (x, y2) )], 'examples/2_line_multi.png',
              mode='line_multi', xlabel = 'X', ylabel = 'Y', xlim = (-0.5,10.5),
              cycler = fastplot.CYCLER_LINESPOINTS, legend=True, legend_loc='upper left',
              legend_ncol=2)
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/2_line_multi.png"  height="200">


**CDF**
```
fastplot.plot(np.random.normal(100, 30, 1000), 'examples/3_CDF.png', mode='CDF',
              xlabel = 'Data', style='latex')
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/3_CDF.png"  height="200">


**CDF complementary**
```
fastplot.plot(np.random.normal(100, 30, 1000), 'examples/3b_CCDF.png', mode='CDF', 
              CDF_complementary=True, xlabel = 'Data', style='latex')
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/3b_CCDF.png"  height="200">



**CDF_multi**
```
data = [ ('A', np.random.normal(100, 30, 1000)), ('B', np.random.normal(140, 50, 1000)) ]
plot_args={"markevery": [500]}
fastplot.plot(data , 'examples/4_CDF_multi.png', mode='CDF_multi', xlabel = 'Data', legend=True,
              cycler = fastplot.CYCLER_LINESPOINTS, plot_args=plot_args)
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/4_CDF_multi.png"  height="200">


**boxplot**
```
data=[ ('A', np.random.normal(100, 30, 450)),
       ('B', np.random.normal(140, 50, 50)),
       ('C', np.random.normal(140, 50, 200))]
fastplot.plot( data,  'examples/5_boxplot.png', mode='boxplot', ylabel = 'Value',
               boxplot_numerousness=True, boxplot_empty=True, boxplot_numerousness_rotate=90)
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/5_boxplot.png"  height="200">



**boxplot_multi**
```
data = pd.DataFrame(data=[ [np.random.normal(100, 30, 50),np.random.normal(110, 30, 50)],
                           [np.random.normal(90, 30, 50),np.random.normal(90, 30, 50)],
                           [np.random.normal(90, 30, 50),np.random.normal(80, 30, 50)],
                           [np.random.normal(80, 30, 50),np.random.normal(80, 30, 50)]],
                    columns=["Male","Female"], index = ["IT", "FR", "DE", "UK"] )
fastplot.plot( data,  'examples/5b_boxplot_multi.png', mode='boxplot_multi', ylabel = 'Value',
               boxplot_palette="muted", legend=True, legend_ncol=2, ylim=(0,None))
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/5b_boxplot_multi.png"  height="200">



**timeseries**
```
rng = pd.date_range('1/1/2011', periods=480, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
fastplot.plot(ts ,  'examples/6_timeseries.png', mode='timeseries', ylabel = 'Value',
              style='latex', xticks_rotate=30, xticks_fontsize='small',
              xlim=(pd.Timestamp('1/1/2011'), pd.Timestamp('1/7/2011')))

```
<img src="https://github.com/marty90/fastplot/raw/master/examples/6_timeseries.png"  height="200">


**timeseries_multi**
```
rng = pd.date_range('1/1/2011', periods=480, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng) + 5
ts2 = pd.Series(np.random.randn(len(rng)), index=rng) + 10
fastplot.plot( [('One', ts), ('Two', ts2)] , 'examples/7_timeseries_multi.png',
               mode='timeseries_multi', ylabel = 'Value', xticks_rotate=30,
               legend = True, legend_loc='upper center', legend_ncol=2, legend_frameon=False,
               ylim = (0,None), xticks_fontsize='small')
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/7_timeseries_multi.png"  height="200">


**timeseries_stacked**
```
rng = pd.date_range('1/1/2011', periods=480, freq='H')
df = pd.DataFrame(np.random.uniform(3,4,size=(len(rng),2)), index=rng, columns=('One','Two'))
df = df.divide(df.sum(axis=1), axis=0)*100
fastplot.plot( df , 'examples/8_timeseries_stacked.png', mode='timeseries_stacked',
               ylabel = 'Value [%]', xticks_rotate=30, ylim=(0,100), legend=True,
               xlim=(pd.Timestamp('1/1/2011'), pd.Timestamp('1/7/2011')))
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/8_timeseries_stacked.png"  height="200">


**bars**
```
data = [('First',3),('Second',2),('Third',7),('Four',6),('Five',5),('Six',4)]
fastplot.plot(data,  'examples/9_bars.png', mode = 'bars', ylabel = 'Value',
              xticks_rotate=30, style='serif', ylim = (0,10))
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/9_bars.png"  height="200">


**bars_multi**
```
data = pd.DataFrame( [[2,5,9], [3,5,7], [1,6,9], [3,6,8], [2,6,8]],
                     index = ['One', 'Two', 'Three', 'Four', 'Five'],
                     columns = ['A', 'B', 'C'] )
fastplot.plot(data,  'examples/10_bars_multi.png', mode = 'bars_multi', style='latex',
              ylabel = 'Value', legend = True, ylim = (0,12), legend_ncol=3,
              legend_args={'markerfirst' : False})
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/10_bars_multi.png"  height="200">

**bars_stacked**
```
data = pd.DataFrame( [[2,5,9], [3,5,7], [1,6,9], [3,6,3], [2,6,2]],
                     index = ['One', 'Two', 'Three', 'Four', 'Five'],
                     columns = ['A', 'B', 'C'] )
fastplot.plot(data,  'examples/12_bars_stacked.png', mode = 'bars_stacked', style='serif',
              ylabel = 'Value', legend = True, xtick_length=0, legend_ncol=3, ylim = (0,25))
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/12_bars_stacked.png"  height="200">



**callback**
```
x = range(11)
y=[120,150,234,465,745,612,554,234,565,888,154]
def my_callback(plt):
    plt.bar(x,y)
fastplot.plot(None,  'examples/11_callback.png', mode = 'callback', callback = my_callback,
              style='latex', xlim=(-0.5, 11.5), ylim=(0, 1000))
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/11_callback.png"  height="200">


**Lorenz Curves**
```
data = [ ('A', np.random.chisquare(2, 1000)), ('B', np.random.chisquare(8, 1000)) ]
data = fastplot.lorenz_gini_multi(data)
fastplot.plot(data, 'examples/13_lorenz.png', mode='line_multi', legend=True, grid=True,
              xlabel = 'Samples [%]', ylabel = 'Share [%]', xlim=(0,1), ylim=(0,1))
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/13_lorenz.png"  height="200">


**seaborn**
```
data = pd.DataFrame([(4,3),(5,4),(4,5),(8,6),(10,8),(3,1),(13,10),(9,7),(11,11)], columns=["x","y"])
def my_callback(plt):
     sns.regplot(x="x", y="y", data=data, ax=plt.gca())
fastplot.plot(None,  'examples/14_seaborn.png', mode = 'callback', callback = my_callback,
              style='latex', grid=True)
```
<img src="https://github.com/marty90/fastplot/raw/master/examples/14_seaborn.png"  height="200">







