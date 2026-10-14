#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Budy API
# Copyright (c) 2008-2025 Hive Solutions Lda.
#
# This file is part of Hive Budy API.
#
# Hive Budy API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Budy API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Budy API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2025 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import unittest

import budy


class OrderAPITest(unittest.TestCase):

    def test_set_gift_slip_order(self):
        calls = []

        def put(url, **kwargs):
            calls.append((url, kwargs))
            return dict(gift_slip=kwargs["data_j"]["gift_slip"])

        api = budy.API(base_url="http://localhost/api/")
        api.put = put

        result = api.set_gift_slip_order("key", dict(gift_slip=True))

        self.assertEqual(result, dict(gift_slip=True))
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][0], "http://localhost/api/orders/key/gift_slip")
        self.assertEqual(calls[0][1], dict(data_j=dict(gift_slip=True)))

        result = api.set_gift_slip_order("other", dict(gift_slip=False))

        self.assertEqual(result, dict(gift_slip=False))
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[1][0], "http://localhost/api/orders/other/gift_slip")
        self.assertEqual(calls[1][1], dict(data_j=dict(gift_slip=False)))
