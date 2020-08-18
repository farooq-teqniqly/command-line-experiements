import click
import json
import os
import platform


class MachineCommands(click.MultiCommand):
    def list_commands(self, ctx):
        return ["show"]

    def get_command(self, ctx, cmd_name):
        if cmd_name == "show":
            return MachineCommandHandler(name="show", params=[click.Option(["-o", "--output"])])


class MachineCommandHandler(click.Command):
    def invoke(self, ctx):
        output = dict(
            name=platform.node(),
            processor=platform.processor(),
            cpu_count=os.cpu_count(),
        )

        if ctx.params["output"]:
            output_type = str(ctx.params["output"])

            if output_type.lower() == "json":
                click.echo(json.dumps(output, indent=4))
            elif output_type.lower() == "tsv":
                click.echo("\t".join(str(v) for v in output.values()))
        else:
            click.echo("\t".join(str(v) for v in output.values()))
