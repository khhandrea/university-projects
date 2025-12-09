# (Data format)
# 이름: (experiment)-(step).txt
# 첫번째 줄: 최종 V값
# 두번째 줄: step별 loss (띄어쓰기로 구분)
# experiment: DP, MC, TD 1step, TD 3step
# step: 100, 1000, 10000, 100000
# (경우의수 총 16개)
from typing import Tuple

import numpy as np

def __file_path(experiment: str, episode_num: int=0) -> str:
    return f'data/{experiment}-{episode_num}.txt'

def write_result(
        experiment: str,
        episode_num: int,
        vs: np.ndarray,
        means: np.ndarray=None,
        std: np.ndarray=None
        ) -> None:
    path = __file_path(experiment, episode_num)
    np2line = lambda arr: ' '.join(map(str, arr)) + '\n'

    with open(path, 'w') as file:
        file.write(np2line(vs))

        if experiment != 'DP':
            file.write(np2line(means))
            file.write(np2line(std))

def read_result(
        experiment: str,
        episode_num: int=0,
        size: int=4
        ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    path = __file_path(experiment, episode_num)
    line2np = lambda line: np.array(list(map(float, line.split())))

    
    with open(path, 'r') as file:
        line = file.readline()
    vs = line2np(line)

    if experiment == 'DP':    
        return vs, None, None
    else:
        with open(path) as file:
            lines = file.readlines()

        # vs
        vs = line2np(lines[0])
        # means
        means = line2np(lines[1])
        # stds
        stds = line2np(lines[2])

    return vs, means, stds

def get_gridlike(state: np.ndarray, size=4) -> np.ndarray:
    return state.reshape((4, -1))