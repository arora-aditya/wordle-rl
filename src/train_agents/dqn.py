import gym
import sys

from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env


sys.path.append("..")
sys.path.append("../..")
import wordle_gym

# Parallel environments
def train_model():
    env = make_vec_env("wordle-v0", n_envs=10)

    model = DQN(
        "MlpPolicy", 
        env,
        gamma=0.99, 
        learning_rate=5e-4,
        learning_starts=100000,
        buffer_size=10000,
        exploration_fraction=1,
        exploration_final_eps=0.5,
        target_update_interval=1000,
        train_freq=4,
        verbose=1,
    )
    try:
        model.learn(total_timesteps=1e7, log_interval=1000)
    except KeyboardInterrupt:
        pass
    model.save("wordle_dqn")
    return model

train_model()

model = DQN.load("wordle_dqn")

env = gym.make("wordle-v0")
obs = env.reset()
done = False
while not done:
    action, _states = model.predict(obs)
    print("Word:", env._valid_words[action][0])
    obs, rewards, done, info = env.step(action)
    env.render()