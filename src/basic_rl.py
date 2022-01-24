import random
from timeit import default_timer as timer

import numpy as np
from tqdm import tqdm


def qlearning(env, episodes, init_Q, epsilon, learning_rate, discount_factor,
              perception_to_state_mapper=lambda p: int(p)):
    Q = np.copy(init_Q)
    steps = np.zeros(episodes)

    for i in tqdm(range(episodes), desc='Q-Learning', disable=episodes == 1):
        episode_steps = 0
        state = perception_to_state_mapper(env.reset())
        done = False

        while not done:
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state, :])

            next_state, reward, done, info = env.step(action)
            next_state = perception_to_state_mapper(next_state)

            if next_state is not None:
                discounted = np.max(Q[next_state, :])
            else:
                discounted = 0

            Q[state, action] = Q[state, action] + learning_rate * (
                    reward + discount_factor * discounted - Q[state, action])

            state = next_state
            episode_steps += 1

        steps[i - 1] = episode_steps

    return Q, steps


def rlearning(env, episodes, init_R, epsilon, learning_rate, zeta,
              init_rho=0,
              perception_to_state_mapper=lambda p: int(p)):
    R = np.copy(init_R)
    rho = init_rho
    steps = np.zeros(episodes)

    for i in tqdm(range(episodes), desc='R-Learning', disable=episodes == 1):
        episode_steps = 0
        state = perception_to_state_mapper(env.reset())
        was_greedy = False
        done = False

        while not done:
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(R[state, :])
                was_greedy = True

            next_state, reward, done, info = env.step(action)
            next_state = perception_to_state_mapper(next_state)

            if next_state is not None:
                discounted = np.max(R[next_state, :])
            else:
                discounted = 0

            R[state, action] = R[state, action] + learning_rate * (
                    reward - rho + discounted - R[state, action])

            if was_greedy:
                rho = rho + zeta * (
                        reward + np.max(R[next_state, :]) - discounted - rho)

            state = next_state
            episode_steps += 1

        steps[i - 1] = episode_steps

    return R, rho, steps


def dynaq(env, episodes, Q, MODEL,
          epsilon, learning_rate, gamma, planning_steps,
          knowledge_fcn,
          metrics_trial_freq):
    # metrics
    metrics = np.zeros((4, episodes))  # steps, model_size, time, knowledge

    for i in range(episodes):
        episode_steps = 0
        past_state = env.reset()
        done = False

        start_ts = timer()

        while not done:
            # q-learning
            if random.uniform(0, 1) < epsilon:
                past_action = env.action_space.sample()
            else:
                past_action = np.argmax(Q[past_state, :])

            state, reward, done, info = env.step(past_action)

            if state is not None:
                discounted = np.max(Q[state, :])
            else:
                discounted = 0

            Q[past_state, past_action] += learning_rate * (
                    reward + gamma * discounted - Q[past_state, past_action])

            # model update
            if past_state not in MODEL:
                MODEL[past_state] = {}

            if past_action not in MODEL[past_state]:
                MODEL[past_state][past_action] = {}

            MODEL[past_state][past_action] = (state, reward)

            # planning
            for _ in range(planning_steps):
                s = random.choice(list(MODEL.keys()))
                a = random.choice(list(MODEL[s].keys()))

                (next_s, r) = MODEL[s][a]

                discounted = np.max(Q[next_s, :])
                Q[s, a] += learning_rate * (r + gamma * discounted - Q[s, a])

            # Next step
            past_state = state
            episode_steps += 1

        end_ts = timer()

        # collect metrics
        if i % metrics_trial_freq == 0:
            metrics[0, i] = episode_steps
            metrics[1, i] = sum(
                [len(actions) for state, actions in MODEL.items()])
            metrics[2, i] = end_ts - start_ts
            metrics[3, i] = knowledge_fcn(MODEL, env)

    return Q, MODEL, metrics


def run_q_learning_alternating(experiments, trials, env, epsilon,
                               learning_rate, discount_factor, init_Q,
                               perception_to_state_mapper=lambda p: int(p)):
    metrics = []

    for experiment in tqdm(range(experiments)):
        Q = init_Q

        for i in range(trials):
            if i % 2 == 0:
                Q, steps = qlearning(env, 1, Q, epsilon, learning_rate,
                                     discount_factor,
                                     perception_to_state_mapper)
                metrics.append(
                    {'agent': 'Q-Learning', 'trial': i, 'phase': 'explore',
                     'steps_in_trial': steps[0]})
            else:
                Q, steps = qlearning(env, 1, Q, 0.0, learning_rate,
                                     discount_factor,
                                     perception_to_state_mapper)
                metrics.append(
                    {'agent': 'Q-Learning', 'trial': i, 'phase': 'exploit',
                     'steps_in_trial': steps[0]})

    return metrics


def run_r_learning_alternating(experiments, trials, env, epsilon,
                               learning_rate, zeta, init_R,
                               perception_to_state_mapper=lambda p: int(p)):
    metrics = []

    for experiment in tqdm(range(experiments)):
        R = init_R
        rho = 0

        for i in range(trials):
            if i % 2 == 0:
                R, rho, steps = rlearning(env, 1, R, epsilon, learning_rate,
                                          zeta, init_rho=rho,
                                          perception_to_state_mapper=perception_to_state_mapper)
                metrics.append(
                    {'agent': 'R-Learning', 'trial': i, 'phase': 'explore',
                     'steps_in_trial': steps[0], 'rho': rho})
            else:
                R, rho, steps = rlearning(env, 1, R, 0.0, learning_rate, zeta,
                                          init_rho=rho,
                                          perception_to_state_mapper=perception_to_state_mapper)
                metrics.append(
                    {'agent': 'R-Learning', 'trial': i, 'phase': 'exploit',
                     'steps_in_trial': steps[0], 'rho': rho})

    return metrics
