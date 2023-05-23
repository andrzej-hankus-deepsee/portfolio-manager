from functools import cached_property

from portfolio_manager.service_layer.messagebus import MessageBus


class Bootstrap:

    @cached_property
    def message_bus(self) -> MessageBus:
        return MessageBus()


def get_bootstrap():
    return Bootstrap()
