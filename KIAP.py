import click
import settings

@click.command()
@click.option('--name', prompt='Enter your name', help='Your name')
# @click.argument('name')
def hello(name):
    click.echo(name)

if __name__ == '__main__':
    if settings.distro_select():
        click.echo(f"Distro {settings.distro_select()}!")
    else:
        hello()

