"""
Sample Test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test case of calc module"""

    def test_add_number(self):
        """Test adding number together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub_number(self):
        """Test subtracting numbers together"""
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)
