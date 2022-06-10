
import click
from tabulate import tabulate
from clients.models import Client
from clients.services import ClientService

@click.group()
def clients () -> None:
    """ Manages the Available Clients """
    pass

@clients.command()
@click.option(
        "-n", "--name", type=str,
        prompt=True, help="Client\'s Name"
        )
@click.option(
        "-c", "--company", type=str,
        prompt=True, help="Client Company's Name"
        )
@click.option(
        "-e", "--email", type=str,
        prompt=True, help="Client\'s Email"
        )
@click.option(
        "-p", "--position", type=str,
        prompt=True, help="Client\'s Company Position"
        )
@click.pass_context
def create (ctx, name:str, company:str, email:str, position:str) -> None:
    """ Creates a New Client """
    new_client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(new_client)

@clients.command()
@click.pass_context
def list (ctx) -> None:
    """ Lists the Available Clients """
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    headers = [title.capitalize() for title in Client.schema()]
    table = []

    for client in client_list:
        table.append([*client.values()])

    click.echo(tabulate(table, headers))

@clients.command()
@click.argument("id_client_to_update", type=str)
@click.pass_context
def update (ctx, id_client_to_update:int) -> None:
    """ Changes and Updates a Client, by the given ID """
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    client_to_update = [client for client in client_list if client["idx"] == id_client_to_update]

    if client_to_update:
        client_to_update = _update_client_flow(Client(**client_to_update[0]))
        client_service.update_clients(client_to_update)
        click.echo("Client Found And Updated")
    else:
        click.echo("Client Not Found")

def _update_client_flow (client:Client) -> Client:
    click.echo("Leave Empty If You Don't Want to Modify the Value")

    client.name = click.prompt("New Client\'s Name", type=str, default=client.name)
    client.company = click.prompt("New Client\'s Company", type=str, default=client.company)
    client.email = click.prompt("New Client\'s Email", type=str, default=client.email)
    client.position = click.prompt("New Client Company\'s Position", type=str, default=client.position)

    return client

@clients.command()
@click.argument("id_client_to_delete", type=str)
@click.pass_context
def delete (ctx, id_client_to_delete:int|str) -> None:
    """ Deletes a Client, by the given ID """
    client_service = ClientService(ctx.obj["clients_table"])
    client_list = client_service.list_clients()

    client_to_delete = [client for client in client_list if client["idx"] == id_client_to_delete]

    if client_to_delete and _confirm_action("Do You want to Delete This User (y/n)"):
        client_to_delete = Client(**client_to_delete[0])
        client_service.delete_clients(client_to_delete)
        click.echo("Client Deleted")
    else:
        click.echo("Client Not Found")

def _confirm_action (label:str) -> bool:
    confirmation = click.prompt(label, default="n", confirmation_prompt=True)

    if confirmation.lower()[0] == "y":
        return True

    return False

