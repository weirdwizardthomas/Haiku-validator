import os
import string

from haiku_validation import get_haiku
from syllabled_word import SyllabledWord

with open(os.path.join('data', 'matsuo_basho_frog.txt'), 'r') as file:
    text = ''.join(file.readlines())

words = [SyllabledWord(word.strip(string.punctuation)) for word in text.split()]

print(get_haiku(words))
