Linux Auto Fix
===
---
    Created: Aleksandr Suvorov
---
[![PyPI](https://img.shields.io/pypi/v/linuxautofix)](https://pypi.org/project/linuxautofix) 
![PyPI - Downloads](https://img.shields.io/pypi/dm/linuxautofix) 
![GitHub](https://img.shields.io/github/license/mysmarthub/linuxautofix)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/linuxautofix)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/linuxautofix)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mysmarthub/linuxautofix)
>Console utility for auto-configuration of Linux distributions after installation
---

Description
---

>With this utility, you can automate
the execution of commands on a Linux system.
Create a settings file with the necessary items,
in each item, collect the necessary commands,
and start their automatic execution when necessary.

>With this utility, it is very convenient 
to perform routine tasks , as well as configure 
and install the system after installation.

>The settings file is very simple and clear, 
and all the commands you need for different 
cases or different systems will be stored in one place.

>You can create your own files with settings 
or edit the default settings file, 
just specify the path to your file when running the script.

>After starting, the program will prompt you to 
select the desired item, and then execute all the 
commands that are stored in the file with the 
settings under this name.

---

Help:
----

```
usage: Linux Auto Fix v0.0.5 [-h] [--version] [path]

Program for auto-tuning Linux distributions after installation

positional arguments:
  path        Путь к файлу с настройками

optional arguments:
  -h, --help  show this help message and exit
  --version   Program version

The configuration file must be a file in the 
format .json and have the correct settings

```

---

Installation and launch:
---
    You can install the utility using pip:

`pip install linuxautofix`

`sudo pip install linuxautofix`

    And then run it like this:

`linuxautofix`

`linuxautofix /path to the settings file/config.json`

>On some systems, some commands require administrator rights, 
> so you can install the utility and run it further using:

`sudo pip install linuxautofix`

`sudo linuxautofix /path to the settings file/config.json`

>You can download the source files and run them using Python:

```
git clone https://github.com/mysmarthub/linuxautofix.git
python linuxautofix/linuxautofix/autofix.py /path to the settings file/config.json
 
 or

sudo python linuxautofix/linuxautofix/autofix.py /path to the settings file/config.json
```
---

Disclaimer
---

> Attention!
> Be very careful with the commands you pass to the program.
> The author of the program does not bear any responsibility for your actions, but
> provides only an automated shell for executing commands on your system.

---
[GitHub](https://github.com/mysmarthub/linuxautofix) / [PyPi](https://pypi.org/project/linuxautofix/)
---


>When creating your own files, use
the structure from the default file.

```json
{
  "Name to be displayed in the list of commands": [
    "command one",
    "command two"
  ],
  "Next name": [
    "command one",
    "command two"
  ]
}
```


info:
---
    Copyright © 2020 Aleksandr Suvorov
    Licensed under the terms of the MIT License
---

Support:
---
    Created: Aleksandr Suvorov
    Email: myhackband@yandex.ru

---

Help the project financially:
---
>Yandex Money:
https://money.yandex.ru/to/4100110928527458

>Sberbank Russia:
4276 4417 5763 7686
    