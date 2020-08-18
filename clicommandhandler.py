import abc
import json
from typing import Any

import click


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
