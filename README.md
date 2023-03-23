# Classical-RL
This repository contains all the tabular RL algorithms  from Monte-Carlo - Q Learning, most which are implemented on minigrid environment
#### This repo made to learn and implemented differet classical/tabular alogrithms taught by David Silver at deep mind
### Environment:
#### Present environments:
- `MiniGrid-Empty-3x3-v0`:
state space and action space
| States | # ```env.agent_pos```(position of agent in grid(tuple))   | # ```env.agent_dir```(face direction of agent)    |
| :---:   | :---: | :---: |
| actions| # turn right(0)   | # turn left (1)  | # move forward(one step)(2)|
- `MiniGrid-Empty-8x8-v0`
### General parameter and hyperparameters
- Episodes: all the alogrithms are initially ran for **150** episodes for training the policy(this might be altered depending upon convergence of particular alogrithm)
- All alogrithms follow ε-greedy policy. Except in case of Q learning base policy follows ε-greedy policy and target policy follows greedy policy)
- Initially ε for each case decreases by **0.01** for every episode to ensure proper exploration vs exploitation of policy.(Might be greater for monte-carlo)
- The update paramter α is set to **0.3** and works fine for all.
- The discount factor γ is set to 0.9 for all cases and works for fine for all.
- The parameter λ is set to 0.9 for SARSA-λ and backward-view SARSA
## Rewared vs episodes
### monte-carlo
### SARSA/SARSA-0
### SARSA-λ(Forward-view)
### SARSA(Backward-view)
### Q Learning
