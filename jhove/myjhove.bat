@echo off
rem Batch command file developed by Dan Lou (http://fishbb.github.io).
rem The file will look into a directory and its sub-directories, find all .tif images, and run against jhove TIFF validation.
rem Output will be saved to an output file.
rem Replace "D:\" with your directory; Replace "output.txt" with your desired place to store output.
rem Run this file from command line inside the jhove directory, usually jhove is installed at C:\Users\Your Username\jhove.
rem For example: C:\Users\dlou\jhove>myjhove

for /r D:\ %%i in (*.tif) do (
echo %%i 
jhove -m TIFF-hul "%%i" >> output.txt
)