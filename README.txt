Linux Auto Fix
==============
Console utility for automatic command execution,
and auto-tuning Linux distributions after installation.

    -----------------------------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details)
    https://github.com/mysmarthub
    Copyright © 2020-2021 Aleksandr Suvorov
    -----------------------------------------------------------------------------

---

Help the project financially:
-----------------------------
If you like my projects, you can support me financially -
" for an apartment in Moscow or a hut in the taiga) ..."

https://paypal.me/myhackband

Yandex money](https://yoomoney.ru/to/4100115206129186

Visa: 4048-4150-0400-5852



If you can't find a way to donate, write to me:
mailto: mysmarthub@ya.ru

---

Termux support:
---
You can easily use the utility with Termux on mobile phones and tablets.

1. Install Termux
2. pkg install python
3. pip install linuxautofix
4. linuxautofix --help

---

Description
---

Linux Auto fix - CLI utility for automatic command execution,
and auto-tuning Linux distributions after installation.

---

Store frequently executed commands in a single file,
and run them automatically at any time.

---

In the default file (config.json), we will collect frequently
executed commands after installing various Linux
systems to automate their configuration after installation.

---

Create new command packages, use standard command packages to
configure popular Linux systems after installation.

---

The program allows you to execute command
packages in automatic and semi-automatic mode.

---

With this utility, you can automate the execution
of commands on a Linux system,
as well as store all the necessary commands in a single
file under different names, for later use.

---

Create a file with command packages or use and edit the default file.
In the settings file, create new command packages,
use the key as the package name,
and the value as the list of commands (see the default file).

---

In each item, collect the necessary commands, and start their
automatic execution when necessary.

---

With this utility, it is very convenient to perform routine tasks,
automatically execute the necessary commands,
and also configure the system after installation.

---

The settings file is very simple and clear,
and all the commands you need for different cases or
different systems will be stored in one place.

---

You will not need to keep them in memory,
in different files, enter them manually or search the Internet.

---

In the file with the command packages,
you can create a "default" package and then use it
as an extension to the executed package.

---

In it, you can collect the same commands for
different packages and when you run the utility,
pass it the-d parameter, then after executing the main package of commands,
the "default" command package will be additionally executed.

---

You can create your own files with settings or edit
the default settings file.
If you have created your own settings file,
just specify the full path to this file when
running the script as a parameter.
The file must be in json format and have the required structure.

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

To automatically execute a batch of commands at startup,
pass the-n or --name parameter the name of the batch of commands,
and if it exists after startup, the automatic
execution of commands from this batch will begin.
In addition, you can use -d to add commands from the default package.


---

Help:
----

```
Usage: linuxautofix.py [OPTIONS]

    Linux Auto Fix - CLI utility for automatic command execution

    and auto-tuning Linux distributions after installation.

    - To work, the utility uses files that store named command packages,
    where the name is the name of the command package,     and the value is a
    list of commands.

    - You can create your own files with command packages using     default
    structure.

    - Use the name "default" for the package with the default commands.
    You can run them in addition to the selected batch of commands.

    - You can pass the file name as an argument     or use the default file,
    it should be located     in the same directory as the file being run.

    - The console version allows you to run the script in the terminal,
    passing it a file with the settings as an argument,     or use the default
    file. In the process of working,     you choose the right one command
    package,     after which you can start executing, display a list     of
    commands for this package,     or go back to selecting the command
    package.

    - Using the -n or --name parameter, you can specify the name     of the
    command package at startup,     then the utility will immediately start
    automatic execution     of commands from this package.

    - Examples of implementation:

    python linuxautofix.py --file=config.json -d

    python linuxautofix.py --file=config.json-d --name=Ubuntu

    or

    linuxautofix --file=config.json -d

    linuxautofix --file=config.json-d --name=Ubuntu

  Options:
    -f, --file TEXT  The path to the file with the command packs
    -d, --default    Run an additional batch of commands from default
    -t, --test       Test run, commands will not be executed.
    -n, --name TEXT  Name of the package to run automatically
    -v, --version    Displays the version of the program and exits.
    --help           Show this message and exit.


```

Installation and launch:
---
    You can install the utility using pip:

`pip install linuxautofix`


`sudo pip install linuxautofix`

    And then run it like this:

`linuxautofix`

`linuxautofix --file config.json -d`

`linuxautofix --file=config.json --name=Ubuntu -d`

On some systems, some commands require administrator rights,
so you can install the utility and run it further using:

`sudo pip install linuxautofix`

`sudo linuxautofix --file=config.json --name=Ubuntu -d`

You can download the source files and run using Python:

`git clone https://github.com/mysmarthub/linuxautofix.git`

`cd linuxautofix`

`pip install -r requirements`

`python linuxautofix/linuxautofix.py --file=linuxautofix/config.json`

or

`sudo pip install -r requirements`

`sudo python linuxautofix/linuxautofix.py`

Links:
-----

[GitHub](https://github.com/mysmarthub/linuxautofix)

[PyPi](https://pypi.org/project/linuxautofix/)

[Sourceforge](https://sourceforge.net/projects/linuxautofix/files/latest/download)

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

---

    -----------------------------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details)
    https://github.com/mysmarthub
    Copyright © 2020-2021 Aleksandr Suvorov
    -----------------------------------------------------------------------------

The program uses Click:
-----------------------
https://github.com/pallets/click
by license:
https://github.com/pallets/click/blob/master/LICENSE.rst


Support:
--------
    Email: mysmarthub@ya.ru
    Copyright © 2020 Aleksandr Suvorov
