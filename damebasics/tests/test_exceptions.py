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

import math
import unittest
import collections
collections.Callable = collections.abc.Callable


class TddInPythonExample(unittest.TestCase):

    def test_exceptions_name_error(self):
        try:
            str0 = x
        except NameError:
            str0 = "Variable x is not defined"
        except:
            str0 = "Something was wrong"
        self.assertEqual(str0, "Variable x is not defined")

    def test_exceptions_finally(self):
        try:
            str0 = x
        except:
            str0 = "Something went wrong"
        finally:
            str0 = "The 'try except' is finished"
        self.assertEqual(str0, "The 'try except' is finished")

    def test_exceptions_value_error(self):
        value = 25.0
        if value < 0:
            raise ValueError("Cannot calculate the square root of a negative number")
        else:
            res = math.sqrt(value)
        self.assertEqual(res, 5.0)

    def test_exceptions_divide_numbers(self):
        numerator = 10
        denominator = 5
        if denominator == 0:
            raise ZeroDivisionError("Cannot calculate the division of a zero number")
        else:
            result = (numerator / denominator)
            self.assertEqual(result, 2)
