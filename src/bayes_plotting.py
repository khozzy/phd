import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

from src.visualization import discretized_algorithms_colors, PLOT_DPI


def plot_bayes_comparison(df, env_name, agents, plot_filename=None):
    df = normalize(df)

    COLORS = discretized_algorithms_colors()

    fig = plt.figure(figsize=(20, 14))

    attributes = df.columns.to_list()
    theta = _radar_factory(len(attributes), frame='circle')

    ax = fig.add_subplot(1, 1, 1, projection='radar')
    ax.get_yaxis().set_ticklabels([])
    ax.set_varlabels(attributes)
    ax.set_title(env_name, pad=50)

    for i, alg in enumerate(agents):
        v = df.loc[alg].to_list()
        ax.plot(theta, v, color=COLORS[alg])
        ax.fill(theta, v, facecolor=COLORS[alg], alpha=0.25)

    # realign theta labels
    for theta, label in zip(ax.get_xticks(), ax.get_xticklabels()):
        theta = theta * ax.get_theta_direction() + ax.get_theta_offset()
        theta = np.pi / 2 - theta
        y, x = np.cos(theta), np.sin(theta)
        if x >= 0.1:
            label.set_horizontalalignment('left')
        if x <= -0.1:
            label.set_horizontalalignment('right')
        if y >= 0.5:
            label.set_verticalalignment('bottom')
        if y <= -0.5:
            label.set_verticalalignment('top')

        fig.suptitle('Bayesian Estimation of metrics', fontsize=28)
        fig.tight_layout()
        fig.subplots_adjust(
            top=0.85,
            # left=0.0, right=0.75,
            bottom=0.1,
            wspace=-0.25,
            hspace=0.35
        )

        # build legend
        fig.legend([alg.upper() for alg in agents], loc='lower center', ncol=len(agents), labelspacing=0.5, prop={'size': 23})

        if plot_filename:
            fig.savefig(plot_filename, dpi=PLOT_DPI, bbox_inches='tight')

        return fig


def normalize(df: pd.DataFrame, norm_type: str = 'max'):
    if norm_type == 'min-max':
        return (df - df.min()) / (df.max() - df.min())
    elif norm_type == 'mean':
        return (df - df.mean()) / df.std()
    elif norm_type == 'max':
        assert all(v >= 0 for v in df.min())
        return df / df.max()
    else:
        raise ValueError(f'Unknown normalization type: {norm_type}')


def _radar_factory(num_vars, frame='circle'):
    theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

    class RadarAxes(PolarAxes):

        name = 'radar'
        # use 1 line segment to connect specified points
        RESOLUTION = 1

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.append(x, x[0])
                y = np.append(y, y[0])
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels, size='small')

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars, radius=.5, edgecolor="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_vars))
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5) + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)

    return theta
