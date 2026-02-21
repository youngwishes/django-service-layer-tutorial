from dataclasses import dataclass
from apps.customer.models import Customer
from apps.product.exceptions import ProductNotFound, NotEnoughBalance, ProductNotAvailable, OutOfStock
from apps.product.models import Product
from apps.product.services.dtos import BuyProductIn
from config.container import container


@dataclass(kw_only=True, slots=True, frozen=True)
class BuyProductService:
    product_in: BuyProductIn

    def __call__(self, *, customer: Customer) -> int:
        product = Product.objects.filter(pk=self.product_in.product_id).first()
        if product is None:
            raise ProductNotFound(
                product=dict(id=self.product_in.product_id, quantity=self.product_in.quantity),
            )
        if self.product_in.quantity > customer.can_buy_max_count_of(product):
            raise NotEnoughBalance(
                product=dict(id=self.product_in.product_id, quantity=self.product_in.quantity),
            )
        if not product.is_available:
            raise ProductNotAvailable(
                product=dict(id=self.product_in.product_id, quantity=self.product_in.quantity),
            )
        if self.product_in.quantity > product.count:
            raise OutOfStock(
                product=dict(id=self.product_in.product_id, quantity=self.product_in.quantity),
            )

        return self._buy(
            product=product,
            customer=customer,
        )

    def _buy(self, *, product: Product, customer: Customer) -> int:
        product.count -= self.product_in.quantity
        product.save(update_fields=["count"])

        customer.balance -= self.product_in.quantity * product.price
        customer.save(update_fields=["balance"])

        return product.pk


def buy_product_service_factory(data: dict) -> BuyProductService:
    return BuyProductService(product_in=BuyProductIn(**data))


container.register("BuyProductService", factory=buy_product_service_factory)
