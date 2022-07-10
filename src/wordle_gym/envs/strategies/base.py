from enum import Enum

from typing import List

class StrategyType(Enum):
    RANDOM = 1
    ELIMINATION = 2
    PROBABILITY = 3

class Strategy:
    def __init__(self, type: StrategyType):
        self.type = type
    
    def get_best_word(self, guesses: List[List[str]], state: List[List[int]]):
        raise NotImplementedError("Strategy.get_best_word() not implemented")