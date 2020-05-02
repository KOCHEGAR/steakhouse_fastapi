from app.enums import StrEnum, OrderStatuses


class AllowedStatusesToCreateOrder(StrEnum):
    ordered = OrderStatuses.ordered
    payed = OrderStatuses.payed


class AllowedStatusesToUpdateOrder(StrEnum):
    in_process = OrderStatuses.in_process
    part_ready = OrderStatuses.part_ready
    order_ready = OrderStatuses.order_ready
    to_client = OrderStatuses.to_client
    ready_cashier = OrderStatuses.ready_cashier
    canceled = OrderStatuses.canceled
