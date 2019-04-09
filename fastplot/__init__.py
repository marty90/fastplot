#!/usr/bin/python3

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from cycler import cycler
import numpy as np
import re
from statsmodels.distributions.empirical_distribution import ECDF

FIGSIZE=(4,2.25)
NUM_BIN_CDF=1000
CYCLER_LINES=(cycler('color', ['r', 'b', 'g', 'y', 'c']) +
              cycler('linestyle', ['-', '--', '-.', ':', (0, (3, 1, 1, 1)) ]))
CYCLER_LINESPOINTS=(cycler('color', ['r', 'b', 'g', 'y', 'c']) +
                    cycler('linestyle', ['-', '--', '-.', ':', (0, (3, 1, 1, 1)) ]) +
                    cycler('marker', ['o', 's', 'v', 'd', '^' ]))
CYCLER_POINTS=(cycler('color', ['r', 'b', 'g', 'y', 'c']) +
               cycler('linestyle', ['', '', '', '', '']) +
               cycler('marker', ['o', 's', 'v', 'd', '^' ]))

CYCLER_LINES_BLACK=(cycler('color', ['black', 'black', 'black', 'black', 'black']) +
                    cycler('linestyle', ['-', '--', '-.', ':', (0, (3, 1, 1, 1)) ]))
CYCLER_LINESPOINTS_BLACK=(cycler('color', ['black', 'black', 'black', 'black', 'black']) +
                    cycler('linestyle', ['-', '--', '-.', ':', (0, (3, 1, 1, 1)) ]) +
                    cycler('marker', ['o', 's', 'v', 'd', '^' ]))
CYCLER_POINTS_BLACK=(cycler('color', ['black', 'black', 'black', 'black', 'black']) +
               cycler('linestyle', ['', '', '', '', '']) +
               cycler('marker', ['o', 's', 'v', 'd', '^' ]))


