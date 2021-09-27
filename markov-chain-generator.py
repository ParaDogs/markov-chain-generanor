from os import makedirs
from sys import path_importer_cache
import numpy as np
from numpy import random
from numpy.core.defchararray import join

data = open("data.txt", 'r', encoding="utf-8").read()

class Generator:
    def __init__(self, text):
        words = text.split(' ')
        n_words = len(words)
        self.dict = {}
        pair = Generator.make_pairs(words)
        # pair is a pairs generator
        for word1, word2 in pair:
            if word1 in self.dict.keys():
                self.dict[word1].append(word2)
            else:
                self.dict[word1] = [word2]

    def make_pairs(words):
        for i in range(len(words)-1):
            yield (words[i], words[i+1])

    def generate(self, n):
        first_word = np.random.choice([*self.dict.keys()])
        while not first_word.istitle():
            first_word = np.random.choice([*self.dict.keys()])
        chain = [first_word]
        
        for i in range(n):
            chain.append(np.random.choice(self.dict[chain[-1]]))

        return ' '.join(chain)


generator = Generator(data)
print(generator.generate(20))