class FulfillmentError(Exception):
    pass


class ValidationError(FulfillmentError):
    pass


class UnknownSku(FulfillmentError):
    pass


class OutOfStock(FulfillmentError):
    pass
