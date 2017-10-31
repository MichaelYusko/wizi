"""Main file for command line"""

import click


@click.command()
@click.option('-n', '--name', prompt='Name of your project',
              help='Create an project based on name.')
def create(name):
    """Generate an project"""
    click.echo('%s was created.' % name)


if __name__ == '__main__':
    create()
