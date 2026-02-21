from core.service import BaseServiceError


class ProductNotFound(BaseServiceError):
    """Product not found"""


class NotEnoughBalance(BaseServiceError):
    """Not enough balance"""


class ProductNotAvailable(BaseServiceError):
    """Product not available now, please try later"""


class OutOfStock(BaseServiceError):
    """Product is out of stock now, please try later"""