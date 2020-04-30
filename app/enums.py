from enum import Enum


class OrderStatuses(str, Enum):
    ordered = 'ordered'
    payed = 'payed'
    in_process = 'in_process'
    part_ready = 'part_ready'
    order_ready = 'order_ready'
    to_client = 'to_client'
    ready_cashier = 'ready_cashier'
    canceled = 'canceled'


class PaymentTypes(str, Enum):
    cash = 'cash'
    non_cash = 'non_cash'


class OperationTypePayment(str, Enum):
    payment = 'payment'


class OperationTypeCanceling(str, Enum):
    canceling = 'canceling'


class OperationTypes(str, Enum):
    payment = OperationTypePayment.payment.value
    canceling = OperationTypeCanceling.canceling.value

