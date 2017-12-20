import unittest
import Base23

class TestGetProperDivisors(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Base23.get_proper_divisors(1), set([]))

    def test_2(self):
        self.assertEqual(Base23.get_proper_divisors(2), set([1]))

    def test_4(self):
        self.assertEqual(Base23.get_proper_divisors(4), set([1,2]) )

    def test_28(self):
        self.assertEqual(Base23.get_proper_divisors(28),set([1,2,4,7,14]) )

class TestIsAbundant(unittest.TestCase):
    def test_2(self):
        self.assertFalse(Base23.is_abundand(2))

    def test_4(self):
        self.assertFalse(Base23.is_abundand(4))

    def test_12(self):
        self.assertTrue(Base23.is_abundand(12))

    def test_18(self):
        self.assertTrue(Base23.is_abundand(18))

    def test_20(self):
        self.assertTrue(Base23.is_abundand(20))

    def test_21(self):
        self.assertFalse(Base23.is_abundand(21))

    def test_28(self):
        self.assertFalse(Base23.is_abundand(28))

    def test_119(self):
        self.assertFalse(Base23.is_abundand(119))

    def test_120(self):
        self.assertTrue(Base23.is_abundand(120))

    def test_121(self):
        self.assertFalse(Base23.is_abundand(121))

class TestIsSumOfTwoAbundant(unittest.TestCase):
    def test_2(self):
        self.assertFalse(Base23.is_sum_of_two_abundant(2))

    def test_4(self):
        self.assertFalse(Base23.is_sum_of_two_abundant(4))

    def test_24(self):
        self.assertTrue(Base23.is_sum_of_two_abundant(24))

    def test_28123(self):
        self.assertTrue(Base23.is_sum_of_two_abundant(28123))

    def test_28124(self):
        self.assertTrue(Base23.is_sum_of_two_abundant(28124))

if __name__ == '__main__':
    unittest.main()