import unittest

from haiku_validator.haiku_validation import get_haiku


class TestHaikuDetection(unittest.TestCase):
    def test_valid_string(self):
        text = 'An old silent pond...\n' \
               'A frog jumps into the pond,\n' \
               'splash! Silence again.\n'
        haiku = get_haiku(text)

        self.assertTrue(haiku)
        self.assertEqual(haiku, 'An old silent pond\nA frog jumps into the pond\nsplash Silence again')

    def test_invalid_string(self):
        text = 'A short story is a piece of prose fiction that typically can be read in one sitting and focuses on a self-contained incident or series of linked incidents.'
        haiku = get_haiku(text)

        self.assertFalse(haiku)
