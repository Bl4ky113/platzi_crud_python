#!/bin/python3

import click

from clients import commands as client_commands

@click.group()
@click.pass_context
def cli (ctx):
    ctx.obj = {}

cli.add_command(client_commands.clients)
