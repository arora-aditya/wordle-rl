from os import path

def get_5_letter_word_freqs():
    """
    Returns a list of words with 5 letters.
    """
    FILEPATH = path.join(path.dirname(path.abspath(__file__)), "data/norvig.txt")
    lines = read_file(FILEPATH)
    return {k:v for k, v in get_freq(lines).items() if len(k) == 5}


def read_file(filename):
    """
    Reads a file and returns a list of words and frequencies
    """
    with open(filename, 'r') as f:
        return f.readlines()


def get_freq(lines):
    """
    Returns a dictionary of words and their frequencies
    """
    freqs = {}
    for word, freq in map(lambda x: x.split("\t"), lines):
        freqs[word] = int(freq)
    return freqs