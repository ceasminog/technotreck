import unittest

from app import multiply


class TestMyFunc(unittest.TestCase):
        def test_multiply(self):
                    self.assertEqual(multiply(2, 3),6)
