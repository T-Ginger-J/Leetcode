@echo off
:: Get date in YYMMDD format
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (
    set yy=%%c
    set mm=%%a
    set dd=%%b
)
set foldername=%yy:~2%%mm%%dd%

:: Folder path (change this to where you want the folders created)
set target_dir=C:\Users\trent\Downloads\Leetcode\Leetcode

:: Make sure target directory exists
if not exist "%target_dir%" mkdir "%target_dir%"

:: Create today's folder
if not exist "%target_dir%\%foldername%" (
    mkdir "%target_dir%\%foldername%"
    echo Folder %target_dir%\%foldername% created.
) else (
    echo Folder %target_dir%\%foldername% already exists.
)
