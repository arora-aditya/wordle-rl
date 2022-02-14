import os


import gym
from gym import error, spaces, utils
from gym.utils import seeding

from enum import Enum
from collections import Counter
import numpy as np

WORD_LENGTH = 5
TOTAL_GUESSES = 6
SOLUTION_PATH = "../words/solution.csv"
VALID_WORDS_PATH = "../words/guess.csv"

class LetterState(Enum):
    ABSENT = 0
    PRESENT = 1
    CORRECT_POSITION = 2


class WordleEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    def _current_path(self):
        return os.path.dirname(os.path.abspath(__file__))

    def _read_solutions(self):
        return open(os.path.join(self._current_path(), SOLUTION_PATH)).read().splitlines()
    
    def _get_valid_words(self):
        words = []
        for word in open(os.path.join(self._current_path(), VALID_WORDS_PATH)).read().splitlines():
            words.append((word, Counter(word)))
        return words


    def __init__(self):
        self._solutions = self._read_solutions()
        self._valid_words = self._get_valid_words()
        self.action_space = spaces.MultiDiscrete([26] * WORD_LENGTH)
        self.observation_space = spaces.Box(low=0, high=2, shape=(TOTAL_GUESSES, WORD_LENGTH))
        np.random.seed(0)
        self.reset()
    
    def _check_guess(self, guess, guess_counter):
        c = guess_counter & self.solution_ct
        result = []
        correct = True
        reward = 0
        for i, char in enumerate(guess):
            if c.get(char, 0) > 0:
                if self.solution[i] == char:
                    result.append(2)
                    reward += 2
                else:
                    result.append(1)
                    correct = False
                    reward += 1
                c[char] -= 1
            else:
                result.append(0)
                correct = False
        return result, correct, reward

    def step(self, action):
        """
        action: index of word in valid_words

        returns:
            observation: (TOTAL_GUESSES, WORD_LENGTH)
            reward: 0 if incorrect, 1 if correct, -1 if game over w/o final answer being obtained
            done: True if game over, w/ or w/o correct answer
            additional_info: empty
        """
        self.guess_no += 1
        guess = "".join(map(lambda x: chr(x + 97), action))
        guess_counter = Counter(guess)
        self.guesses.append(guess)
        result, correct, reward = self._check_guess(guess, guess_counter)
        done = False
        if correct:
            done = True
            reward = 15
        if self.guess_no == TOTAL_GUESSES:
            done = True
            if not correct:
                reward = -15
        self.obs[self.guess_no-1] = result
        return self.obs, reward, done, {}

    def reset(self):
        self.solution = self._solutions[np.random.randint(len(self._solutions))]
        self.solution_ct = Counter(self.solution)
        self.guess_no = 0
        self.guesses = []
        self.obs = np.zeros((TOTAL_GUESSES, WORD_LENGTH))

    def render(self, mode="human"):
        m = {
            0: "⬜",
            1: "🟨",
            2: "🟩"
        }
        print("Solution:", self.solution)
        for g, o in zip(self.guesses, self.obs):
            o_n = "".join(map(lambda x: m[x], o))
            print(g, o_n)

    def close(self):
        pass

if __name__ == "__main__":
    env = WordleEnv()
    print(env.action_space)
    print(env.observation_space)
    print(env.solution)
    print(env.step(0))
    print(env.step(0))
    print(env.step(0))
    print(env.step(0))
    print(env.step(0))
    print(env.step(0))