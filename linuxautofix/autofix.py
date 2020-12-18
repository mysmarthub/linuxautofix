#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Program for auto-tuning Linux distributions after installation"""
import argparse
import inspect
import os
import shutil
import json
from pathlib import Path

COLUMNS, _ = shutil.get_terminal_size()
VERSION = '0.0.5'


def check_path(path):
    if type(path) is str and Path(path).exists() and Path(path).suffix == '.json':
        return True
    return False


def open_json(file):
    with open(file, 'r') as f:
        json_data = json.load(f)
    return json_data


def execute_the_command(command: str):
    if type(command) is str:
        status = os.system(command)
        print(status)
        if not status:
            return True
    return False


def menu(conf_dict):
    print(''.center(COLUMNS, '*'))
    print('Configuration Settings'.center(COLUMNS, '='))
    print(''.center(COLUMNS, '-'))
    for n, val in conf_dict.items():
        print(f'{n}: {val[0]}')
    print(''.center(COLUMNS, '-'))


def get_input():
    while True:
        try:
            user_input = int(input('Enter the command, to exit, enter 0: '))
        except ValueError:
            print('Input Error!')
            continue
        else:
            return user_input


def start(conf_dict):
    while True:
        menu(conf_dict)
        conf_number = get_input()
        if not conf_number:
            print('Getting out...')
            break
        if conf_number not in conf_dict.keys():
            print('Invalid input!!!')
            continue
        fix_name, fix_list = conf_dict[conf_number]
        while True:
            print(f'Selected {fix_name}'.center(COLUMNS, '='))
            print(''.center(COLUMNS, '-'))
            print(f'1 - Start\n'
                  f'2 - Info\n'
                  f'0 - Cancel\n')
            user_input = get_input()
            if user_input == 1:
                for fix in fix_list:
                    print('\n')
                    print(f'Execute: {fix}'.center(COLUMNS, '-'))
                    print(f'[Execute]: {fix}')
                    print(f'Execute: {fix}'.center(COLUMNS, '-'))
                    status = execute_the_command(fix)
                    print(''.center(COLUMNS, '-'))
                    if status:
                        print('Successfully!')
                    else:
                        print('Error! Command not executed!')
            elif user_input == 2:
                for fix in fix_list:
                    print(fix)
            break


def createParser():
    parser = argparse.ArgumentParser(
        description='Program for auto-tuning Linux distributions after installation',
        prog=f'Linux Auto Fix v{VERSION}',
        epilog="""The configuration file must be a file in the format 
        .json and have the correct settings""",
    )
    parser.add_argument('path', nargs='?', help='Путь к файлу с настройками', default=False)
    parser.add_argument('--version',
                        action='version',
                        help='Program version',
                        version='%(prog)s {}'.format(VERSION))
    return parser


def logo(func):
    parser = createParser()
    namespace = parser.parse_args()
    print(namespace)
    if namespace.path:
        path = namespace.path
    else:
        filename = inspect.getframeinfo(inspect.currentframe()).filename
        path = os.path.dirname(os.path.abspath(filename))
        path = f'{path}/config.json'

    def deco():
        print(''.center(COLUMNS, '*'))
        print('Linux Auto Fix'.center(COLUMNS, '='))
        print('Aleksandr Suvorov | myhackband@ya.ru'.center(COLUMNS, '-'))
        print('Program for auto-tuning Linux distributions after installation'.center(COLUMNS, '='))
        if path:
            func(path)
        else:
            parser.print_help()
        print(''.center(COLUMNS, '='))
        print('Program completed'.center(COLUMNS, '-'))
    return deco


@logo
def main(path):
    if check_path(path):
        try:
            config = open_json(path)
        except json.decoder.JSONDecodeError as err:
            print(''.center(COLUMNS, '-'))
            print('Error in the configuration file!!!')
            print(f'Error: {err}')
        else:
            config_dict = {n: name for n, name in enumerate(config.items(), 1)}
            if config_dict:
                start(config_dict)
            else:
                print('Settings not found!')
    else:
        print('Error! The path does not exist!')


if __name__ == '__main__':
    main()
