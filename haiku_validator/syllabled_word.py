from haiku_validator import syllable_counter


class SyllabledWord:
    def __init__(self, word):
        self.word = word
        self.syllable_count = set(syllable_counter.count(word))

    def __str__(self):
        return self.word

    def __repr__(self):
        return f'{self.word}, syllables: {self.syllable_count}'

    @property
    def syllables(self):
        return min(self.syllable_count)
