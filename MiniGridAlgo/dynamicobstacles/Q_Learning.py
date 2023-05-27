import gym
import numpy as np 
import random
import matplotlib.pyplot as plt
from numpy import load
from numpy import save
#   Sarsa for minigrid
# taking action epsilon greedy
def take_action(q_value,epsilon):
    prob=np.random.random()
    if prob<epsilon:
        # print("action_taken_not_greedy")
        return np.random.randint(0,3)
    else:
        # print("taken_greedy")
        return np.argmax(q_value)
# making environment
env = gym.make('MiniGrid-Dynamic-Obstacles-Random-6x6-v0',render_mode="human")
env.reset()
# defining q values,episodes,epsilon,no of visits and discount factor(gamma)
q_value=np.zeros((3,16,4,2))
episode=600
epsilon=1
gamma=0.9
alpha=0.3
lamda=0.99
total_reward=np.zeros(episode)

for K in range(episode):
    print("episode_no: "+str(K+1))
    # random spawn
    env.reset()
    # exploration vs exploitation decay
    epsilon-=0.002
    # to remember visited state and to udpate the total return for action and state pair
    terminated=False
    truncated=False
    terminated=False
    truncated=False
    front_cell = env.grid.get(*env.front_pos)
    not_clear = front_cell and front_cell.type != "goal"
    if not_clear:
        x3=1
    else:
        x3=0
    x1=(env.agent_pos[0]-1)*4+(env.agent_pos[1]-1)
    x2=env.agent_dir
    action=take_action(q_value[:,x1,x2,x3],epsilon)
    #  all the reward obtained in all the episodes
    
    while not (terminated or truncated):
        # env.render()
        # 2d array to 1d array indices:
        x1=(env.agent_pos[0]-1)*4+(env.agent_pos[1]-1)
        x2=env.agent_dir
        # taking obervation and reward
        observation, reward, terminated, truncated, info=env.step(action)
        # updating total return recieved from state action pair
        total_reward[K]+=reward
        # update step toward actual action value using episodes of exprience
        new_x1=(env.agent_pos[0]-1)*4+(env.agent_pos[1]-1)
        new_x2=env.agent_dir

        front_cell = env.grid.get(*env.front_pos)
        not_clear = front_cell and front_cell.type != "goal"

        if not_clear:
            new_x3=1
        else:
            new_x3=0
        
        new_action=take_action(q_value[:,new_x1,new_x2,new_x3],epsilon)
        error=(reward+gamma*(max(q_value[:,new_x1,new_x2,new_x3]))-q_value[action,x1,x2,x3])
        q_value[action,x1,x2,x3]+=alpha*error
        action=new_action
        x3=new_x3
    print(total_reward[K])
save("q_learning_reward100.npy",total_reward)
# q_values = load('q_values.npy')
# print(q_values)
# env.reset()
# while True:
#     x1=(env.agent_pos[0]-1)*3+(env.agent_pos[1]-1)
#     x2=env.agent_dir
#     action=take_action(q_values[:,x1,x2],0)
#     observation, reward, terminated, truncated, info=env.step(action)
#     if terminated:
#         break


        
# episodes=np.arange(1,101)
#     # print(pos)
# # action value for each coordinate and each direction is a state and actions are turn right, turn left and move forward.
# # get coordinate and direction
episodes=np.arange(1,101)
env.close()
# plt.plot(episodes,total_reward)
# plt.show()