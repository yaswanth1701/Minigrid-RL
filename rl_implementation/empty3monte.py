import gym
import numpy as np 
import random
import empty3monte
from gym_minigrid.wrappers import *
import matplotlib.pyplot as plt
from numpy import load
from numpy import save
# every episode monte carlo control for minigrid
# taking action epsilon greedy
def take_action(state,q_value,epsilon):
    prob=np.random.random()
    if prob<epsilon:
        # print("non_greedy")
        return np.random.randint(0,3)
    else:
        # print("greedy")
        return np.argmax(q_value)
# making environment
env = gym.make('MiniGrid-Empty-8x8-v0',render_mode="human")
env.reset()
#defining q values,episodes,epsilon,no of visits and discount factor(gamma)
q_value=np.zeros((3,36,4))
episode=150
epsilon=1
no_visits=np.zeros((3,36,4))
gamma=0.9
#  all the reward obtained in all the episodes
total_reward=np.zeros(episode)

for K in range(episode):
    print("episode_no: "+str(K+1))
    total_return=np.zeros((3,36,4))

    # random spawn
    env.reset()
    # exploration vs exploitation decay
    epsilon-=0.01
    # to remember visited state and to udpate the total return for action and state pair
    visited_states=[]
    terminated=False
    # measure of time in each episode
    time=0
    while not terminated:
        # env.render()
        # 2d array to 1d array indices:
        x1=(env.agent_pos[0]-1)*6+(env.agent_pos[1]-1)
        x2=env.agent_dir
        # taking action according to epsilon greedy policy
        action =take_action([x1,x2],q_value[:,x1,x2],epsilon)
        if [action,x1,x2] not in visited_states:
            visited_states.append([action,x1,x2])
        # updating number of visits every visit monte carlo
        no_visits[action,x1,x2]+=1
        # taking obervation and reward
        observation, reward, terminated, truncated, info=env.step(action)
        if reward<0:
            reward=0
        # updating total return recieved from state action pair
        for i,state in enumerate(visited_states):
            total_return[state[0],state[1],state[2]]+=(gamma**(time-i))*reward
        time=time+1
        total_reward[K]+=reward
        
    print(total_reward[K])
    for i,state in enumerate(visited_states):
        # update step toward actual action value using episodes of exprience
        q_value[state[0],state[1],state[2]]+=(total_return[state[0],state[1],state[2]]-q_value[state[0],state[1],state[2]])/no_visits[state[0],state[1],state[2]]
save('montecarlo_reward.npy',total_reward)
env.close()
