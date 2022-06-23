import unittest
from translator import english_to_french, french_to_english

class EnglishTranslatorTest(unittest.TestCase):
    def test_null(self):
        self.assertNotEqual("", english_to_french("Hello"))
    
    def test_hello_word(self):
        self.assertEqual("Bonjour", english_to_french("Hello"))

class FrenchTranslatorTest(unittest.TestCase):
    def test_null(self):
        self.assertNotEqual("", french_to_english("Bonjour"))
    
    def test_hello_word(self):
        self.assertEqual("Hello", french_to_english("Bonjour"))

unittest.main()