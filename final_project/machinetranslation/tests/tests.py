import unittest
import machinetranslation.translator as translator

class EnglishTranslatorTest(unittest.TestCase):
    def test_null_input(self):
        self.assertRaises(ValueError, translator.englishToFrench(""))
    
    def test_hello_word(self):
        self.assertEqual("Bonjour", translator.englishToFrench("Hello"))

class FrenchTranslatorTest(unittest.TestCase):
    def test_null_input(self):
        self.assertRaises(ValueError, translator.frenchToEnglish(""))
    
    def test_hello_word(self):
        self.assertEqual("Hello", translator.frenchToEnglish("Bonjour"))

unittest.main()