Linux Auto Fix
===
---
    Created: Aleksandr Suvorov
---
![PyPI](https://img.shields.io/pypi/v/linuxautofix) 
![PyPI - Downloads](https://img.shields.io/pypi/dm/linuxautofix) 
![GitHub](https://img.shields.io/github/license/mysmarthub/linuxautofix)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/linuxautofix)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/linuxautofix)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mysmarthub/linuxautofix)
>Console utility for auto configuration of Linux distributions after installation
---

Description
---

>With this utility, you can automate the execution 
> of commands on a Linux system. Create your own file 
> with settings, add the necessary commands to it 
> and start automatic execution when it is necessary.

> With this utility, it is very convenient to 
> perform routine tasks, as well as to configure 
> and install the system after installation.
> 
> The settings file is very simple, suitable 
> even for the most ordinary users.

> When you run the utility on the command line, 
> the path to the settings file is passed to it as an argument, 
> if the file is not found or another error occurs, 
> the default settings file will be used(if you have one), 
> this file must be located in the same folder as the program being run.
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

`linuxautofix [path]`

>On some systems, some commands require administrator rights, 
> so you can install the utility and run it further using:

`sudo pip install linuxautofix`

`sudo linuxautofix`

>You can download the source files and run them using Python:

```
git clone https://github.com/mysmarthub/linuxautofix.git
python linuxautofix/linuxautofix/autofix.py
 
 or

sudo python linuxautofix/linuxautofix/autofix.py
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
  "ubuntu": [
    "sudo apt update",
    "sudo touch .gitconfig",
    "sudo apt-get install python",
    "pip3 install mycleaner",
    "pip3 install smartcleaner",
    "pip3 install sfd",
    "pip3 install mpassgen",
    "sudo echo GRUB_TIMEOUT=30 >> /etc/default/grub",
    "sudo echo GRUB_GFXMODE=1280x1024 >> /etc/default/grub",
    "sudo echo DefaultTimeoutStopSec=10s >> /etc/systemd/system.conf",
    "sudo echo ENABLED=yes >> /etc/default/ufw",
    "sudo echo vm.swappiness=0 >> /etc/sysctl.conf",
    "sudo echo vm.vfs_cache_pressure = 1000 >> /etc/sysctl.conf",
    "python3 -m pip install --user --upgrade setuptools wheel",
    "sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common",
    "sudo apt-get install -y curl",
    "systemctl daemon-reload",
    "sudo ufw enable",
    "sudo ufw default deny",
    "sudo ufw deny ssh",
    "sudo ufw logging on",
    "sudo ufw status verbose",
    "sudo update-grub",
    "sudo sysctl -p"
  ],
  "fedora": [
    "sudo dnf update",
    "sudo dnf groupupdate multimedia sound-and-video",
    "sudo rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm",
    "sudo rpm -Uvh http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm",
    "sudo dnf install python",
    "sudo dnf install python3",
    "sudo dnf install git",
    "sudo dnf install htop",
    "sudo dnf install twine",
    "sudo dnf install tree",
    "sudo dnf install mc",
    "sudo dnf install cmatrix",
    "sudo dnf install vlc",
    "sudo dnf install gstreamer1-libav",
    "sudo dnf install gstreamer1-plugins-bad-free",
    "sudo dnf install gstreamer1-plugins-bad-free-extras",
    "sudo dnf install gstreamer1-plugins-bad-freeworld",
    "sudo dnf install gstreamer1-plugins-bad-nonfree",
    "sudo dnf install gstreamer1-plugins-good gstreamer1-plugins-ugly",
    "sudo dnf install lame-libs",
    "sudo dnf install ffmpeg-libs",
    "sudo dnf install compat-ffmpeg28",
    "pip install virtualenv",
    "pip install wheel",
    "pip install mycleaner",
    "pip install smartcleaner",
    "pip install sfd",
    "pip install mpassgen"
  ],
  "Manjaro": [
    "pacman-mirrors --fasttrack",
    "pacman -Syyu",
    "pacman -Sy cmatrix",
    "pacman -Sy git",
    "pacman -Sy htop",
    "pacman -Sy twine",
    "pacman -Sy tree",
    "pacman -Sy mc",
    "pacman -Sy vlc",
    "pip install virtualenv",
    "pip install wheel",
    "pip install mycleaner",
    "pip install smartcleaner",
    "pip install sfd",
    "pip install mpassgen",
    "sudo echo GRUB_TIMEOUT=30 >> /etc/default/grub",
    "sudo echo GRUB_GFXMODE=1280x1024 >> /etc/default/grub",
    "sudo echo ENABLED=yes >> /etc/default/ufw",
    "sudo ufw enable",
    "sudo ufw default deny",
    "sudo ufw deny ssh",
    "sudo ufw logging on",
    "sudo ufw status verbose",
    "sudo update-grub",
    "sudo sysctl -p"
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
    