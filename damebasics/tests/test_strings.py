#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2021  David Arroyo Menéndez

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
# along with DameBasics; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import unittest
import re
from pprint import pprint


class TddInPythonExample(unittest.TestCase):

    def test_string_check_type_method_returns_correct_result(self):
        doublestr = "str1str2"
        # a string
        self.assertTrue(isinstance(doublestr, str))
        # letters and/or numbers without white spaces
        self.assertTrue(doublestr.isalnum())
        # letters without numbers and without white spaces
        self.assertTrue(not(doublestr.isalpha()))
        # numbers without white spaces
        self.assertTrue(not(doublestr.isdigit()))
        # lower case
        self.assertTrue(doublestr.lower())
        # lower case
        self.assertEqual("Str1str2", doublestr.capitalize())

    def test_string_concat_method_returns_correct_result(self):
        string1 = "str1"
        string2 = "str2"
        self.assertEqual("str1str2", string1 + string2)

    def test_string_sub_method_returns_correct_result(self):
        str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
        strsub = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
        self.assertEqual('purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher', strsub)

    def test_string_search_method_returns_correct_result(self):
        m = re.search(r'^(1[0-2]|[1-9])$', str(9))
        self.assertTrue(m)
        m2 = re.search(r'^(1[0-2]|[1-9])$', str(12))
        self.assertTrue(m2)
        m3 = re.search(r'^(1[0-2]|[1-9])$', str(19))
        self.assertFalse(m3)

    def test_string_search_method_returns_correct_result(self):
        p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
        regex = 'http[s]?://(www.)?([a-z]*\.)*(?P<host>[a-z]*)\.(?P<ext>[a-z]*)?'
        m = re.search(p,'http://www.abc.com:123/test')
        self.assertEqual(m.group('host'), 'www.abc.com') # 'www.abc.com'
        self.assertEqual(m.group('port'), str(123)) # '123'
        m2 = re.search(regex,'http://madrid.elpais.es')
        self.assertEqual(m2.group('host'), 'elpais')
        self.assertEqual(m2.group('ext'), 'es')
