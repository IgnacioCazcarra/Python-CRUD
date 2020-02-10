import click
from clients.services import ClientService
from clients.services import Client


@click.group()
def clients():
    """Manages the client life-cylce"""
    pass


@clients.command()
@click.option('-n','--name',type=str,prompt=True,help='The clients name')
@click.option('-c','--company',type=str,prompt=True,help='The clients company')
@click.option('-m','--mail',type=str,prompt=True,help='The clients mail')
@click.option('-a','--age',type=str,prompt=True,help='The clients age')
@click.pass_context
def create(ctx, name, company, mail, age):
    """Creates a new client"""
    client = Client(name,company,mail,age)
    client_service = ClientService(ctx.obj['clients_table'])    
    client_service.create_client(client)

@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()
    
    click.echo('ID   |NAME     |COMPANY     |MAIL     |AGE     ')
    click.echo('*'*100)

    for client in clients_list:
        click.echo('{uid}|{name}|{company}|{mail}|{age}'.format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            mail=client['mail'],
            age = client['age']))

@clients.command()
@click.option('-id','--uid',type=str,prompt=True,help='The clients ID you want to update')
@click.pass_context
def update(ctx, uid):
    """Updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients() 
    updated_client = [client for client in client_list  if client['uid'] == uid]
    
    if updated_client:
        updated_client = _update_client_flow(Client(**updated_client[0]))
        client_service.update_client(updated_client)
    else: click.echo('The client does not exist')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')

    client.name = click.prompt('New name', type=str, default = client.name)
    client.company = click.prompt('New company', type=str, default = client.company)
    client.mail = click.prompt('New mail', type=str, default = client.mail)
    client.age = click.prompt('New age', type=str, default = client.age)
    return client


@clients.command()
@click.option('-id','--uid',type=str,prompt=True,help='The clients ID you want to update')
@click.pass_context
def delete(ctx, uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients() 
    deleted_client = [client for client in client_list if client['uid'] == uid]
    if deleted_client:
        client_service.delete_client(uid)
        click.echo('Client successfully removed')
    else: click.echo('The client does not exist')


all = clients

