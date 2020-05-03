
from enum import Enum


# Str enum which also return field value, instead of "<Enum.field: value>"
class StrEnum(str, Enum):
    def __get__(self, instance, owner):
        return self.value


class CashPayment(StrEnum):
    cash = 'cash'


class NonCashPayment(StrEnum):
    non_cash = 'non_cash'


class PaymentTypes(StrEnum):
    cash = CashPayment.cash
    non_cash = NonCashPayment.non_cash


class PaymentOperation(StrEnum):
    payment = 'payment'


class CancelOperation(StrEnum):
    cancel = 'cancel'


class OperationTypes(StrEnum):
    payment = PaymentOperation.payment
    cancel = CancelOperation.cancel


class OrderStatuses(StrEnum):
    ordered = 'ordered'
    payed = 'payed'
    in_process = 'in_process'
    part_ready = 'part_ready'
    order_ready = 'order_ready'
    to_client = 'to_client'
    ready_cashier = 'ready_cashier'
    canceled = 'canceled'


class OrderedProductStatuses(StrEnum):
    ordered = 'ordered'
    payed = 'payed'
    in_process = 'in_process'
    ready = 'ready'
    to_client = 'to_client'


class CookRoles(StrEnum):
    sushi = 'sushi'
    steak = 'steak'
    onCashier = 'onCashier'


class UserRoles(StrEnum):
    pass
