#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_lazy_list.py
Author: SpaceLis
Email: Wen.Li@tudelft.nl
Github: http://github.com/spacelis
Description:
    Basic tests
"""
__author__ = 'wenli'

from unittest import TestCase
from lazylist import LazyList
from lazylist import LazyListClass


class TestLazyList(TestCase):

    """ Basic Tests"""

    def setUp(self):
        """
        """
        @LazyList
        def nat():
            """ A natural number sequence. """
            i = 1
            while True:
                yield i
                i += 1
        self.nat = nat

        @LazyListClass
        def Nat(x):
            """ dummy """
            i = x
            while True:
                yield i
                i += 1
        self.Nat = Nat


    def test_LazyList(self):
        """
        @return: None
        """
        a = self.nat
        self.assertEqual(a[3], 4)

    def test_lazy_filter(self):
        """

        @return: None
        """
        a = self.nat.filtered(lambda x: x % 2 == 0)
        for i in range(1000):
            self.assertEqual(a[i] % 2, 0)

    def test_LzayListClass(self):
        """
        @return: None
        """
        a = self.Nat(10)
        self.assertEqual(a[2], 12)

