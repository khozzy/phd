import numpy as np
import pymc3 as pm


def bayes_estimate(data: np.ndarray, draws=3000):
    # If all values are the same there is no point in calculating statistical model
    if np.all(data == data[0]):
        return {
            'mu': np.array([data[0]]),
            'std': np.array([0])
        }

    mean = data.mean()
    variance = data.std() * 2

    # prior
    with pm.Model() as model:
        mu = pm.Normal('mu', mu=mean, sd=variance)
        std = pm.Uniform('std', 1 / 100, 1000)
        nu = pm.Exponential('nu', 1.0 / 29)  # degrees of freedom

    # posterior
    with model:
        obs = pm.StudentT('obs', mu=mu, lam=1.0 / std ** 2, nu=nu + 1, observed=data)

    # sample
    with model:
        trace = pm.sample(draws, target_accept=0.95, return_inferencedata=False, progressbar=False)

    return trace
