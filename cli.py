import click
import machinecommands as mc


@click.group()
def root():
    pass


@root.group(cls=mc.MachineCommands)
def machine():
    pass


if __name__ == "__main__":
    root()
