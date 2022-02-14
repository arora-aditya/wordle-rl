import gym
import sys

from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env


sys.path.append("..")
sys.path.append("../..")
import wordle_gym

def train_model():
    # Parallel environments
    env = make_vec_env("wordle-v0", n_envs=1)

    model = A2C("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=1e6, log_interval=1000)
    model.save("wordle_a2c")
    return model

# train_model()

model = A2C.load("wordle_a2c")

env = gym.make("wordle-v0")
for i in range(100):
    obs = env.reset()

done = False
while not done:
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    print(rewards, _states)
    env.render()