import abc
from typing import List, Any

import click


class CliCommands(click.MultiCommand, abc.ABC):
    def list_commands(self, ctx) -> List[Any]:
        return self.on_list_commands(ctx)

    def get_command(self, ctx, cmd_name):
        return self.on_get_command(ctx, cmd_name)

    @abc.abstractmethod
    def on_list_commands(self, ctx):
        pass

    @abc.abstractmethod
    def on_get_command(self, ctx, cmd_name):
        pass
