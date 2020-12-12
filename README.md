Linux Auto Fix
===
---

>Console utility for auto configuration of Linux distributions after installation

> Attention!
> Be very careful with the commands you pass to the program.
> The author of the program does not bear any responsibility for your actions, but
> provides only an automated shell for executing commands on your system.

Installation and launch:
---

`pip install linuxautofix`

`linuxautofix [optional parameters with paths to files or settings folders]`

    To write to some files, you may need to run as administrator.
    You can set like this:

`sudo pip install linuxautofix`

`sudo pip3 install linuxautofix`

    Run like this:

`sudo linuxautofix [optional parameters with paths to files or settings folders]`

    Or so:

`sudo python autofix.py [optional parameters with paths to files or settings folders]`


---
[GitHub](https://github.com/mysmarthub/linuxautofix) / [PyPi](https://pypi.org/project/linuxautofix/)
---
>Download the source files [GitHub](https://github.com/mysmarthub/linuxautofix)

>Or `git clone https://github.com/mysmarthub/linuxautofix.git`

> To run use:

`python autofix.py [optional parameters with paths to files or settings folders]`

---

>The utility requires files with settings in the 
> file.json format with special settings.
Addresses of files or folders with settings files can 
> be specified at startup as a parameter/parameters. 
> If run without parameters, the default files from the json_fix 
> folder will be used, this folder must be in the same folder as
where the executable is located. Custom configuration files, 
> which you can create as default files, 
> must also be located in this folder (json_fix), 
> or passed as parameters at startup (full paths to files and / and folders.

---

>Once launched, the utility will execute the initial commands using the batch
the manager will install the specified packages, Python packages, Snap packages,
will add the specified settings to the end of the specified files,
will execute final commands.

---
Launch example:
---
<code>python autofix.py /home/linux.json</code>

<code>python autofix.py /home/my_fix</code>

---

>If you do not have files with settings,
you can use files for different systems by default.
Moreover, you can edit each file,
adding or removing the commands you want.

>You can create files yourself with
settings and either specify them as an argument at startup,
or add it to the json_fix folder. When running the utility without parameters,
your files will be available for selection and application.


>When creating your own files use
structure from files by default from the json_fix folder,
do not change the structure, add only the values you want.

<pre>
"options":
    "name": "System name",
    "pack_man": "Command for installing packages using a package manager like apt",
    "pip_man": "Command for installing Python packages using pip",
    "snap_man": "Command to install packages using snap",
    "file_fixer": "Command for writing to configuration files, it is not recommended to change"
"pre_install": "List of commands that will be executed first, before installing programs and configuring files."
"install":
    "pack_man": "list of applications for the package manager"
    "pip_man": "package list for Python pip"
    "snap_man": "list of programs for snap"
"file_fix":
    "fix": List of settings of the type: "File address": "Recorded value"
"post_install": "List of commands to be executed last."
</pre>

info:
---
    Copyright © 2020 Aleksandr Suvorov
    Licensed under the terms of the MIT License

Support:
---
    Author: Aleksandr Suvorov
    Email: myhackband@yandex.ru

Help the project financially:
---
>Yandex Money:
https://money.yandex.ru/to/4100110928527458

>Sberbank Russia:
4276 4417 5763 7686
    