import unittest

from context import sample

import sample.util.calc as calc

class SqTest(unittest.TestCase):
    def test_sq(self):
        self.assertEqual(calc.mysq(9), 81)

if __name__ == "__main__":
    unittest.main()
