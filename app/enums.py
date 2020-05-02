
from enum import Enum


# Str enum which also return field value, instead of "<Enum.field: value>"
class StrEnum(str, Enum):
    def __get__(self, instance, owner):
        return self.value


# # # # Payment Types # # # #

class CashPayment(str, Enum):
    cash = 'cash'

    def __get__(self, instance, owner):
        return self.value


class NonCashPayment(str, Enum):
    non_cash = 'non_cash'

    def __get__(self, instance, owner):
        return self.value


class PaymentTypes(StrEnum):
    cash = CashPayment.cash
    non_cash = NonCashPayment.non_cash

    # def __get__(self, instance, owner):
    #     return self.value


# # # # Operation Types # # # #

class PaymentOperation(str, Enum):
    payment = 'payment'

    def __get__(self, instance, owner):
        return self.value


class CancelOperation(str, Enum):
    cancel = 'cancel'

    def __get__(self, instance, owner):
        return self.value


class OperationTypes(str, Enum):
    payment = PaymentOperation.payment
    cancel = CancelOperation.cancel

    def __get__(self, instance, owner):
        return self.value


# # # # Order statuses # # # #


class OrderStatuses(StrEnum):
    ordered = 'ordered'
    payed = 'payed'
    in_process = 'in_process'
    part_ready = 'part_ready'
    order_ready = 'order_ready'
    to_client = 'to_client'
    ready_cashier = 'ready_cashier'
    canceled = 'canceled'

#     ordered
#     payed
#     in_process
#     part_ready
#     order_ready
#     to_client
#     ready_cashier
#     canceled
