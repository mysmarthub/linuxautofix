Linux Auto Fix
===
    
    Console utility for auto-configuration of Linux distributions after installation
    
    

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

![Linux Auto Fix](https://github.com/mysmarthub/linuxautofix/raw/master/images/logo.png)

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
>With this utility, you can automate
the execution of commands on a Linux system.
Create a settings file with the necessary items,
or use/edit the default file.
In each item, collect the necessary commands,
and start their automatic execution when necessary.

>With this utility, it is very convenient 
to perform routine tasks , as well as configure 
and install the system after installation.

>The settings file is very simple and clear, 
and all the commands you need for different 
cases or different systems will be stored in one place.

>In the settings file, a section with a special 
name default is available, 
any commands added to this section 
will be executed by default after the 
main commands are executed.

>You can create your own files with settings
or edit the default settings file. 
If you have created your own settings file, 
just specify the full path to this file when 
running the script as a parameter. 
Keep in mind that at the moment the file 
must be in json format, have this file extension, 
and use the required structure:

>The section with the "default" commands will run anyway.

```json
{
  "Name to be displayed in the list of commands": [
    "command one",
    "command two"
  ],
  "Next name": [
    "command one",
    "command two"
  ],
  "default": [
    "command one",
    "command two"
  ]
}
```

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
python linuxautofix/linuxautofix/autofix.py /path to the settings file/config.json
 
 or

sudo python linuxautofix/linuxautofix/autofix.py /path to the settings file/config.json
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
