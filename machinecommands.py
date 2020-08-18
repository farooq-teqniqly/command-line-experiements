import abc
import click
import json
import os
import platform


class CliCommands(click.MultiCommand, abc.ABC):
    @abc.abstractmethod
    def list_commands(self, ctx):
        pass

    @abc.abstractmethod
    def get_command(self, ctx, cmd_name):
        pass


class CliCommandHandler(click.Command, abc.ABC):
    def __init__(self, name):
        super(CliCommandHandler, self).__init__(
            name=name, params=[click.Option(["-o", "--output"])]
        )

    @abc.abstractmethod
    def invoke(self, ctx):
        pass

    def _on_output(self, ctx, output):
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


class MachineCommands(CliCommands):
    def list_commands(self, ctx):
        return ["show"]

    def get_command(self, ctx, cmd_name):
        if cmd_name == "show":
            return MachineCommandHandler(name="show")


class MachineCommandHandler(CliCommandHandler):
    def invoke(self, ctx):
        output = dict(
            name=platform.node(),
            processor=platform.processor(),
            cpu_count=os.cpu_count(),
        )

        super(MachineCommandHandler, self)._on_output(ctx, output)
