class PaymentError(Exception):
    pass


class ValidationError(PaymentError):
    pass


class UnknownAccount(PaymentError):
    pass


class InsufficientFunds(PaymentError):
    pass
