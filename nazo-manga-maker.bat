@echo off
@REM Change directory to the location of the Python script
cd /d %~dp0

@REM Run the Python script with default output count and name
python nmm.py

@REM Optional: To specify output count and name, use the following line instead
@REM python nmm.py 3 output jpg 85 top-left 2x3

@REM If you want to keep the command line open after processing, uncomment @REM pause.
@REM pause