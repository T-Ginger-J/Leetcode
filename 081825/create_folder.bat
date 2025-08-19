@echo off
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (
    set yy=%%c
    set mm=%%a
    set dd=%%b
)
set foldername=%yy:~2%%mm%%dd%

if not exist %foldername% (
    mkdir %foldername%
    echo Folder %foldername% created.
) else (
    echo Folder %foldername% already exists.
)
