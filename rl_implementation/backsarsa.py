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
episode=150
epsilon=1
no_visits=np.zeros((3,36,4))
gamma=0.9
alpha=0.3
lamda=0.9
total_reward=np.zeros(episode)
for K in range(episode):
    print("episode_no: "+str(K+1))
    # random spawn
    env.reset()
    # exploration vs exploitation decay
    epsilon=epsilon-0.01
    if epsilon<0.04:
        epsilon=0.0001
    # to remember visited state and to udpate the total return for action and state pair
    terminated=False
    x1=(env.agent_pos[0]-1)*6+(env.agent_pos[1]-1)
    x2=env.agent_dir
    action=take_action(q_value[:,x1,x2],epsilon)
    #  all the reward obtained in all the episodes
   
    visited_states=[]
    E=np.zeros((3,36,4))
    while not terminated:
        # env.render()
        # 2d array to 1d array indices:
        x1=(env.agent_pos[0]-1)*6+(env.agent_pos[1]-1)
        x2=env.agent_dir
        E[action,x1,x2]=1
        # taking obervation and reward
        observation, reward, terminated, truncated, info=env.step(action)
        if reward<0:
            reward=0
        # updating total return recieved from state action pair
        total_reward[K]+=reward
        if [action,x1,x2] not in visited_states:
            visited_states.append([action,x1,x2])
        # update step toward actual action value using episodes of exprience
        new_x1=(env.agent_pos[0]-1)*6+(env.agent_pos[1]-1)
        new_x2=env.agent_dir
        new_action=take_action(q_value[:,new_x1,new_x2],epsilon)
        for i,state in enumerate(visited_states):
            error=(reward+gamma*(q_value[new_action,new_x1,new_x2])-q_value[action,x1,x2])
            q_value[state[0],state[1],state[2]]+=alpha*(E[state[0],state[1],state[2]])*error
        action=new_action
        E=gamma*lamda*E
    print(total_reward[K])
save('total_reward_backview_sarsa',total_reward)
# q_value = load('q_values.npy')

        
episodes=np.arange(1,101)
    # print(pos)
# action value for each coordinate and each direction is a state and actions are turn right, turn left and move forward.
# get coordinate and direction
# env.close()
# plt.plot(episodes,total_reward)
# plt.show()