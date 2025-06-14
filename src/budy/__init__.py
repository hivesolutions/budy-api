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

__copyright__ = "Copyright (c) 2008-2025 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

from . import account
from . import address
from . import bag
from . import base
from . import brand
from . import category
from . import collection
from . import color
from . import country
from . import order
from . import product
from . import referral
from . import season
from . import section
from . import store
from . import subscription
from . import voucher

from .account import AccountAPI
from .address import AddressAPI
from .bag import BagAPI
from .base import API
from .brand import BrandAPI
from .category import CategoryAPI
from .collection import CollectionAPI
from .color import ColorAPI
from .country import CountryAPI
from .order import OrderAPI
from .product import ProductAPI
from .referral import ReferralAPI
from .season import SeasonAPI
from .section import SectionAPI
from .store import StoreAPI
from .subscription import SubscriptionAPI
from .voucher import VoucherAPI
