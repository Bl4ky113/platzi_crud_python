
import click

@click.group()
def clients () -> None:
    """ Manages the Available Clients """
    pass

@clients.command()
@click.pass_context
def create (ctx, name:str, company:str, email:str, position:str) -> None:
    """ Creates a New Client """
    pass

@clients.command()
@click.pass_context
def list (ctx) -> None:
    """ Lists the Available Clients """
    pass

@clients.command()
@click.pass_context
def update (ctx, client_id) -> None:
    """ Changes and Updates a Client, by the given ID """
    pass

@clients.command()
@click.pass_context
def delete (ctx, client_id) -> None:
    """ Deletes a Client, by the given ID """
    pass
