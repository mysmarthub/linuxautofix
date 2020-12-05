Linux Auto Fix
===
Консольная утилита для автонастройки дистрибутивов Linux после установки
===
Aleksandr Suvorov | myhackband@ya.ru
---
<p>
Для работы утилита требует файлы с настройками в формате .json
со специализированными настройками. 
Адрес файла или папки с файлами настроек, можно указать при запуске 
в качестве параметра. Если запустить без параметров, будут использоваться
файлы по-умолчанию из папки json_fix, эта папка должа находится в той же папке,
что и исполняемый файл. Собственные файлы конфигурации которые вы можете создать
по принципу файлов по умолчанию, следует так же поместить в данную папку(json_fix)
</p>
<p>
После запуска утилита выполнит начальные команды,
установит указанные пакеты, Python пакеты, Snap пакеты,
допишет указанные настройки в конец указанных файлов,
выполнит завершающие команды.
</p>
<p>
    Пример запуска:
</p>
<code>python autofix.py /home/linux.json</code>

<code>python autofix.py /home/my_fix</code>

<p>Если у вас нет фалов с настройками, 
вы можете воспользоваться файлами для разных систем по-умолчанию.
Более того, каздый файл вы можете редактировать, 
добавляя или удаляя нужные вам команды.</p>

<p>Вы можете самостоятельно создавать файлы с 
настройками и либо указывать их в качестве аргумента при запуске,
либо добавлять в папку json_fix. При запуске утилиты без параметров,
ваши файлы будут доступны для выбора и применения.</p>

<p>
При создании собственных файлов используйте 
структуру из файлов по умолчанию из папки json_fix, 
не меняйте структуру, добавляйте только нужные значения.
</p>
<pre>
"options":
    "name": "Имя системы",
    "pack_man": "Команда для установки пакетов с помощью пакетного менеджера например apt",
    "pip_man": "Команда для установки Python пакетов с помощью pip",
    "snap_man": "Команда для установки пакетов с помощью snap",
    "file_fixer": "Команда для записи в файлы конфигураций, менять не рекоммендуется"
"pre_install": "Список команд которые будут выполнены в первую очередь, до установки программ и настройки файлов."
"install":
    "pack_man": "список приложений для пакетного менеджера"
    "pip_man": "список пакетов для Python pip"
    "snap_man": "список программ для snap"
"file_fix":
    "fix": Список настроек типа: "Адрес файла": "Записываемое значение"
"post_install": "Список команд которые будут выполнены в последнюю очередь."
</pre>
