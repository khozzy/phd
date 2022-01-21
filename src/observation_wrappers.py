import gym
import numpy as np


class CorridorObservationWrapper(gym.ObservationWrapper):
    def observation(self, obs):
        return obs,


class FSWObservationWrapper(gym.ObservationWrapper):
    def observation(self, observation):
        return observation,


class BinnedObservationWrapper(gym.ObservationWrapper):
    """
    Divide observation using environment's observation space into `num_bins` equal bins.
    """

    def __init__(self, env, num_bins):
        super().__init__(env)
        self._range, self._low = (env.observation_space.high - env.observation_space.low, env.observation_space.low)
        self.num_bins = num_bins

    def observation(self, obs):
        r = (obs + np.abs(self._low)) / self._range
        b = (r * self.num_bins).astype(int)
        return b.astype(str).tolist()
