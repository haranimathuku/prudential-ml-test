import unittest

from scripts.funs import calc_bmi


class BMICalcTest(unittest.TestCase):
    def test_bmi_calc(self):
        height = 510
        weight = 205
        bmi = calc_bmi(height, weight)
        self.assertEqual(bmi, 29.4)


if __name__ == "__main__":
    unittest.main()