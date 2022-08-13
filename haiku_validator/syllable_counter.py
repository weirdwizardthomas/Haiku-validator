from nltk.corpus import cmudict

VOWELS = 'aeiouy'
DICTIONARY = cmudict.dict()


def count(word):
    try:
        word = word.lower()
        entry = DICTIONARY[word]
        return [len(list(y for y in x if y[-1].isdigit())) for x in entry]
    except KeyError:  # if word not found in cmudict
        return manual_count(word)


def manual_count(word):
    # referred from stackoverflow.com/questions/14541303/count-the-number-of-syllables-in-a-word
    count = 0
    if word[0] in VOWELS:
        count += 1

    for index in range(1, len(word)):
        if word[index] in VOWELS and word[index - 1] not in VOWELS:
            count += 1

    if word.endswith('e'):
        count -= 1

    if word.endswith('le'):
        count += 1

    return max(1, count)
