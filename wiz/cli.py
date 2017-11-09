import click

from wiz.generator import WiziGenerator as Wizi


@click.command()
@click.option('-n', '--name', prompt='Enter project name',
              help='Create an project based on name.')
@click.option('-a', '--author', prompt='Enter author name',
              help='An author name')
@click.option('-lt', '--license_type', prompt='Type of license [MIT, BSD]',
              help='Type of license')
def create(name, author, license_type):
    """Generate an project"""
    wizi = Wizi(name)
    wizi.create_project(license_type=license_type, author_name=author)
    click.echo('%s was created.' % name)
