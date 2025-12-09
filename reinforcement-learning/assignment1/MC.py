from sys import argv

import numpy as np

from implements.agent import Agent
from implements.data_handler import write_result, read_result
from implements.data_handler import get_gridlike
from implements.world import GridWorld


def train_MC(
    *,
    size: int=4,
    alpha: float=0.01,
    gamma: float=0.99,
    reward: int=-1,
    episode_num: int=100,
    experiment_num: int=30,
    true_vs: np.ndarray
):
    # Initialize
    state_num = size * size
    population_errors = []
    means = np.array([])
    stds = np.array([])
    agent = Agent()
    env = GridWorld()

    # Train
    for experiment in range(experiment_num):
        vs = np.zeros(state_num)
        errors = []
        for episode in range(episode_num):
            MAE = sum([abs(v - true_v) for v, true_v in zip(vs, true_vs)]) / state_num
            errors.append(MAE)

            state = env.reset()
            done = False
            history = []
            while not done:
                action = agent.select_action(state)
                state, reward, done = env.step(action)
                history.append((state, reward))

            G = 0
            for state, reward in history[:-1][::-1]:
                G = reward + gamma * G
                vs[state] = vs[state] + alpha * (G - vs[state])

        population_errors.append(errors)
    population_errors = np.array(population_errors)

    print(f"MC for {episode_num} episodes prediction completed.")

    means = np.mean(population_errors, axis=0)
    stds = np.std(population_errors, axis=0)

    # Save
    write_result('MC', episode_num, vs, means, stds)

if __name__ == '__main__':
    episode_num = int(argv[1])

    true_vs, _, _ = read_result('DP')
    train_MC(episode_num=episode_num, true_vs=true_vs)
    vs, means, stds = read_result('MC', episode_num)
    print(get_gridlike(vs))