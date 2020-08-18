from typing import Any

import os
import platform

from clicommandhandler import CliCommandHandler
from clicommands import CliCommands


class MachineCommands(CliCommands):
    def on_list_commands(self, ctx):
        return ["show"]

    def on_get_command(self, ctx, cmd_name):
        if cmd_name == "show":
            return MachineCommandHandler(name="show")


class MachineCommandHandler(CliCommandHandler):
    def on_invoke(self, ctx) -> Any:
        return dict(
            name=platform.node(),
            processor=platform.processor(),
            cpu_count=os.cpu_count(),
        )
