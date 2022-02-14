import gym
import sys

from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from collections import Counter

sys.path.append("..")
sys.path.append("../..")
import wordle_gym

# Parallel environments
env = gym.make("wordle-v0")

env.reset()
done = False
while not done:
    guess = input("Guess: ").lower()
    while True:
        try:
            action = env._valid_words.index((guess, Counter(guess)))
            break
        except:
            guess = input("Guess: ").lower()

    obs, reward, done, _ = env.step(action)  # take a random action
    env.render()
    print(f"REWARD: {reward}")
env.close()