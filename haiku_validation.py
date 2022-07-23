import string

from syllabled_word import SyllabledWord

HAIKU_SCHEMA = [5, 7, 5]
HAIKU_SYLLABLE_COUNT = sum(HAIKU_SCHEMA)


def is_valid_schema(words):
    return find_valid_schema(words) is not None


def find_valid_schema(words):
    text_length = len(words)

    start, end = 0, 0
    while start <= text_length:
        while end <= text_length:
            schema_candidate = words[start:end]

            # simplified by taking the shorter syllable count of each word
            syllables_count = sum(x.syllables for x in schema_candidate)

            if syllables_count == HAIKU_SYLLABLE_COUNT:
                return schema_candidate

            end += 1

        start += 1
        end = start

    return None


def get_haiku(text):
    if isinstance(text, str):
        words = [SyllabledWord(word.strip(string.punctuation)) for word in text.split()]
    elif isinstance(text, list) and isinstance(text[0], SyllabledWord):
        words = text
    else:
        raise ValueError('Invalid argument type for "text", should be either str or list of SyllabledWord.')

    if not is_valid_schema(words):
        return None

    verses = []
    for verse_syllables in HAIKU_SCHEMA:
        success, verse, words = get_verse(words, verse_syllables)

        if success:
            verses += [verse]
        else:
            return None

    if not words:
        return '\n'.join(verses)


def find_first_valid_sequence(array, number=HAIKU_SYLLABLE_COUNT):
    # adapted from https://stackoverflow.com/a/23088128
    if number < 1 or len(array) == 0:
        return None

    if array[0].syllables == number:
        return [array[0]]

    with_v = find_first_valid_sequence(array[1:], (number - array[0].syllables))

    if with_v:
        return [array[0]] + with_v
    else:
        return find_first_valid_sequence(array[1:], number)


def find_haiku(text):
    words = [SyllabledWord(word.strip(string.punctuation)) for word in text.split()]
    sequence = find_first_valid_sequence(words, number=HAIKU_SYLLABLE_COUNT)
    return get_haiku(sequence)


def get_verse(words, verse_syllables):
    if verse_syllables not in HAIKU_SCHEMA:
        raise ValueError(f'Argument "length" must be one of {set(HAIKU_SCHEMA)}')

    return _get_verse(words, '', verse_syllables)


def _get_verse(words, current_verse, remaining_syllables):
    if remaining_syllables == 0:
        return True, current_verse, words

    for index, word in enumerate(words):
        for syllables in word.syllable_count:
            if syllables > remaining_syllables:
                continue

            next_verse = ' '.join([current_verse, str(word)]) if current_verse else str(word)
            remaining_words = words[index + 1:]
            success, haiku, remaining_words = _get_verse(remaining_words, next_verse, remaining_syllables - syllables)

            if success:
                return success, haiku, remaining_words

    return False, None, None
