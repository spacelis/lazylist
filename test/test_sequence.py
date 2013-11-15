__author__ = 'wenli'

from unittest import TestCase
from lazylist.sequence import Nat
from lazylist.sequence import OddNat
from lazylist.sequence import EvenNat
from lazylist.sequence import Prime
from lazylist.sequence import Fabonacci
from lazylist.sequence import PascalTriangle


class TestLazyList(TestCase):

    """ Basic Tests"""

    def test_Nat(self):
        """

        @return:
        """
        self.assertEqual(Nat(5)[:10], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(Nat()[4], 5)

    def test_OddNat(self):
        """

        @return:
        """
        self.assertEqual(OddNat(5)[:10], [5, 7, 9, 11, 13, 15, 17, 19, 21, 23])

    def test_EvenNat(self):
        """

        @return:
        """
        self.assertEqual(EvenNat(5)[:10], [6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_Prime(self):
        """
        @return: None
        """
        self.assertEqual(Prime[:5], [2, 3, 5, 7, 11])

    def test_Fabonacci(self):
        """

        @return:
        """
        self.assertEqual(Fabonacci[:10], [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_PascalTriangle(self):
        """

        @return:
        """
        self.assertEqual(PascalTriangle[:4], [[1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
