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
            syllables_count = sum(min(x.syllable_count) for x in schema_candidate)

            if syllables_count == HAIKU_SYLLABLE_COUNT:
                return schema_candidate

            end += 1

        start += 1
        end = start

    return None


def get_haiku(words):
    if not is_valid_schema(words):
        return None

    verses = []
    for verse_syllables in HAIKU_SCHEMA:
        success, verse, words = initialise_verse_recurrence(words, verse_syllables)

        if success:
            verses += [verse]
        else:
            return None
    return '\n'.join(verses)


def initialise_verse_recurrence(words, verse_syllables):
    if verse_syllables not in HAIKU_SCHEMA:
        raise ValueError(f'Argument "length" must be one of {set(HAIKU_SCHEMA)}')

    return get_verse(words, '', verse_syllables)


def get_verse(words, current_verse, remaining_syllables):
    if remaining_syllables == 0:
        return True, current_verse, words

    for index, word in enumerate(words):
        for syllables in word.syllable_count:
            if syllables > remaining_syllables:
                continue

            next_verse = ' '.join([current_verse, str(word)])
            remaining_words = words[index + 1:]
            success, haiku, remaining_words = get_verse(remaining_words, next_verse, remaining_syllables - syllables)

            if success:
                return success, haiku, remaining_words

    return False, None, None
