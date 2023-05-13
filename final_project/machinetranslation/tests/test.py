import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    """Test case for translation functions"""

    def test_englishToFrench(self):
        """Test englishToFrench function"""
        self.assertEqual(englishToFrench('0'), '0')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench("None"), '')
        
    def test_frenchToEnglish(self):
        """Test frenchToEnglish function"""
        self.assertEqual(frenchToEnglish('0'), '0')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish("None"), '')

if __name__ == '__main__':
    unittest.main()