#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details)
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""
Console utility for automatic command execution

and auto-tuning Linux distributions after installation.

Store commands for different tasks or systems in one
place and execute them automatically.
"""
import inspect
import json
import os
import shutil

import click

TITLE = 'Linux Auto Fix'
VERSION = '1.0.2'
AUTHOR = 'Aleksandr Suvorov'
DESCRIPTION = 'CLI utility for automatic command execution, ' \
              'and auto-tuning Linux distributions after installation'
URL = 'https://github.com/mysmarthub'
YANDEX = 'https://yoomoney.ru/to/4100115206129186'
PAYPAL = 'https://paypal.me/myhackband'
COPYRIGHT = 'Copyright © 2020-2021 Aleksandr Suvorov'


class Pack:
    def __init__(self, name, command_list):
        self.name = name
        self.command_list = command_list

    @property
    def count(self):
        return len(self.command_list)


def executor(command: str, test: bool = False) -> bool:
    """
    Executes the command

    :param command: <str> Command to execute
    :param test: <bool> Used for testing. True disables the actual execution of commands.
    :return: <bool> Logical status of command execution
    """
    if not test:
        if type(command) is str:
            status = os.system(command)
            if status:
                return False
    return True


def open_file(file):
    """
    Open the settings file in json format.

    :param file: <str> Path to the file in json format with command packages
    :return: <dict> Dictionary with command packages, where the key is the name of the package,
    and the value is a list of commands. If an error occurs, it returns an empty dictionary.
    """
    try:
        with open(file, 'r') as f:
            json_data = json.load(f)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return {}
    else:
        return json_data


def smart_print(text='', char='-'):
    if not char:
        char = ' '
    columns, _ = shutil.get_terminal_size()
    if text:
        click.echo(f' {text} '.center(columns, char))
    else:
        click.echo(f''.center(columns, char))


def start_logo():
    smart_print('', '*')
    smart_print(f'{TITLE} v{VERSION} | Author: {AUTHOR}', '=')
    smart_print(f'CLI utility for auto-tuning Linux distributions after installation.', '-')
    smart_print()


def end_logo():
    smart_print(f'{YANDEX}', '-')
    smart_print(f'{PAYPAL}', '-')
    smart_print(f'{COPYRIGHT}', '=')
    smart_print('Program completed', '*')


def get_pack_name(pack_objects: dict):
    num_pack = {n: name for n, name in enumerate(pack_objects.keys(), 1)}
    while 1:
        """Shows a simple menu."""
        smart_print('Command packages:')
        for n, name in num_pack.items():
            click.echo(f'{n}. {name} | Commands[{pack_objects[name].count}]')
        smart_print()
        num = click.prompt(text='Enter the package number and click Enter', type=int)
        if num not in num_pack:
            smart_print()
            click.echo('Input Error!')
            continue
        pack_name = num_pack[num]
        command_list = pack_objects[pack_name].command_list
        while 1:
            smart_print()
            click.echo(f'The selected package {num_pack[num]} | '
                       f'Commands:[{pack_objects[pack_name].count}]')
            smart_print()
            click.echo('1. Start')
            click.echo('2. Show commands')
            click.echo('3. Cancel')
            smart_print()
            user_input = click.prompt(text='Enter the desired number and press ENTER', type=int)
            smart_print()
            if user_input not in (1, 2, 3):
                click.echo('Input Error!')
            elif user_input == 1:
                return pack_name
            elif user_input == 2:
                click.echo()
                click.echo(f'{pack_name} commands: ')
                for command in command_list:
                    click.echo(command)
                continue
            break


def start(pack_obj, test=False):
    count = 0
    errors = []
    click.echo()
    click.echo(f'Pack name: [{pack_obj.name}]')
    smart_print()
    for command in pack_obj.command_list:
        count += 1
        click.echo()
        msg = f'[execute {count}]: {command}'
        click.echo(msg)
        status = executor(command, test=test)
        if status:
            click.echo('[Successfully]')
        else:
            errors.append(f'Error: {msg}')
            click.echo('[Error]')
        smart_print()
    smart_print('', '=')
    click.echo(f'The command package [{pack_obj.name}] is executed.')
    click.echo(f'Commands completed: [{count - len(errors)}] | Errors: [{len(errors)}]')


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'{TITLE} {VERSION} - {COPYRIGHT}')
    ctx.exit()


@click.command()
@click.option('--file', '-f', help='The path to the file with the command packs', type=click.Path(exists=True))
@click.option('--default', '-d', is_flag=True, help='Run an additional batch of commands from default')
@click.option('--test', '-t', is_flag=True, help='Test run, commands will not be executed.')
@click.option('--name', '-n', help='Name of the package to run automatically')
@click.option('--version', '-v', is_flag=True, callback=print_version,
              help='Displays the version of the program and exits.',
              expose_value=False, is_eager=True)
def cli(file, default, name, test):
    """Linux Auto Fix - CLI utility for automatic command execution

    and auto-tuning Linux distributions after installation.

    - To work, the utility uses files that store named command packages,
        where the name is the name of the command package,
        and the value is a list of commands.

    - You can create your own files with command packages using
        default structure.

    - Use the name "default" for the package with the default commands.
        You can run them in addition to the selected batch of commands.

    - You can pass the file name as an argument
        or use the default file, it should be located
        in the same directory as the file being run.

    - The console version allows you to run the script in the terminal,
        passing it a file with the settings as an argument,
        or use the default file. In the process of working,
        you choose the right one command package,
        after which you can start executing, display a list
        of commands for this package,
        or go back to selecting the command package.

    - Using the -n or --name parameter, you can specify the name
        of the command package at startup,
        then the utility will immediately start automatic execution
        of commands from this package.

    - Examples of implementation:

    python linuxautofix.py --file=config.json -d

    python linuxautofix.py --file=config.json-d --name=Ubuntu

    or

    linuxautofix --file=config.json -d

    linuxautofix --file=config.json-d --name=Ubuntu

    """
    start_logo()
    if os.path.exists(str(file)) and os.path.isfile(file):
        file = file
    else:
        click.echo('The path is not found, we are looking for the default file...')
        filename = inspect.getframeinfo(inspect.currentframe()).filename
        folder = os.path.dirname(os.path.abspath(filename))
        file = os.path.join(folder, 'config.json')
    if file:
        pack_dict = open_file(file)
        pack_objects = {key: Pack(name=key, command_list=val) for key, val in pack_dict.items()}
        if pack_dict:
            if name and name in pack_dict:
                pack_name = name
            else:
                if name:
                    click.echo('Name not found...')
                pack_name = get_pack_name(pack_objects)
            pack_obj = Pack(pack_name, pack_dict[pack_name])
            start(pack_obj, test=test)
            if default and 'default' in pack_dict and pack_name != 'default':
                pack_obj = Pack(name='default', command_list=pack_dict['default'])
                start(pack_obj=pack_obj, test=test)
        else:
            click.echo('No data available... There may be an error in the configuration file')
    else:
        click.echo('Failed to load settings... There may be an error in the configuration file')
    end_logo()


if __name__ == '__main__':
    cli()
