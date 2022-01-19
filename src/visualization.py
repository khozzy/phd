import matplotlib.pyplot as plt

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
