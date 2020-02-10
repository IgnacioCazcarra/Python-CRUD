import click
import os
from clients import commands as clients_commands

CLIENTS_TABLE = 'clients.csv'
@click.group()
@click.pass_context
def cli(ctx):
    if not os.path.exists(CLIENTS_TABLE):
        with open(CLIENTS_TABLE,mode='w'):
            pass
    ctx.obj={}
    ctx.obj['clients_table']=CLIENTS_TABLE

cli.add_command(clients_commands.all)
