import os

from haiku_validation import get_haiku, find_haiku

with open(os.path.join('data', 'matsuo_basho_frog.txt'), 'r') as file:
    text = ''.join(file.readlines())

print(get_haiku(text))

with open(os.path.join('data', 'input_01.txt'), 'r') as file:
    text = ''.join(file.readlines())

print(find_haiku(text))
