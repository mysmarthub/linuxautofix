Linux Auto Fix
===
    
>Console utility for automatic command execution,
and auto-tuning Linux distributions after installation
    

>Created: Aleksandr Suvorov

---

[![PyPI](https://img.shields.io/pypi/v/linuxautofix)](https://pypi.org/project/linuxautofix) 
[![PyPI - Downloads](https://img.shields.io/pypi/dm/linuxautofix)](https://pypi.org/project/linuxautofix)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/linuxautofix)](https://pypi.org/project/linuxautofix)
[![GitHub all releases](https://img.shields.io/github/downloads/mysmarthub/linuxautofix/total)](https://github.com/mysmarthub/linuxautofix/)
[![GitHub](https://img.shields.io/github/license/mysmarthub/linuxautofix)](https://github.com/mysmarthub/linuxautofix/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/linuxautofix)](https://github.com/mysmarthub/linuxautofix/)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mysmarthub/linuxautofix)](https://github.com/mysmarthub/linuxautofix/)
[![GitHub repo size](https://img.shields.io/github/repo-size/mysmarthub/linuxautofix)](https://github.com/mysmarthub/linuxautofix/)
[![GitHub Repo stars](https://img.shields.io/github/stars/mysmarthub/linuxautofix?style=social)](https://github.com/mysmarthub/linuxautofix/)

---
[![Download Linux Auto Fix](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/linuxautofix/files/latest/download)

[![Download Linux Auto Fix](https://img.shields.io/sourceforge/dt/linuxautofix.svg)](https://sourceforge.net/projects/linuxautofix/files/latest/download)

---

![Linux Auto Fix](https://github.com/mysmarthub/linuxautofix/raw/master/images/linuxautofix_logo.png)

---

Help the project financially:
---
>Yandex Money:
https://yoomoney.ru/to/4100115206129186

    Visa:    4048 4150 0400 5852

    Sberbank Russia: 4276 4417 5763 7686

https://paypal.me/myhackband

---

Description
---

>Store your frequently used commands in one place, edit, 
> run, create new command packages, use the default 
> command package to store common commands for different packages.

>A project that gave rise to another interesting project. 
> At first, Linux Auto Fix was used narrowly, 
> to automate the execution of commands to configure the 
> system after installation, but later developed 
> into a more simplified project to automate the 
> storage and execution of commands ["Commandoro"](https://github.com/mysmarthub/commandoro). 

> In ["Commandoro"](https://github.com/mysmarthub/commandoro), 
> there is also a graphical version of the 
> program that allows you to execute command packages, 
> create, modify, and update configuration files that 
> can be used in both the console version and the graphical version.

> The console version allows you to run a script in the terminal, 
> passing it a file with settings as an argument, or use the default file. 

> In the process, you select the desired command package, 
> then you can start execution, display a list of commands 
> for this package, or return to the selection of the command package. 

> After executing all the commands, the program goes to the 
> main menu and again waits for input to 
> select the desired package, or exit the program. 

> During execution, it displays information about the command number, 
> the command itself, and the status of its execution. 
> Upon completion, it displays information about the 
> number of executed commands, and the number of errors during execution.

> With this utility, you can automate the execution of 
> commands on a Linux system. 
> 
> Create a file with command packages or use and edit the default file. 
> In the settings file, create new command packages, 
> use the key as the package name, 
> and the value as the list of commands (see the default file).

>In each item, collect the necessary commands, and start their 
> automatic execution when necessary.
> 
> With this utility, it is very convenient to perform routine tasks, 
> automatically execute the necessary commands, 
> and also configure the system after installation.

> The settings file is very simple and clear, 
> and all the commands you need for different cases or 
> different systems will be stored in one place. 

> You will not need to keep them in memory, 
> in different files, enter them manually or search the Internet.

> In the settings file, there is a section from 
> which commands will be executed in any case. 
> This is done in order to bring common commands for all 
> command packages into a single default package.

> You can create your own files with settings or edit the default settings file. If you have created your own settings file, just specify the full path to this file when running the script as a parameter. If you are using the graphical version of the program, just open the file with the settings using the open button. The file must be in json format and have the required structure.
The section with the "default" commands will run anyway.

```json
{
  "Commands pack name": [
    "command one",
    "command two"
  ],
  "Next commands pack name": [
    "command one",
    "command two"
  ],
  "default": [
    "command one",
    "command two"
  ]
}
```

>After starting, the program will prompt you to select the desired item, 
> and then execute all the commands that are stored in the 
> file with the settings under this name/key.

---

Help:
----

```
usage: Linux Auto Fix v0.0.7 [-h] [--version] [path]

Program for auto-tuning Linux distributions after installation

positional arguments:
  path        Путь к файлу с настройками

optional arguments:
  -h, --help  show this help message and exit
  --version   Program version

The configuration file must be a file in the 
format .json and have the correct settings

```


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
python linuxautofix/linuxautofix/linuxautofix.py /path to the settings file/config.json
python linuxautofix/linuxautofix/linuxautofix.py
 
 or

sudo python linuxautofix/linuxautofix/linuxautofix.py /path to the settings file/config.json
sudo python linuxautofix/linuxautofix/linuxautofix.py
```

Links:
---
>[GitHub](https://github.com/mysmarthub/linuxautofix)
> 
>[PyPi](https://pypi.org/project/linuxautofix/)
> 
>[Sourceforge](https://sourceforge.net/projects/linuxautofix/files/latest/download)
---

Disclaimer of liability:
------------------------
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Support:
---
    Email: myhackband@yandex.ru
    Copyright © 2020 Aleksandr Suvorov
