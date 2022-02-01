from lcs.metrics import population_metrics


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
