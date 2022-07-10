from random import sample
from typing import List

from base import Strategy
from base import StrategyType

from utils import freq

class Random(Strategy):
    def __init__(self):
        self.words = freq.get_5_letter_word_freqs()
        super().__init__(StrategyType.RANDOM)

    def get_best_word(self, state: List[List[int]]):
        


if __name__ == "__main__":
    r = Random()
    print(r.get_best_word([]))