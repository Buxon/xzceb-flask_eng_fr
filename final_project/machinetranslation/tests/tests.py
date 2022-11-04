import unittest
from translator import english_to_french, french_to_english

class TestEnToFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour", "Wrong translation from english to french")
        self.assertIsNone(english_to_french(None))


class TestFrToEn(unittest.TestCase): 
    def test1(self):  
        self.assertEqual(french_to_english("Bonjour"), "Hello", "Wrong translation from french to english")
        self.assertIsNone(french_to_english(None))

unittest.main()


