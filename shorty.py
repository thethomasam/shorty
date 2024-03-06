import click

@click.group()
def cli():
    pass

@cli.command()
def create_project():
    click.echo('Project Created: 123')

@cli.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)


if __name__ == '__main__':
    cli()