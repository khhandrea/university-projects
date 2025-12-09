# Reinforcement learning planning & prediction

## Execution
### Docker
```
docker build -t ku-ossp2-assignment1 .
docker run --rm -it -v path/to/directory:/volume -p 5000:8888 ku-ossp2-assignment1
# localhost:5000으로 접속 후 터미널의 token을 비밀번호로 입력하여 jupyter notebook 접속
```

### DP\.py
Reinforcement learning with dynamic programming

example:
```bash
DP.py
```

### MC\.py
Reinforcement learning with Monte Carlo learning

- 1st argument(Ne): the number of episodes

example:
```bash
MC.py 1000
```

### TD\.py
Reinforcement learning with N-step TD learning

- 1st argument(Ns): the number of step
- 2nd argument(Ne): the number of episodes

example:
```bash
TD.py 3 1000
```

### experiment\.ipynb
Experiment DP until convergence / MC, TD, 3step-TD with 100, 1000, 10000 steps and plot the data


## Subject
- Policy Type: Random Policy
- Follows OpenAI gym interface (ref. [Create custom gym environments from scratch](https://towardsdatascience.com/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e))

---

- Dynamic Planning for 4x4 Gid World
- N-step TD Learning for 4x4 Gid World
    - Ns, Ne are command line arguments
        - Ns: N-step
        - Ne: Number of Episodes
    
- Experiments
    - Learning Methods: DP, MC, 1-Step TD, 3-step TD
    - Ne for each N-step TD learning: 100, 1000, 10000, 100000
    -  Perform Experiments saving results
    -  Analyze the results of Experiments in tables or graphs
        - Compare V(s) of all learning methods
        - Compare mean or variance or bias(error) of V(s)