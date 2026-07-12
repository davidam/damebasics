#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2026  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with damebasics; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from unittest import TestCase
from functools import reduce

class TestLambda(TestCase):

    def test_lambda_basic(self):
        x = lambda a, b, c : a + b + c
        self.assertEqual(x(5, 6, 4), 15)
        x = lambda a, b : a * b
        self.assertEqual(x(5, 6), 30)
        x = lambda x: 2 ** x
        self.assertEqual(x(3), 8)

    def test_lambda_map_power(self):
        x = list(map(lambda x: 2 ** x, range(10)))
        self.assertEqual(x, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512])

    def test_lambda_map_upper(self):
        a = ["apple", "banana", "cherry"]
        # Use map() with lambda to convert each string to uppercase
        b = map(lambda x: x.upper(), a)
        # Convert the map object to a list and print it
        result = list(b)
        self.assertEqual(result, ["APPLE", "BANANA", "CHERRY"])

    def test_lambda_map_multiply(self):
        a = [1, 2, 3, 4, 5]
        result = list(map(lambda x: x * 3, a))
        print(result)
        self.assertEqual(result, [3, 6, 9, 12, 15])

    def test_lambda_map_and_tuples(self):
        nums = (1, 2, 3)
        result = tuple(map(lambda x: x + 1, nums))
        self.assertEqual(result, (2, 3, 4))

    def test_lambda_reduce_strings(self):
        from functools import reduce
        a = ["Geeks", "for", "Geeks"]
        result = reduce(lambda x, y: x + " " + y, a)
        self.assertEqual(result, "Geeks for Geeks")

    def test_lambda_reduce_integers(self):
        a = [2, 4, 6, 8]
        result = reduce(lambda x, y: x + y, a)
        self.assertEqual(result, 20)

    def test_lambda_reduce_highest(self):
        a = [5, 9, 3, 12, 7]
        result = reduce(lambda x, y: x if x > y else y, a)
        self.assertEqual(result, 12)
