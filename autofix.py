#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Программа для автонастройки дистрибутивов Linux после установки"""
import json
import os
import sys
from pathlib import Path


def get_absolute_file_path(path):
    return f'{Path(__file__).resolve().parent}/{path}'


def logo_dec(func):
    def deco():
        print('Aleksandr Suvorov | myhackband@ya.ru'.center(79, '-'))
        print('Автонастройка дистрибутивов Linux после установки'.center(79, '='))
        print(''.center(79, '-'))
        func()
        print(''.center(79, '='))
        print('Программа завершена'.center(79, '-'))

    return deco


def get_json_file_list() -> dict:
    default_file_list = {n: f'{Path(__file__).resolve().parent}/json_fix/{path}'
                         for n, path in enumerate(os.listdir(f'{Path(__file__).parent.absolute()}/json_fix/'), 1)}
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        my_path = sys.argv[1]
        if Path(my_path).is_file():
            return {1: my_path}
        elif Path(my_path).is_dir():
            return {n: f'{my_path}/{path}' for n, path in enumerate(os.listdir(my_path), 1)}
    else:
        return default_file_list


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
    def data(self):
        return self.__data

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
        print(f'Выполняем: {fix}')
        print(''.center(79, '='))
        os.system(fix)


def pack_man_installer(app_list, command):
    for app in app_list:
        print(f'Выполняем: {command} {app}')
        print(''.center(79, '='))
        os.system(f'{command} {app}')


def edit_configuration_files(fix_obj):
    for file_name, fix in fix_obj.file_fix_dict.items():
        print(f'Редактируем файл: {file_name}'.center(79, '-'))
        print(f'Вносим изменения: {fix}')
        print(''.center(79, '='))
        os.system(f'{fix_obj.file_fixer} {fix} >> {file_name}')


def installer(fix_obj):
    print(f'Выполняем начальные команды'.center(79, '='))
    command_installer(fix_obj.pre_install_list)
    print(f'Выполняем установку используя {fix_obj.pack_man}'.center(79, '='))
    pack_man_installer(fix_obj.pack_man_command_list, fix_obj.pack_man)
    print(f'Выполняем установку используя {fix_obj.pip_man}'.center(79, '='))
    pack_man_installer(fix_obj.pip_command_list, fix_obj.pip_man)
    print(f'Выполняем установку используя {fix_obj.snap_man}'.center(79, '='))
    pack_man_installer(fix_obj.snap_command_list, fix_obj.snap_man)
    print(f'Работаем с файлами'.center(79, '='))
    edit_configuration_files(fix_obj)
    print(f'Выполняем завершающие команды'.center(79, '='))
    command_installer(fix_obj.post_command_list)


@logo_dec
def main():
    json_file_dict = get_json_file_list()
    if json_file_dict:
        while True:
            print('Найдены файлы конфигураций'.center(79, '='))
            for number, value in json_file_dict.items():
                print(f'{number}. {Path(value).name}')
            print(''.center(79, '='))
            user_input = int(input('Введите номер нужного файла конфиграции и нажмите ENTER: '))
            fix_obj = FixObj(json_file_dict[user_input])
            print(''.center(79, '-'))
            print(f'Внимание! Будет применен фикс для {fix_obj.fix_name} из файла: {fix_obj.file_name}')
            print(''.center(79, '-'))
            user_input = input('ENTER для продолжения, 0 + ENTER для возврата к выбору: ')
            if user_input:
                print(''.center(79, '-'))
                continue
            else:
                print('Начинаем работу'.center(79, '='))
                installer(fix_obj=fix_obj)
            break
    else:
        print('Ошибка! Не найдены файлы конфигурации...')


if __name__ == '__main__':
    main()
