from numpy import load
import matplotlib.pyplot as plt
reward_sarsa0=load('reward_sarsa0.npy')
reward_monte=load('montecarlo_reward.npy')
reward_sarsal=load('sarsalamda_reward.npy')
reward_sarsab=load('total_reward_backview_sarsa.npy')
reward_q=load("q_learning_reward.npy")


fig=plt.figure(figsize=(8,4))
plt.plot(reward_monte,label="monte-carlo")
plt.plot(reward_sarsa0,label="SARSA")
plt.plot(reward_sarsal,label="SARSAλ")
plt.plot(reward_sarsab,label="backward_view_SARSA")
plt.plot(reward_q,label="Q_learning")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.grid()
plt.legend()
plt.show()