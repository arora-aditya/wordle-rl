import gym
import sys

from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env


sys.path.append("..")
sys.path.append("../..")
import wordle_gym

# Parallel environments
env = gym.make("wordle-v0")

reward = -1
while True:
    env.reset()
    done = False
    while not done:
        obs, reward, done, _ = env.step(env.action_space.sample())  # take a random action 	
    if reward > 0:
        env.render()
        break
    print(f"REWARD: {reward}")
env.close()