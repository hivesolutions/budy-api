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


class VoucherAPI(object):

    def list_vouchers(self, *args, **kwargs):
        url = self.base_url + "vouchers"
        contents = self.get(url, **kwargs)
        return contents

    def get_voucher(self, key):
        url = self.base_url + "vouchers/" + key
        contents = self.get(url)
        return contents

    def create_value_voucher(
        self,
        amount,
        key=None,
        currency=None,
        usage_limit=0,
        unlimited=False,
        start=None,
        expiration=None,
        meta=None,
    ):
        url = self.base_url + "vouchers/value"
        data_j = dict(
            amount=amount,
            key=key,
            currency=currency,
            usage_limit=usage_limit,
            unlimited=unlimited,
            start=start,
            expiration=expiration,
        )
        if not meta == None:
            data_j["meta"] = meta
        contents = self.post(
            url,
            data_j=data_j,
        )
        return contents

    def create_percentage_voucher(
        self,
        percentage,
        key=None,
        usage_limit=0,
        unlimited=False,
        start=None,
        expiration=None,
        meta=None,
    ):
        url = self.base_url + "vouchers/percentage"
        data_j = dict(
            percentage=percentage,
            key=key,
            usage_limit=usage_limit,
            unlimited=unlimited,
            start=start,
            expiration=expiration,
        )
        if not meta == None:
            data_j["meta"] = meta
        contents = self.post(
            url,
            data_j=data_j,
        )
        return contents

    def use_voucher(
        self, key, amount=None, currency=None, justification=None, save_use=True
    ):
        url = self.base_url + "vouchers/" + key + "/use"
        data_j = dict(
            amount=amount,
            currency=currency,
            justification=justification,
            save_use=save_use,
        )
        contents = self.post(url, data_j=data_j)
        return contents

    def disuse_voucher(self, key):
        url = self.base_url + "vouchers/" + key + "/disuse"
        contents = self.post(url)
        return contents
