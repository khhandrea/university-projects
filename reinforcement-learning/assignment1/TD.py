from collections import deque
from sys import argv

import numpy as np

from implements.agent import Agent
from implements.data_handler import write_result, read_result
from implements.data_handler import get_gridlike
from implements.world import GridWorld


def train_TD(
    *,
    size: int=4,
    alpha: float=0.01,
    gamma: float=0.99,
    reward: int=-1,
    episode_num: int=100,
    n_step: int=1,
    experiment_num: int=30,
    true_vs: np.ndarray
):
    # Initialize
    state_num = size * size
    population_errors = []
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

            step = 0
            done = False
            history = deque([(state, None)])
            prev_return = 0 # n step return for t-n
            while not done:
                step += 1
                action = agent.select_action(state)
                state, reward, done = env.step(action)
                history.append((state, reward))

                # Calculate return    
                if step <= n_step:
                    prev_return += gamma ** (step - 1) * reward

                if step >= n_step:
                    prev_state, prev_reward = history.popleft()

                    if prev_reward != None:
                        prev_return -= prev_reward
                        prev_return /= gamma
                        prev_return += gamma ** (n_step - 1) * reward

                    if done:
                        target = prev_return
                    else:
                        target = prev_return + gamma ** n_step * vs[state]
                    
                    # Update vs
                    vs[prev_state] += alpha * (target - vs[prev_state])


            # Update terminal vs
            while len(history) > 1:
                prev_state, prev_reward = history.popleft()
                prev_return -= prev_reward
                prev_return /= gamma
                
                vs[prev_state] += alpha * (prev_return - vs[prev_state])

        population_errors.append(errors)
    population_errors = np.array(population_errors)

    print(f"{n_step}step-TD for {episode_num} episodes prediction completed.")

    means = np.mean(population_errors, axis=0)
    stds = np.std(population_errors, axis=0)

    # Save
    write_result(f'{n_step}stepTD', episode_num, vs, means, stds)

if __name__ == '__main__':
    n_step = int(argv[1])
    episode_num = int(argv[2])

    true_vs, _, _ = read_result('DP')
    train_TD(n_step=n_step, episode_num=episode_num, true_vs=true_vs)
    vs, means, stds = read_result(f'{n_step}stepTD', episode_num)
    print(get_gridlike(vs))