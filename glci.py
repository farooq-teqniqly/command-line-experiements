import click
import glob

CONTEXT_SETTINGS = dict(help_option_names=["--help", "-h"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--path",
    prompt="Path to search for files:",
    help="This is the path to search for files: /tmp",
)
@click.option(
    "--ftype",
    prompt="Search for only this file type:",
    help="Specify the file type: csv",
)
def search(path: str, ftype: str):
    results = glob.glob(f"{path}/*.{ftype}")
    click.echo(click.style("Found matches:", fg="green"))

    for result in results:
        click.echo(click.style(f"{result}", fg="blue"))


if __name__ == "__main__":
    search()
