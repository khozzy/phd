import numpy as np
import pandas as pd
from lcs.metrics import population_metrics
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from src.visualization import PLOT_DPI, diminishing_reward_colors


def common_metrics(agent, env):
    metrics = {}

    pop = agent.get_population()
    agent_name = agent.__class__.__name__

    if hasattr(agent, 'rho'):
        metrics['rho'] = agent.rho
        agent_name += "_v" + agent.cfg.rho_update_version
    else:
        metrics['rho'] = 0

    metrics['agent'] = agent_name
    metrics['reliable'] = len([cl for cl in pop if cl.is_reliable()])

    metrics.update(population_metrics(pop, env))

    return metrics
