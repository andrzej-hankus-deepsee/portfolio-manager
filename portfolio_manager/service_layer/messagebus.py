from typing import Union

from portfolio_manager.domain import commands, events
from portfolio_manager.domain.commands import Command
from portfolio_manager.domain.events import Event

Message = Union[commands.Command, events.Event]


class MessageBus:

    def __init__(self):
        self.queue = []

    def handle(self, message: Message):
        self.queue.append(message)
        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, events.Event):
                self.queue.extend(self.handle_event(message))
            elif isinstance(message, commands.Command):
                self.queue.extend(self.handle_command(message))
            else:
                raise Exception(f"{message} was not an Event or Command")

    def handle_event(self, message: Event) -> list[Message]:
        pass

    def handle_command(self, message: Command) -> list[Message]:
        pass
