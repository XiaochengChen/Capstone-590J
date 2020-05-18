set oShell = CreateObject("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c C:\Users\590Capstone\Documents\Notepad\run.bat"
oShell.Run strArgs, 0, false