def plot(data, path, mode = 'line',
         style = 'sans-serif', figsize = FIGSIZE, cycler = CYCLER_LINES, fontsize = 11, dpi=300, classic_autolimit=True, rcParams={}, plot_args = {},
         grid = False, grid_which='major', grid_axis = 'both', grid_linestyle = 'dotted', grid_color = 'black',
         yscale = 'linear' , xscale = 'linear',
         xlim = None, ylim = None, xlabel = None, ylabel = None, xticks = None, yticks = None, xticks_rotate = None, yticks_rotate = None, xticks_fontsize='medium', yticks_fontsize='medium', 
         xtick_direction = 'in', xtick_width = 1, xtick_length = 3, ytick_direction = 'in', ytick_width = 1, ytick_length = 3, 
         legend = False, legend_loc = 'best', legend_ncol = 1, legend_fontsize = 'medium', legend_border = False, legend_frameon = True, legend_fancybox = False, legend_alpha=1.0, legend_args = {},
         linewidth = 1, boxplot_sym='', boxplot_whis=[5,95], timeseries_format='%Y/%m/%d', bars_width=0.6,
         callback = None, timeseries_stacked_right_legend_order=True, CDF_complementary=False ):

    # 1. Create and configure plot visual style
    mpl.rcParams.update(mpl.rcParamsDefault)
    plt.clf()
    plt.figure(figsize=figsize)

    plt.rc('axes', prop_cycle=cycler)
    plt.rc('font', **{'size': fontsize})

    # Old default axis lim
    if classic_autolimit:
        plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
        plt.rcParams['axes.xmargin'] = 0
        plt.rcParams['axes.ymargin'] = 0

    if style == 'latex':
        plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
        plt.rc('text', usetex=True)
    elif style == 'serif':
        plt.rcParams["font.family"] = "Times New Roman"
    else:
        plt.rcParams["font.family"] = "sans-serif"

    # Set custom rcparams
    plt.rcParams.update(rcParams)


    # 2. Set axis characteristics
    plt.yscale(yscale)
    plt.xscale(xscale)
    if grid:
        plt.grid(which=grid_which, axis=grid_axis, linestyle=grid_linestyle, color=grid_color)


    # 3. Plot
    if mode == 'line_multi':
        for name, points in data:
            plt.plot(points[0], points[1], label = name, markeredgewidth=0,
                     linewidth = linewidth, **plot_args)    

    elif mode == 'line':
        plt.plot(data[0], data[1], markeredgewidth=0, linewidth = linewidth, **plot_args) 

    elif mode == 'CDF':
        s = data
        e = ECDF(s)
        if xscale == 'log':
            x = np.logspace(np.log10(min(s)), np.log10(max(s)), NUM_BIN_CDF )
            if CDF_complementary:
                y = 1-e(x)
            else:
                y = e(x)
        else:
            x = np.linspace(min(s), max(s), NUM_BIN_CDF )  
            if CDF_complementary:
                y = 1-e(x)
                x = np.concatenate( (np.array([min(s)]), x) )
                y = np.concatenate( (np.array([1]), y) )
            else:
                y = e(x)
                x = np.concatenate( (np.array([min(s)]), x) )
                y = np.concatenate( (np.array([0]), y) )

        plt.plot(x,y, linewidth = linewidth, **plot_args)
        if ylabel is None:
            ylabel = 'CCDF' if CDF_complementary else "CDF"
        if ylim is None:
            ylim = (0,1)

    elif mode == 'CDF_multi':
        for s_name, s in data :
            e = ECDF(s)
            if xscale == 'log':
                x = np.logspace(np.log10(min(s)), np.log10(max(s)), NUM_BIN_CDF )
                if CDF_complementary:
                    y = 1-e(x)
                else:
                    y = e(x)
            else:
                x = np.linspace(min(s), max(s), NUM_BIN_CDF )  

                if CDF_complementary:
                    y = 1-e(x)
                    x = np.concatenate( (np.array([min(s)]), x) )
                    y = np.concatenate( (np.array([1]), y) )
                else:
                    y = e(x)
                    x = np.concatenate( (np.array([min(s)]), x) )
                    y = np.concatenate( (np.array([0]), y) )

            plt.plot(x,y, label=s_name, linewidth = linewidth, **plot_args)

        if ylabel is None:
            ylabel = 'CCDF' if CDF_complementary else "CDF"
        if ylim is None:
            ylim = (0,1)

    elif mode == 'boxplot':
        labels = [e[0] for e in data]
        samples = [e[1] for e in data]
        plt.boxplot(samples, labels=labels, sym=boxplot_sym, whis=boxplot_whis, **plot_args)

    elif mode == 'timeseries':
        plt.plot(data, markeredgewidth=0, linewidth = linewidth, **plot_args) 
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(timeseries_format))

    elif mode == 'timeseries_multi':
        for name, series in data:
            plt.plot(series, markeredgewidth=0, label = name, linewidth = linewidth, **plot_args) 
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(timeseries_format))

    elif mode == 'timeseries_stacked':
        plt.stackplot(data.index,  np.transpose(data.as_matrix()), lw=0, labels = data.columns, **plot_args)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(timeseries_format))

    elif mode == 'bars':
        yy = [d[1] for d in data]
        xticks_labels_from_data = [d[0] for d in data]
        xx = range(len(yy))
        plt.bar(xx, yy, linewidth = linewidth, align = 'center', width = bars_width, **plot_args)
        plt.xticks(xx, xticks_labels_from_data)
        plt.xlim((-0.5, len(xx) -0.5 )) # Default pretty xlim

    elif mode == 'bars_multi':
        xticks_labels_from_data = list(data.index)
        num_rows = len(data.index)
        num_columns = len(data.columns)
        bars_width_real=bars_width/num_columns
        prop_iter = iter(plt.rcParams['axes.prop_cycle'])
        for i, column in enumerate( data ):
            delta = -bars_width/2 + i*bars_width_real + bars_width_real/2
            plt.bar( [e + delta for e in range(num_rows)], list(data[column]), linewidth = linewidth,
                     align = 'center', width = bars_width_real, label = column,
                     color=next(prop_iter)['color'], **plot_args)
        plt.xticks(range(num_rows), xticks_labels_from_data)
        plt.xlim((-0.5, num_rows -0.5 )) # Default pretty xlim

    elif mode == 'bars_stacked':
        xticks_labels_from_data = list(data.index)
        num_rows = len(data.index)
        num_columns = len(data.columns)
        prop_iter = iter(plt.rcParams['axes.prop_cycle'])
        bottom = np.zeros(num_rows)
        for i, column in enumerate( data ):
            plt.bar(range(num_rows), list(data[column]), bottom=bottom, linewidth = linewidth,
                     align = 'center', width = bars_width, label = column,
                     color=next(prop_iter)['color'], **plot_args)
            bottom = np.add(bottom, list(data[column]))
            
        plt.xticks(range(num_rows), xticks_labels_from_data)
        plt.xlim((-0.5, num_rows -0.5 )) # Default pretty xlim

    elif mode == 'callback':
        callback(plt)


    # 4. Set axis
    plt.xticks(fontsize=xticks_fontsize)
    plt.yticks(fontsize=yticks_fontsize)

    if ylabel is not None:
        plt.ylabel(ylabel)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    if xticks is not None:
        plt.xticks(xticks[0], xticks[1])
    if yticks is not None:
        plt.yticks(yticks[0], yticks[1])
    if xticks_rotate is not None:
        if xticks_rotate > 0:
            plt.xticks(rotation=xticks_rotate, ha="right")
        else:
            plt.xticks(rotation=xticks_rotate, ha="left")
    if yticks_rotate is not None:
        if yticks_rotate > 0:
            plt.yticks(rotation=yticks_rotate, ha="right")
        else:
            plt.yticks(rotation=yticks_rotate, ha="left")

    # Tick marker params
    plt.tick_params(axis = 'x', direction = xtick_direction, width = xtick_width, length = xtick_length )
    plt.tick_params(axis = 'y', direction = ytick_direction, width = ytick_width, length = ytick_length )

    # 5. Legend
    if legend:
        legend = plt.legend(loc=legend_loc, ncol = legend_ncol, fontsize = legend_fontsize,
                            numpoints=1, frameon = legend_frameon, fancybox=legend_fancybox,
                            **legend_args)
        legend.get_frame().set_alpha(legend_alpha)
        if legend_border == False:
            legend.get_frame().set_linewidth(0.0)

        # Handle timeseries_stacked_right_legend_order
        if mode == 'timeseries_stacked' and timeseries_stacked_right_legend_order: 
            handles, labels = plt.gca().get_legend_handles_labels()
            legend = plt.gca().legend(handles[::-1], labels[::-1], loc=legend_loc, ncol = legend_ncol,
                                fontsize = legend_fontsize, numpoints=1, frameon = legend_frameon,
                                fancybox=legend_fancybox, **legend_args) 
            legend.get_frame().set_alpha(legend_alpha)
            if legend_border == False:
                legend.get_frame().set_linewidth(0.0)


    # 6. Save Fig
    plt.tight_layout()

    # Handle Interactive Plot
    if path is not None:
        plt.savefig(path, dpi=dpi)
        plt.close()
        return
    else:
        return plt

# Thanks to: https://stackoverflow.com/a/25875504/6018688
def tex_escape(text):
    """
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
    }
    regex = re.compile('|'.join(re.escape(str(key)) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], text)

def gini(arr):
    count = arr.size
    coefficient = 2 / count
    indexes = np.arange(1, count + 1)
    weighted_sum = (indexes * arr).sum()
    total = arr.sum()
    constant = (count + 1) / count
    return coefficient * weighted_sum / total - constant

def lorenz_gini(arr):
    arr = np.sort(arr)
    scaled_prefix_sum = arr.cumsum() / arr.sum()
    np.insert(scaled_prefix_sum, 0, 0)
    lorenz_y = scaled_prefix_sum 
    lorenz_x = np.linspace(0.0, 1.0, lorenz_y.size) 
    gini_index = gini(arr)
    return ((lorenz_x, lorenz_y), gini_index)

def lorenz_gini_multi(data, name_format="{} (GI={:0.2f})"):
    data_new = []
    for name, samples in data:
        (lorenz_x, lorenz_y), gini_index = lorenz_gini(samples)
        name_new = name_format.format(name, gini_index)
        data_new.append( (name_new, (lorenz_x,lorenz_y) )   )
    return data_new
  
