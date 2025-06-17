from typing import Any, Sequence

from .base import Base

class Voucher(Base):
    key: str
    amount: float
    currency: str
    usage_limit: int
    unlimited: bool
    start: int
    expiration: int
    meta: dict[str, Any]

class VoucherAPI:
    def list_vouchers(self, *args: Any, **kwargs: Any) -> Sequence[Voucher]: ...
    def get_voucher(self, key: str) -> Voucher: ...
    def create_value_voucher(
        self,
        amount: float,
        key: str | None = None,
        currency: str | None = None,
        usage_limit: int = 0,
        unlimited: bool = False,
        start: Any = None,
        expiration: Any = None,
        meta: Any = None,
    ) -> Voucher: ...
    def create_percentage_voucher(
        self,
        percentage: float,
        key: str | None = None,
        usage_limit: int = 0,
        unlimited: bool = False,
        start: Any = None,
        expiration: Any = None,
        meta: Any = None,
    ) -> Voucher: ...
    def use_voucher(
        self,
        key: str,
        amount: float | None = None,
        currency: str | None = None,
        justification: str | None = None,
        save_use: bool = True,
    ) -> Voucher: ...
    def disuse_voucher(self, key: str) -> Voucher: ...
