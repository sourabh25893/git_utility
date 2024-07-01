import subprocess

import click
import os


@click.group()
def cli():
    pass

@click.command()
@click.option("-d", "--directory", default=".", type=str, help="Target path get git branch of")
def get_branches(directory):
    os.chdir(directory)
    result = subprocess.run(["git", "branch"], capture_output=True, text=True)
    print(result.stdout)

@click.command()
@click.option("-d", "--directory", default=".", type=str, help="Target path get git status of")
def get_status(directory):
    os.chdir(directory)
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(result.stdout)


cli.add_command(get_status)
cli.add_command(get_branches)


if __name__ == '__main__':
    cli()

