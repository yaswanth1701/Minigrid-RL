import gym
import numpy as np 
import random
from gym_minigrid.wrappers import *
import matplotlib.pyplot as plt
from numpy import load
from numpy import save
#   Sarsa for minigrid
# taking action epsilon greedy
def take_action(q_value,epsilon):
    prob=np.random.random()
    if prob<epsilon:
        print("action_taken_not_greedy")
        return np.random.randint(0,3)
    else:
        print("taken_greedy")
        return np.argmax(q_value)
# making environment
env = gym.make('MiniGrid-Empty-8x8-v0',render_mode="human")
env.reset()
# defining q values,episodes,epsilon,no of visits and discount factor(gamma)
q_value=np.zeros((3,36,4))
# number of episodes for training
episode=120
# epsilon greedy policy parameter
epsilon=1
# total number of visits to particular state-action pair during whole training
no_visits=np.zeros((3,36,4))
# discount factor
gamma=0.9
# learning rate
alpha=0.3
total_reward=np.zeros(episode)
for K in range(episode):
    print("episode_no: "+str(K+1))
    # random spawn
    env.reset()
    # exploration vs exploitation decay
    epsilon=epsilon-0.01
    # goal pos
    terminated=False
    # number of steps timeout
    truncated=False
    # 2d grid to 1d array indices
    x1=(env.agent_pos[0]-1)*6+(env.agent_pos[1]-1)
    # facing direction of agent
    x2=env.agent_dir
    #action taken according to epsilon greedy policy
    action=take_action(q_value[:,x1,x2],epsilon)
    #  all the reward obtained in all the episodes
   
    while not (terminated or truncated):
        # env.render()
        # 2d array to 1d array indices:
        x1=(env.agent_pos[0]-1)*6+(env.agent_pos[1]-1)
        x2=env.agent_dir
        # taking obervation and reward
        observation, reward, terminated, truncated, info=env.step(action)
        total_reward[K]+=reward
        # new state-action pair
        new_x1=(env.agent_pos[0]-1)*6+(env.agent_pos[1]-1)
        new_x2=env.agent_dir
        # new action to be taken
        new_action=take_action(q_value[:,new_x1,new_x2],epsilon)
        # update towards actual value using bootstrapping
        q_value[action,x1,x2]+=(reward+gamma*(q_value[new_action,new_x1,new_x2])-q_value[action,x1,x2])* alpha
        action=new_action
    print(total_reward[K])
save('reward_sarsa0.npy',total_reward)
env.close()