import click

CONTEXT_SETTINGS = dict(help_option_names=["--help", "-h"])


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """
    Ensure SSH directories and files have correct permissions:

    \b
    $HOME/.ssh          -> 700
    authorized_keys     -> 644
    known_hosts         -> 644
    config              -> 644
    *.pub keys          -> 644
    All private keys    -> 600
    """
    pass


@main.command()
def check():
    import os

    ssh_dir = os.path.expanduser("~/.ssh")
    files = [ssh_dir] + os.listdir(ssh_dir)

    for file in files:
        file_stat = os.stat(os.path.join(ssh_dir, file))
        permissions = oct(file_stat.st_mode)
        click.echo(f"{permissions[-3:]} ->  {file}")


if __name__ == "__main__":
    main()
