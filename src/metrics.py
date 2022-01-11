import pandas as pd

from lcs import Perception


def parse_experiments_results(explore_metrics, exploit_metrics, frequency):
    explore_df = pd.DataFrame(explore_metrics)
    exploit_df = pd.DataFrame(exploit_metrics)

    explore_df['phase'] = 'explore'
    exploit_df['phase'] = 'exploit'

    df = pd.concat([explore_df, exploit_df], ignore_index=True)
    df['trial'] = df.index * frequency
    df.set_index('trial', inplace=True)
    return df


def corridor_transition_knowledge(population, environment):
    transitions = environment.env.get_transitions()

    reliable = [c for c in population if c.is_reliable()]
    nr_correct = 0

    for start, action, end in transitions:
        p0 = Perception((str(start),))
        p1 = Perception((str(end),))

        if any([True for cl in reliable if
                cl.predicts_successfully(p0, action, p1)]):
            nr_correct += 1

    return nr_correct / len(transitions) * 100.0


def grid_transition_knowledge(population, environment):
    transitions = environment.env.get_transitions()

    reliable = [c for c in population if c.is_reliable()]
    nr_correct = 0

    for start, action, end in transitions:
        p0 = Perception([str(el) for el in start])
        p1 = Perception([str(el) for el in end])

        if any([True for cl in reliable if cl.predicts_successfully(p0, action, p1)]):
            nr_correct += 1

    return nr_correct / len(transitions) * 100.0

