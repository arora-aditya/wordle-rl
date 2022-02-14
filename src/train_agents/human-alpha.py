import gym
import sys

from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from collections import Counter

sys.path.append("..")
sys.path.append("../..")
import wordle_gym

# Parallel environments
env = gym.make("wordle-alpha-v0")

env.reset()
done = False
while not done:
    guess = input("Guess: ").lower()
    action = [ord(x) - ord('a') for x in guess]

    obs, reward, done, _ = env.step(action)  # take a random action
    env.render()
    print(f"REWARD: {reward}")
env.close()