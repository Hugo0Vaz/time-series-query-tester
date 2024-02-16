import click

@click.command()
@click.option()
def run_query():


@click.group()
def cli():
    pass

if __name__ == '__main__':
    exit(cli())
