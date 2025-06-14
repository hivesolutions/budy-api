from typing import Any

class VoucherAPI:
    def list_vouchers(self, *args: Any, **kwargs: Any) -> Any: ...
    def create_value_voucher(
        self,
        amount: float,
        key: str | None = None,
        currency: str | None = None,
        unlimited: bool = False,
    ) -> Any: ...
    def create_percentage_voucher(
        self,
        percentage: float,
        key: str | None = None,
    ) -> Any: ...
