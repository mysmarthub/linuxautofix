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

-----------------------------
Help the project financially:
-----------------------------
If you like my projects, you can support me financially -
" for an apartment in Moscow or a hut in the taiga) ..."

https://paypal.me/myhackband

Yandex money:

https://yoomoney.ru/to/4100115206129186

Visa: 4048-0250-0089-5923



If you can't find a way to donate, write to me:
mailto: mysmarthub@ya.ru


---
What's news?
---
1. Changed interface
2. An added menu for working with file. 
3. Removed -d option
4. Removed option -y
5. Added option -a
6. Added the ability to select autorun commands.
7. If you do not select autorun or do 
   not specify an option -a, the program will ask 
   for permission to execute commands, 
   which will allow unnecessary commands to be skipped.
   
8. If you do not select autorun, 
   after the program finishes, 
   you can return to the selection 
   of packages, or exit.
   
9. Dismissed the possibility of using the default package, 
   now the package named "default" 
   must be run as a regular package.


---------------
Termux support:
---------------
You can easily use the utility with Termux on mobile phones and tablets.

1. Install Termux
2. pkg install python
3. pip install linuxautofix
4. linuxautofix --help

-----------
Description
-----------

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
settings of popular Linux systems after installation.

---

The program allows you to execute a set of commands
in automatic and semi-automatic modes.

---

With this utility you can automate the execution
commands in Linux system,
and also keep all the necessary commands in one
file under different names, for future use, automatic start.

---

Create a file with command packages or use and edit the default file.
In the settings file, create new command packages,
use the key as the package name,
and the value as the list of commands (see the default file).

---

In each package, collect the required commands and run them
automatic execution if necessary.

---

With this utility, it is very convenient to perform routine tasks,
automatically execute the necessary commands,
and also configure the system after installation.

---

The settings file is very simple and clear,
and all the commands you need for different cases or
different systems will be stored in one place.

---

You will not need to store them in memory,
in different files, or search the Internet.

---

In the file with command packages
you can create a "default" package and
then compile commonly used commands into it.

---

You can create your own customization files or edit
default settings file.
If you created your own settings file,
just give the full path to this file when running the script for the -f [name.file] option.
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
pass the parameter -n [name], or --name [name], the name of the command package,
as well as the option - for automatic execution and autocompletion.


----
Help:
----

```
Usage: linuxautofix.py [OPTIONS]

    linuxautofix.py --help


Usage: linuxautofix.py [OPTIONS]

  Linux Auto Fix - CLI utility for automatic command execution, and
  auto-tuning Linux distributions after installation.

  - Run the utility without parameters to manually select options.

  Example: linuxautofix python linuxautofix.py

  - Use the option -f/--file [filename] to select a file with command
  packages.

  Example: linuxautofix -f file.json python linuxautofix.py -f file.json

  - Use the option -n/--name to specify an existing package name.

  Example: linuxautofix -f file.json -n Ubuntu python linuxautofix.py -f
  file.json -n Ubuntu

  - Use the option -a for autorun and auto-completion.

  Example: linuxautofix -f file.json -n Ubuntu -a python linuxautofix.py
  -f file.json -n Ubuntu -a

  Author and developer: Aleksandr Suvorov

  Url: https://github.com/mysmarthub/

  Email: mysmarthub@ya.ru

  Donate: https://paypal.me/myhackband

  https://yoomoney.ru/to/4100115206129186

  4048 0250 0089 5923

Options:
  -f, --file FILE  The path to the file with the command packs
  -n, --name TEXT  Name of the package
  -a, --auto       Auto command execution, auto exit
  -v, --version    Displays the version of the program and exits.
  --help           Show this message and exit.



```

------------------------
Installation and launch:
------------------------
    You can install the utility using pip:

`pip install linuxautofix`


`sudo pip install linuxautofix`

    And then run it like this:

`linuxautofix`

`linuxautofix --file config.json`

`linuxautofix --file config.json --name Ubuntu`

On some systems, some commands require administrator rights,
so you can install the utility and run it further using:

`sudo pip install linuxautofix`

`sudo linuxautofix --file config.json --name Ubuntu`

You can download the source files and run using Python:

`git clone https://github.com/mysmarthub/linuxautofix.git`

`cd linuxautofix`

`pip install -r requirements`

`python linuxautofix/linuxautofix.py --file linuxautofix/config.json`

or

`sudo pip install -r requirements`

`sudo python linuxautofix/linuxautofix.py`

------
Links:
------

[GitHub](https://github.com/mysmarthub/linuxautofix)

[PyPi](https://pypi.org/project/linuxautofix/)

[Sourceforge](https://sourceforge.net/projects/linuxautofix/files/latest/download)

------------------------
Disclaimer of liability:
------------------------
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

-------------
Requirements:
-------------

The program uses Click: https://github.com/pallets/click
by license: https://github.com/pallets/click/blob/master/LICENSE.rst

Python 3+ : https://python.org

--------
Support:
--------
    Email: mysmarthub@ya.ru
    Copyright © 2020 Aleksandr Suvorov

    -----------------------------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details)
    https://github.com/mysmarthub
    Copyright © 2020-2021 Aleksandr Suvorov
    -----------------------------------------------------------------------------
