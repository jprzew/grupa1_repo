import unittest
import random
from age import categorize_by_age


class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        interval = (1, 10)

        test_cases_integer = list(range(*interval))
        test_cases_float = [random.uniform(*interval)]


        for case in test_cases_float + test_cases_integer:
            with self.subTest(number=case):
                self.assertEqual(categorize_by_age(case), 'Child')

    def test_teenager(self):
        test_cases_integer = list(range(10, 20))
        test_cases_float = [10.2, 14.5, 16.8, 18.6, 15.7, 11.1]

        for case in test_cases_float + test_cases_integer:
            with self.subTest(number=case):
                self.assertEqual(categorize_by_age(case), 'Teenager')

    def test_adult(self):
        test_cases_integer = list(range(20, 66))
        test_cases_float = [41.2, 54.5, 26.8, 48.6, 64.7, 31.1]

        for case in test_cases_float + test_cases_integer:
            with self.subTest(number=case):
                self.assertEqual(categorize_by_age(case), 'Adult')

    def test_senior(self):
        test_cases_integer = list(range(66, 100))
        test_cases_float = [71.2, 74.5, 86.8, 98.6, 75.7, 71.1]

        for case in test_cases_float + test_cases_integer:
            with self.subTest(number=case):
                self.assertEqual(categorize_by_age(case), 'Senior')

    def test_negative_age(self):
        self.assertEqual(categorize_by_age(-10), 'Invalid age: -10')

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            categorize_by_age('a')


class TestCollections(unittest.TestCase):


    def test_sequence_objects(self):
        a = ('H', 'e', 'l', 'l', 'o')
        b = 'Hello'
        self.assertSequenceEqual(a, b)

    def test_string_objects(self):
        a = """Litwo ojczyzno moja!
               Ty jesteś jak zdrowie"""
        b = """Litwo ojczyzno moja!
               Ty jesteś jak zdrowie"""

        self.assertMultiLineEqual(a, b)

    # assertListEqual

    # assertTupleEqual

    # assertDictEqual

    # assertSetEqual
    def test_set_objects(self):
        a = {1, 2, 3, 4}
        b = {4, 2, 1, 3}
        self.assertSetEqual(a, b)

# Przykłady popularnych funkcji typu assert
# assertNotEqual
# assertTrue
# assertFalse
# assertGreater
# assertGreaterEqual
# assertLess
# assertLessEqual
# assertIsNone
# assertIsNotNone








if __name__ == '__main__':
    unittest.main(verbosity=2)
