import lcs.agents.acs as acs
import lcs.agents.acs2 as acs2
import lcs.agents.yacs as yacs
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd

from src.basic_rl import dynaq
from src.visualization import PLOT_DPI, discretized_algorithms_colors


def single_acs_experiment(
        env_provider,
        trials,
        classifier_length,
        possible_actions,
        learning_rate,
        metrics_trial_freq,
        metrics_fcn):
    env = env_provider()

    cfg = acs.Configuration(
        classifier_length=classifier_length,
        number_of_possible_actions=possible_actions,
        beta=learning_rate,
        metrics_trial_frequency=metrics_trial_freq,
        user_metrics_collector_fcn=metrics_fcn)

    agent = acs.ACS(cfg)
    metrics = agent.explore(env, trials)

    return agent, metrics


def single_acs2_experiment(
        env_provider,
        trials,
        classifier_length,
        possible_actions,
        learning_rate,
        do_ga,
        initial_q,
        metrics_trial_freq,
        metrics_fcn):
    env = env_provider()

    cfg = acs2.Configuration(
        classifier_length=classifier_length,
        number_of_possible_actions=possible_actions,
        beta=learning_rate,
        do_ga=do_ga,
        initial_q=initial_q,
        metrics_trial_frequency=metrics_trial_freq,
        user_metrics_collector_fcn=metrics_fcn)

    agent = acs2.ACS2(cfg)
    metrics = agent.explore(env, trials)

    return agent, metrics


def single_yacs_experiment(
        env_provider,
        trials,
        classifier_length,
        possible_actions,
        learning_rate,
        trace_length,
        estimate_expected_improvements,
        feature_possible_values,
        metrics_trial_freq,
        metrics_fcn):
    env = env_provider()

    cfg = yacs.Configuration(
        classifier_length=classifier_length,
        number_of_possible_actions=possible_actions,
        learning_rate=learning_rate,
        trace_length=trace_length,
        estimate_expected_improvements=estimate_expected_improvements,
        feature_possible_values=feature_possible_values,
        metrics_trial_frequency=metrics_trial_freq,
        user_metrics_collector_fcn=metrics_fcn)

    agent = yacs.YACS(cfg)
    metrics = agent.explore(env, trials)

    return agent, metrics


def single_dynaq_experiment(
        env_provider,
        trials,
        q_init,
        model_init,
        epsilon,
        learning_rate,
        knowledge_fcn,
        metrics_trial_freq):
    env = env_provider()
    Q, MODEL, metrics = dynaq(
        env,
        episodes=trials,
        Q=q_init,
        MODEL=model_init,  # maps state-actions to (reward, next_state) tuples
        epsilon=epsilon,
        learning_rate=learning_rate,
        gamma=0.9,
        planning_steps=5,
        knowledge_fcn=knowledge_fcn,
        metrics_trial_freq=metrics_trial_freq)

    return Q, MODEL, metrics


def parse_lcs_metrics(agent_name, metrics):
    data = [[agent_name, d['perf_time'], d['trial'], d['knowledge'], d['pop'],
             d['generalization'], d['steps_in_trial']] for d in metrics]

    df = pd.DataFrame(
        data,
        columns=['agent', 'time', 'trial', 'knowledge', 'population',
                 'generalization', 'trial_steps'])

    return df


def parse_dyna_metrics(agent, metrics):
    # (steps, model_size, time, knowledge) = metrics
    df = pd.DataFrame(metrics.T, columns=['trial_steps', 'population', 'time', 'knowledge'])

    # add derived columns
    df['trial'] = df.index
    df['agent'] = agent
    df['generalization'] = 0

    df = df.drop(df[df.time == 0.0].index)

    return df


