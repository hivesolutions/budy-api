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

import appier

from . import base


class BudyApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(self, name="budy", *args, **kwargs)

    @appier.route("/", "GET")
    def index(self):
        return self.products()

    @appier.route("/products", "GET")
    def products(self):
        api = self.get_api()
        products = api.list_products()
        return products

    @appier.route("/bags", "GET")
    def bags(self):
        api = self.get_api()
        bags = api.list_bags()
        return bags

    def get_api(self):
        return base.get_api()


if __name__ == "__main__":
    app = BudyApp()
    app.serve()
else:
    __path__ = []
