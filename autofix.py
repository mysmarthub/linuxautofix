#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Program for auto-tuning Linux distributions after installation"""
import json
import os
import sys
import shutil
from pathlib import Path


COLUMNS, _ = shutil.get_terminal_size()


def get_absolute_file_path(path):
    return f'{Path(__file__).resolve().parent}/{path}'


class FixObj:

    def __init__(self, json_file):
        self.__json_file = json_file
        self.__data = self.__json_data()

    @property
    def fix_name(self):
        return self.__data["options"]["name"]

    @property
    def file_name(self):
        return Path(self.__json_file).name

    def __json_data(self):
        with open(self.__json_file, 'r') as f:
            data = json.load(f)
        return data

    @property
    def pack_man(self):
        return self.__data["options"]["pack_man"]

    @property
    def pip_man(self):
        return self.__data["options"]["pip_man"]

    @property
    def snap_man(self):
        return self.__data["options"]["snap_man"]

    @property
    def file_fixer(self):
        return self.__data["options"]["file_fixer"]

    @property
    def pre_install_list(self):
        return self.__data["pre_install"]

    @property
    def pack_man_command_list(self):
        return self.__data["install"]["pack_man"]

    @property
    def pip_command_list(self):
        return self.__data["install"]["pip_man"]

    @property
    def snap_command_list(self):
        return self.__data["install"]["snap_man"]

    @property
    def file_fix_dict(self):
        return self.__data["file_fix"]

    @property
    def post_command_list(self):
        return self.__data["post_install"]


def make_json_obj_dict(json_list):
    return {n: obj for n, obj in enumerate([FixObj(file) for file in json_list], 1)}


def command_installer(command_list):
    for fix in command_list:
        print(f'\n\nPerformed: {fix}')
        print(''.center(COLUMNS, '='))
        # os.system(fix)


def pack_man_installer(app_list, command):
    for app in app_list:
        print(f'\n\nPerformed: {command} {app}')
        print(''.center(COLUMNS, '='))
        # os.system(f'{command} {app}')


def edit_configuration_files(fix_obj):
    for file_name, fix in fix_obj.file_fix_dict.items():
        print(f'Editing the file: {file_name}'.center(COLUMNS, '-'))
        print(f'Making changes: {fix}')
        print(''.center(COLUMNS, '='))
        # os.system(f'{fix_obj.file_fixer} {fix} >> {file_name}')


def installer(fix_obj):
    msg = 'We carry out the installation using'
    print(f'We execute the initial commands'.center(COLUMNS, '='))
    command_installer(fix_obj.pre_install_list)
    print(f'{msg} {fix_obj.pack_man}'.center(COLUMNS, '='))
    pack_man_installer(fix_obj.pack_man_command_list, fix_obj.pack_man)
    print(f'{msg} {fix_obj.pip_man}'.center(COLUMNS, '='))
    pack_man_installer(fix_obj.pip_command_list, fix_obj.pip_man)
    print(f'{msg} {fix_obj.snap_man}'.center(COLUMNS, '='))
    pack_man_installer(fix_obj.snap_command_list, fix_obj.snap_man)
    print(f'Working with files'.center(COLUMNS, '='))
    edit_configuration_files(fix_obj)
    print(f'Executing the final commands'.center(COLUMNS, '='))
    command_installer(fix_obj.post_command_list)


def get_json_file_dict(json_file_list) -> dict:
    return {n: path for n, path in enumerate(json_file_list, 1)}


def get_json_files(path):
    file_list = []
    for p, _, f in os.walk(path):
        for file in f:
            if Path(file).suffix == '.json':
                file_list.append(os.path.join(p, file))
    return file_list


def get_args():
    file_list = []
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            if Path(path).is_file() and Path(path).suffix == '.json':
                file_list.append(path)
            else:
                file_list.extend(get_json_files(path))
        return file_list
    else:
        return [file for file in get_json_files(f'{Path(__file__).parent.absolute()}/json_fix/')]


def logo_dec(func):
    def deco():
        print('Linux Auto Fix'.center(COLUMNS, '='))
        print('Aleksandr Suvorov | myhackband@ya.ru'.center(COLUMNS, '-'))
        print('Program for auto-tuning Linux distributions after installation'.center(COLUMNS, '='))
        json_file_set = set(get_args())
        json_file_dict = get_json_file_dict(json_file_set)
        func(json_file_dict)
        print(''.center(COLUMNS, '='))
        print('Program completed'.center(COLUMNS, '-'))
    return deco


@logo_dec
def main(json_file_dict):
    if json_file_dict:
        while True:
            print('Configuration files found: ')
            for number, value in json_file_dict.items():
                print(f'{number}. {Path(value).name}')
            print(''.center(COLUMNS, '='))
            user_input = int(input('Enter the desired config file number and press ENTER: '))
            fix_obj = FixObj(json_file_dict[user_input])
            print(''.center(COLUMNS, '-'))
            print(f'Attention! Fix will be applied for {fix_obj.fix_name} from file: {fix_obj.file_name}')
            print(''.center(COLUMNS, '-'))
            user_input = input('ENTER to continue, 0 + ENTER to return to selection: ')
            if user_input:
                print(''.center(COLUMNS, '-'))
                continue
            else:
                print('Getting started'.center(COLUMNS, '='))
                installer(fix_obj=fix_obj)
            break
    else:
        print('Error! No config files found...')


if __name__ == '__main__':
    files = get_args()
    print(files)
    main()
