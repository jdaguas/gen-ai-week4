"""Run using: python3 -m unittest discover -s 03_hybrid -p 'test_*.py'"""
import unittest
from analyzer import count_words


class WordCountTests(unittest.TestCase):
    def test_lowercase_and_punctuation(self):
        self.assertEqual(count_words("Hello, hello! WORLD."), {"hello": 2, "world": 1})

    def test_empty_text(self):
        self.assertEqual(count_words(""), {})

    def test_contractions(self):
        self.assertEqual(count_words("don't don't"), {"don't": 2})


if __name__ == "__main__":
    unittest.main()
