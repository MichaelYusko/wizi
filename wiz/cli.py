import click

from wiz.generator import WiziGenerator as Wizi


@click.command()
@click.option('-n', '--name', prompt='Name of your project',
              help='Create an project based on name.')
def create(name):
    """Generate an project"""
    wizi = Wizi(name)
    wizi.create_project()
    click.echo('%s was created.' % name)
