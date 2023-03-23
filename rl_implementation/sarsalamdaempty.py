import gym
import numpy as np 
import random
from gym_minigrid.wrappers import *
import matplotlib.pyplot as plt
from numpy import load
from numpy import save
# every episode monte carlo control for minigrid
# taking action epsilon greedy
def take_action(q_value,epsilon):
    prob=np.random.random()
    if prob<epsilon:
        print("non_greedy")
        return np.random.randint(0,3)
    else:
        print("greedy")
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
lamda=0.9
alpha=0.3
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
    x1=(env.agent_pos[0]-1)*6+(env.agent_pos[1]-1)
    x2=env.agent_dir
    action =take_action(q_value[:,x1,x2],epsilon)
    # measure of time in each episode
    time=0
    # q lamba value
    q_lamda=np.zeros((3,36,4))
    while not terminated:
        # env.render()
        # 2d array to 1d array indices:
        x1=(env.agent_pos[0]-1)*6+(env.agent_pos[1]-1)
        x2=env.agent_dir
        
        # taking action according to epsilon greedy policy
        if [action,x1,x2] not in visited_states:
            visited_states.append([action,x1,x2])
        # updating number of visits every visit monte carlo
        no_visits[action,x1,x2]+=1
        # taking obervation and reward
        observation, reward, terminated, truncated, info=env.step(action)
        if reward<0:
            reward=0
        # updating total return recieved from state action pair
        new_x1=(env.agent_pos[0]-1)*6+(env.agent_pos[1]-1)
        new_x2=env.agent_dir
        new_action=take_action(q_value[:,new_x1,new_x2],epsilon)
        for i,state in enumerate(visited_states):
            total_return[state[0],state[1],state[2]]+=(gamma**(time-i))*reward
            q_lamda[state[0],state[1],state[2]]+=(1-lamda)*(lamda**(time-i))*(total_return[state[0],state[1],state[2]]+(gamma**(time-i+1))*q_value[new_action,new_x1,new_x2])
        time=time+1
        total_reward[K]+=reward
        action=new_action
    print(total_reward[K])
    for i,state in enumerate(visited_states):
        # update step toward actual action value using episodes of exprience
        q_value[state[0],state[1],state[2]]+=(q_lamda[state[0],state[1],state[2]]-q_value[state[0],state[1],state[2]])*alpha
save('sarsalamda_reward.npy',total_reward)
# q_values = load('q_values.npy')
# while True:
#     env.render()
#     x1=(env.agent_pos[0]-1)*3+(env.agent_pos[1]-1)
#     x2=env.agent_dir
#     action=take_action([x1,x2],q_values[:,x1,x2],0)
#     observation, reward, terminated, truncated, info=env.step(action)
#     if terminated:
#         break

        
episodes=np.arange(1,101)

    # print(pos)
# action value for each coordinate and each direction is a state and actions are turn right, turn left and move forward.
# get coordinate and direction
env.close()
print(episodes)
plt.plot(episodes,total_reward)
plt.show()