def plot_comparison(df, plot_filename=None):
    COLORS = discretized_algorithms_colors()
    ALGS_NO = len(COLORS)

    fig, axs = plt.subplots(2, 2, figsize=(22, 16))

    # Line styles
    # marker = metrics.index.get_level_values(1).max() / 10
    marker = 10
    mark_every = (np.linspace(0, marker, ALGS_NO) + marker).astype(int)
    line_props = {
        'linewidth': 3,
        'markersize': 9
    }

    acs_line_props = {'label': 'ACS', 'color': COLORS['acs'], 'marker': 'x', 'markevery': mark_every[0], **line_props}
    acs2_line_props = {'label': 'ACS2', 'color': COLORS['acs2'], 'marker': 'v', 'markevery': mark_every[1],
                       **line_props}
    acs2_oiq_line_props = {'label': 'ACS2_OIQ', 'color': COLORS['acs2_oiq'], 'marker': 'v', 'markevery': mark_every[2],
                           **line_props}
    acs2_ga_line_props = {'label': 'ACS2_GA', 'color': COLORS['acs2_ga'], 'marker': 's', 'markevery': mark_every[3],
                          **line_props}
    acs2_ga_oiq_line_props = {'label': 'ACS2_GA_OIQ', 'color': COLORS['acs2_ga_oiq'], 'marker': 's',
                              'markevery': mark_every[4], **line_props}
    yacs_line_props = {'label': 'YACS', 'color': COLORS['yacs'], 'marker': 'o', 'markevery': mark_every[5],
                       **line_props}
    dynaq_line_props = {'label': 'DynaQ', 'color': COLORS['dynaq'], 'marker': 'D', 'markevery': mark_every[6],
                        **line_props}

    df['knowledge_100'] = df['knowledge'] * 100
    df['generalization_100'] = df['generalization'] * 100

    # Population
    df.loc['acs']['population'].plot(ax=axs[0, 0], **acs_line_props)
    df.loc['acs2']['population'].plot(ax=axs[0, 0], **acs2_line_props)
    df.loc['acs2_oiq']['population'].plot(ax=axs[0, 0], **acs2_oiq_line_props)
    df.loc['acs2_ga']['population'].plot(ax=axs[0, 0], **acs2_ga_line_props)
    df.loc['acs2_ga_oiq']['population'].plot(ax=axs[0, 0], **acs2_ga_oiq_line_props)
    df.loc['yacs']['population'].plot(ax=axs[0, 0], **yacs_line_props)
    df.loc['dynaq']['population'].plot(ax=axs[0, 0], **dynaq_line_props)
    axs[0, 0].set_title('Population size')
    axs[0, 0].set_ylabel('Number of rules/classifiers')
    #     axs[0, 0].legend(loc='best', frameon=False)

    # Knowledge
    axs[0, 1].set_title('Knowledge')
    df.loc['acs']['knowledge_100'].plot(ax=axs[0, 1], **acs_line_props)
    df.loc['acs2']['knowledge_100'].plot(ax=axs[0, 1], **acs2_line_props)
    df.loc['acs2_oiq']['knowledge_100'].plot(ax=axs[0, 1], **acs2_oiq_line_props)
    df.loc['acs2_ga']['knowledge_100'].plot(ax=axs[0, 1], **acs2_ga_line_props)
    df.loc['acs2_ga_oiq']['knowledge_100'].plot(ax=axs[0, 1], **acs2_ga_oiq_line_props)
    df.loc['yacs']['knowledge_100'].plot(ax=axs[0, 1], **yacs_line_props)
    df.loc['dynaq']['knowledge_100'].plot(ax=axs[0, 1], **dynaq_line_props)
    #     axs[0, 1].legend(loc='lower right', frameon=False)
    axs[0, 1].yaxis.set_major_formatter(mtick.PercentFormatter())

    # Generalization
    axs[1, 0].set_title('Generalization')
    df.loc['acs']['generalization_100'].plot(ax=axs[1, 0], **acs_line_props)
    df.loc['acs2']['generalization_100'].plot(ax=axs[1, 0], **acs2_line_props)
    df.loc['acs2_oiq']['generalization_100'].plot(ax=axs[1, 0], **acs2_oiq_line_props)
    df.loc['acs2_ga']['generalization_100'].plot(ax=axs[1, 0], **acs2_ga_line_props)
    df.loc['acs2_ga_oiq']['generalization_100'].plot(ax=axs[1, 0], **acs2_ga_oiq_line_props)
    df.loc['yacs']['generalization_100'].plot(ax=axs[1, 0], **yacs_line_props)
    df.loc['dynaq']['generalization_100'].plot(ax=axs[1, 0], **dynaq_line_props)
    #     axs[1, 0].legend(loc='best', frameon=False)
    axs[1, 0].yaxis.set_major_formatter(mtick.PercentFormatter())

    # Trial time
    times = df.groupby('agent')['time'].mean().to_dict()

    labels = ['ACS', 'ACS2', 'ACS2_OIQ', 'ACS2_GA', 'ACS2_GA_OIQ', 'YACS', 'DynaQ']
    values = [times['acs'], times['acs2'], times['acs2_oiq'], times['acs2_ga'], times['acs2_ga_oiq'], times['yacs'],
              times['dynaq']]
    colors = [COLORS['acs'], COLORS['acs2'], COLORS['acs2_oiq'], COLORS['acs2_ga'], COLORS['acs2_ga_oiq'],
              COLORS['yacs'], COLORS['dynaq']]

    axs[1, 1].bar(labels, values, color=colors)
    axs[1, 1].set_xticklabels(labels, rotation=60)
    axs[1, 1].set_title('Average trial time')
    axs[1, 1].set_ylabel('Seconds [s]')

    # create some space below the plots by increasing the bottom-value
    fig.subplots_adjust(top=0.9, left=0.1, right=0.9, bottom=0.16)

    # Global legend
    handles, labels = axs[1, 0].get_legend_handles_labels()
    fig.legend(handles, labels, ncol=len(values), loc='lower center', prop={'size': 23})

    if plot_filename:
        fig.savefig(plot_filename, dpi=PLOT_DPI, bbox_inches='tight')
