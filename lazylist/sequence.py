#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: sequence.py
Author: SpaceLis
Email: Wen.Li@tudelft.nl
GitHub: http://github.com/spacelis
Description:
    Some useful sequences constructed by LazyList.
    Nat(starting=1) is a sequence with
"""
__author__ = 'wenli'

from lazylist import LazyList, LazyListClass


@LazyListClass
def Nat(starting=1):
    """ A sequence of natural numbers starting from 1 (default)

    :starting: @todo
    :returns: @todo

    """
    while True:
        yield starting
        starting += 1


def EvenNat(starting=2):
    """ A sequence of even numbers starting from 2 (default)

    :starting: @todo
    :returns: @todo

    """
    return Nat(starting).filtered(lambda x: x % 2 == 0)


def OddNat(starting=1):
    """ A sequence of odd numbers starting from 1 (default)

    :starting: @todo
    :returns: @todo

    """
    return Nat(starting).filtered(lambda x: x % 2 == 1)


def isPrime(n):
    """ Check weather a number n is a prime number by tryout all prime factors

    :n: @todo
    :prime_seq: @todo
    :returns: @todo

    """
    for i in Prime:
        if i * i > n:
            return True
        if n % i == 0:
            return False


@LazyList
def Prime():
    """ Iterate through a list prime numbers, e.g., 2, 3, 5, 7, ...
    :returns: @todo

    """
    yield 2
    for i in OddNat(3).filtered(lambda x: isPrime(x)):
        yield i


@LazyList
def Fabonacci():
    """
    @return:
    """
    yield 1
    yield 1
    for n in Nat(2):
        yield Fabonacci[n-1] + Fabonacci[n-2]


@LazyList
def PascalTriangle():
    """

    @return:
    """
    add = lambda x: x[0] + x[1]
    yield [1, 1]
    for n in Nat(1):
        yield list(map(add, zip([0] + PascalTriangle[n-1], PascalTriangle[n-1]))) + [1]