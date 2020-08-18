import abc
from typing import Any, List

import click
import json
import os
import platform


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


class CliCommandHandler(click.Command, abc.ABC):
    def __init__(self, name):
        super(CliCommandHandler, self).__init__(
            name=name, params=[click.Option(["-o", "--output"])]
        )

    @classmethod
    def _on_output(cls, ctx, output):
        if ctx.params["output"]:
            output_type = str(ctx.params["output"])

            if output_type.lower() == "json":
                click.echo(json.dumps(output, indent=4))
            elif output_type.lower() == "tsv":
                click.echo("\t".join(str(v) for v in output.values()))
            else:
                raise click.UsageError(
                    "Valid values for the output parameter are 'json' and 'tsv'."
                )
        else:
            click.echo("\t".join(str(v) for v in output.values()))

    @abc.abstractmethod
    def on_invoke(self, ctx) -> Any:
        pass

    def invoke(self, ctx):
        output = self.on_invoke(ctx)
        self._on_output(ctx, output)


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
