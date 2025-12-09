from random import choices

import numpy as np

from implements.data_handler import write_result, read_result
from implements.data_handler import get_gridlike

def train_DP(
        size: int = 4,
        gamma: float = 0.99,
        reward: int = -1,
        ):
    # Initialize
    state_num = size * size
    vs = np.zeros(state_num)
    old_vs = np.full(state_num, -1)

    # Make transition matrix
    transition = np.zeros((state_num, state_num, 4))
    for state in range(state_num):
        # Left
        next_state = (state - 1) if (state % size != 0) else state
        transition[state, next_state, 0] = 1.0
        # Up
        next_state = (state - size) if (state >= size) else state
        transition[state, next_state, 1] = 1.0
        # Right
        next_state = (state + 1) if (state % size != size - 1) else state
        transition[state, next_state, 2] = 1.0
        # Down
        next_state = (state + size) if (state < size * (size - 1)) else state
        transition[state, next_state, 3] = 1.0

    # Bellman equation
    while not np.array_equal(vs, old_vs):
        old_vs = vs.copy()
        for state in range(state_num):
            if state == state_num - 1:
                break

            new_v = 0.0
            for action in range(4):
                next_v = 0.0
                for next_state in range(state_num):
                    next_v += transition[state, next_state, action] * old_vs[next_state]
                q = reward + gamma * next_v
                new_v += 0.25 * q
            vs[state] = new_v

    print(f"DP evaluation completed.")

    # Save
    write_result('DP', 0, vs)

if __name__ == '__main__':
    train_DP()
    vs, _, _ = read_result('DP')
    print(get_gridlike(vs))