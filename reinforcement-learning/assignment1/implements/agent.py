from random import choices

import numpy as np

class Agent:
    def __init__(self, size: int=4):
        state_num = size * size
        self.__policy = np.full((state_num, 4), 0.25)

    def select_action(self, state: np.ndarray) -> int:
        return choices(range(4), self.__policy[state])[0]