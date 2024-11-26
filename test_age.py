import unittest
from age import categorize_by_age


class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        self.assertEqual(categorize_by_age(7), 'Child')

    def test_teenager(self):
        self.assertEqual(categorize_by_age(17), 'Teenager')

    def test_adult(self):
        self.assertEqual(categorize_by_age(27), 'Adult')

    def test_senior(self):
        self.assertEqual(categorize_by_age(67), 'Senior')

    def test_negative_age(self):
        self.assertEqual(categorize_by_age(-10), 'Invalid age: -10')

    @unittest.skip('I do not want to handle exceptions yet!')
    def test_invalid_age(self):
        self.assertEqual(categorize_by_age('a'), 'Invalid age: a')


if __name__ == '__main__':
    unittest.main(verbosity=2)
