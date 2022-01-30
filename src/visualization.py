import matplotlib.pyplot as plt
from pylab import cm

# GLOBAL SETTINGS
PLOT_DPI = 200


# COLOR SCHEMES
def biased_exploration_colors():
    cmap = plt.get_cmap('jet_r')
    norm = plt.Normalize(vmin=0, vmax=4)
    return {
        "eg": cmap(norm(0)),
        "ad": cmap(norm(1)),
        "ka": cmap(norm(2)),
        "oiq": cmap(norm(3))
    }


def diminishing_reward_colors():
    palette = cm.get_cmap('Paired', 5)
    return {
        'ACS2': palette(0),
        'AACS2_v1': palette(1),
        'AACS2_v2': palette(2),
        'Q-Learning': palette(3),
        'R-Learning': palette(4)
    }


def discretized_algorithms_colors():
    palette = cm.get_cmap('tab10', 5)
    return {
        'acs': palette(0),
        'acs2': palette(1),
        'acs2_ga': palette(2),
        'yacs': palette(3),
        'dynaq': palette(4),
    }