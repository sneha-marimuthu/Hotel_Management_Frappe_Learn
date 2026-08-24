import click

@click.command("sample")
def sample():
    click.echo("Sample code")

commands  = [sample]