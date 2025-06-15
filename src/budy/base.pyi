from typing import Any, Dict

import appier
from . import account as account
from . import address as address
from . import bag as bag
from . import brand as brand
from . import category as category
from . import collection as collection
from . import color as color
from . import country as country
from . import order as order
from . import product as product
from . import referral as referral
from . import season as season
from . import section as section
from . import store as store
from . import subscription as subscription
from . import voucher as voucher

BASE_URL: str

class API(
    appier.API,
    bag.BagAPI,
    color.ColorAPI,
    order.OrderAPI,
    brand.BrandAPI,
    store.StoreAPI,
    season.SeasonAPI,
    account.AccountAPI,
    address.AddressAPI,
    country.CountryAPI,
    product.ProductAPI,
    section.SectionAPI,
    voucher.VoucherAPI,
    category.CategoryAPI,
    referral.ReferralAPI,
    collection.CollectionAPI,
    subscription.SubscriptionAPI,
):
    base_url: str
    country: str
    currency: str
    username: str | None
    password: str | None
    session_id: str | None
    tokens: Any | None
    def __init__(self, *args, **kwargs) -> None: ...
    def build(
        self,
        method: str,
        url: str,
        data: Any | None = None,
        data_j: Any | None = None,
        data_m: Any | None = None,
        headers: Dict[str, Any] | None = None,
        params: Dict[str, Any] | None = None,
        mime: str | None = None,
        kwargs: Dict[str, Any] | None = None,
    ) -> None: ...
    def get_session_id(self) -> str | None: ...
    def auth_callback(
        self, params: Dict[str, Any], headers: Dict[str, Any]
    ) -> None: ...
    def login(
        self, username: str | None = None, password: str | None = None
    ) -> str | None: ...
    def is_auth(self) -> bool: ...
