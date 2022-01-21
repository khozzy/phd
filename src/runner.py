import logging

import lcs.agents.aacs2 as aacs2
import lcs.agents.acs2 as acs2
import pandas as pd


def run_experiments_alternating(env_provider, trials, params):
    """
    Function running experiments in explore-exploit fashion using
    3 algorithms - ACS2, AACS2-v1, AACS2-v2
    """

    def parse_metrics(metrics):
        # idx = [d['agent'] for d in metrics]

        data = [[
            d['agent'],
            d['trial'],
            d['steps_in_trial'],
            d['rho'],
            d['population'],
            d['reliable']] for d in metrics]

        df = pd.DataFrame(
            data,
            columns=['agent', 'trial', 'steps_in_trial', 'rho', 'population', 'reliable'],
            # index=idx
        )

        # It is used in alternating explore-exploit mode
        df['phase'] = df.trial.map(
            lambda t: "explore" if t % 2 == 0 else "exploit")

        return df

    env = env_provider()

    logging.info('Starting ACS2 experiments')
    acs2_cfg = acs2.Configuration(
        classifier_length=params['perception_bits'],
        number_of_possible_actions=params['possible_actions'],
        do_ga=params['do_ga'],
        beta=params['beta'],
        epsilon=params['epsilon'],
        gamma=params['gamma'],
        user_metrics_collector_fcn=params['user_metrics_collector_fcn'],
        biased_exploration_prob=params['biased_exploration_prob'],
        metrics_trial_frequency=params['metrics_trial_freq'])

    acs2_agent = acs2.ACS2(acs2_cfg)
    metrics_acs2 = acs2_agent.explore_exploit(env, trials)

    logging.info('Starting AACS2-v1 experiments')
    aacs2v1_cfg = aacs2.Configuration(
        classifier_length=params['perception_bits'],
        number_of_possible_actions=params['possible_actions'],
        do_ga=params['do_ga'],
        beta=params['beta'],
        epsilon=params['epsilon'],
        gamma=params['gamma'],
        zeta=params['zeta'],
        rho_update_version='1',
        user_metrics_collector_fcn=params['user_metrics_collector_fcn'],
        biased_exploration_prob=params['biased_exploration_prob'],
        metrics_trial_frequency=params['metrics_trial_freq'])

    aacs2v1_agent = aacs2.AACS2(aacs2v1_cfg)
    metrics_aacs2v1 = aacs2v1_agent.explore_exploit(env, trials)

    logging.info('Starting AACS2-v2 experiments')
    aacs2v2_cfg = aacs2.Configuration(
        classifier_length=params['perception_bits'],
        number_of_possible_actions=params['possible_actions'],
        do_ga=params['do_ga'],
        beta=params['beta'],
        epsilon=params['epsilon'],
        gamma=params['gamma'],
        zeta=params['zeta'],
        rho_update_version='2',
        user_metrics_collector_fcn=params['user_metrics_collector_fcn'],
        biased_exploration_prob=params['biased_exploration_prob'],
        metrics_trial_frequency=params['metrics_trial_freq'])

    aacs2v2_agent = aacs2.AACS2(aacs2v2_cfg)
    metrics_aacs2v2 = aacs2v2_agent.explore_exploit(env, trials)

    # Join metrics together
    m = []
    m.extend(metrics_acs2)
    m.extend(metrics_aacs2v1)
    m.extend(metrics_aacs2v2)

    return acs2_agent.population, \
           aacs2v1_agent.population, \
           aacs2v2_agent.population, \
           parse_metrics(m)
