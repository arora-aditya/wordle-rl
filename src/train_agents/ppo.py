import gym
import sys

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env


sys.path.append("..")
sys.path.append("../..")
import wordle_gym

# Parallel environments
def train_model():
    env = make_vec_env("wordle-v0", n_envs=100)

    model = PPO("MlpPolicy", env, verbose=1)
    try:
        model.learn(total_timesteps=1e6, log_interval=1000)
    except KeyboardInterrupt:
        pass
    model.save("wordle_ppo")
    return model

train_model()

model = PPO.load("wordle_ppo")

env = gym.make("wordle-v0")
obs = env.reset()
done = False
while not done:
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()