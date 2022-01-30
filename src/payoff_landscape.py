import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from collections import namedtuple
from typing import Dict

from src.visualization import diminishing_reward_colors, PLOT_DPI

StateAction = namedtuple('StateAction', 'id state action')


def get_all_state_action(state_to_actions):
    state_action = []

    idx = 1
    for state, actions in state_to_actions.items():
        if len(actions) > 0:
            for action in actions:
                state_action.append(StateAction(idx, state, action))
                idx += 1

    return state_action


def plot_payoff_landscape(payoffs: Dict, rho: float, rho_text_location, plot_filename=None) -> None:
    colors = diminishing_reward_colors()

    fig, ax = plt.subplots(figsize=(15, 10))

    x = range(1, len(payoffs)+1)

    for alg in ['ACS2', 'AACS2_v1', 'AACS2_v2', 'Q-Learning', 'R-Learning']:
        y = sorted([v[alg] for k, v in payoffs.items()])

        plt.scatter(x, y, color=colors[alg])
        plt.plot(x, y, label=alg,  linewidth=2, color=colors[alg])

    # x-axis
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%1.0f'))
    ax.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
    ax.xaxis.set_tick_params(which='minor', size=5, width=1, direction='in')
    ax.set_xlabel("State-action pairs")

    # y-axis
    ax.yaxis.set_major_locator(MultipleLocator(250))
    ax.yaxis.set_minor_locator(MultipleLocator(50))
    ax.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
    ax.yaxis.set_tick_params(which='minor', size=5, width=1, direction='in')
    ax.set_ylabel("Payoff value")

    # others
    ax.set_title(f"Payoff Landscape")
    ax.text(**rho_text_location, s=fr'$\rho={rho:.2f}$', color=colors['R-Learning'])
    ax.legend(loc='lower right', bbox_to_anchor=(1, 0), frameon=False)

    if plot_filename:
        plt.savefig(plot_filename, transparent=False, bbox_inches='tight', dpi=PLOT_DPI)

    return fig