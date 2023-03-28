# Classical-RL
This repository contains all the tabular RL algorithms  from Monte-Carlo - Q Learning, most which are implemented on minigrid environment
#### This repo made to learn and implemented differet classical/tabular alogrithms taught by David Silver at deep mind
### Environment:
#####  Minigrid
#### Current Status: 
- [X] Empty
- [X] Dyanamic obstacles
- [ ] FourRooms
#### Present environments:

- Empty(Empty grid)
<p align="center">

<img src="https://user-images.githubusercontent.com/92177410/227360283-b990b65a-57cb-473c-b0ba-7eec1dda3158.gif" width="300" height="300">
</p>

- `MiniGrid-Empty-5x5-v0`
- `MiniGrid-Empty-8x8-v0`

##### Reward:
- Everywhere reward is **0** except for the goal position which has a reward of **1**. 
- The total amount of reward recieved in a episode is  ```1-0.9*steps/max_steps```.



#####   State space:




states         
:-------------------------:
`env.agent_pos` (position of agent in grid)
`env.agent_dir` (direction of head of agent) (0,4)

##### Action space:
states         
:-------------------------:
```turn right``` (0)
```turn_left``` (1)
```move_forward``` (2)








### General parameter and hyperparameters
- Episodes: all the alogrithms are initially ran for **150** episodes for training the policy(this might be altered depending upon convergence of particular alogrithm)
- All alogrithms follow ε-greedy policy. Except in case of Q learning base policy follows ε-greedy policy and target policy follows greedy policy)
- Initially ε for each case decreases by **0.01** for every episode to ensure proper exploration vs exploitation of policy.(Might be greater for monte-carlo)
- The update paramter α is set to **0.3** and works fine for all.
- The discount factor γ is set to 0.9 for all cases and works for fine for all.
- The parameter λ is set to 0.9 for SARSA-λ and backward-view SARSA
## Rewared vs episodes
- `MiniGrid-Empty-8x8-v0`
<p align="center">
<img src="https://user-images.githubusercontent.com/92177410/227701555-481297ce-480f-496c-89f7-2a35fbb057e7.png" width="800" height="400">

</p>



### Monte-Carlo
### SARSA/SARSA-0
### SARSA-λ(Forward-view)
### SARSA(Backward-View)
- SARSA(Backward-View) converges to optimal policy with very little training as compared to other algorithms due to online updates.
<p align="center">
<img src="https://user-images.githubusercontent.com/92177410/227707354-2b07b955-c3ba-43a0-bd84-fbaf6959be63.png" width="800" height="400">

</p>


### Q Learning



#### Future environments:
 - Four rooms
 <p align="center">

<img src="https://user-images.githubusercontent.com/92177410/227493413-dae22696-63fc-4630-917c-5e4de8a671fc.gif" width="300" height="300">

</p>

- Dynamic obstacles
 
 
  <p align="center">

<img src="https://user-images.githubusercontent.com/92177410/228380260-0048dae2-d5a2-4155-9d79-4f88f331b885.gif" width="300" height="300">

</p>

