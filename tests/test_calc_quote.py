import unittest

from scripts.funs import calc_quote


class QuoteCalcTest(unittest.TestCase):
    def test_quote_calc(self):
        age = 31
        gender = 'Female'
        bmi=26.5
        discount=10
        quote = calc_quote(age, gender, bmi, discount)
        self.assertEqual(quote, 450)


if __name__ == "__main__":
    unittest.main()