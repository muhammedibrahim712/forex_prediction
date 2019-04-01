@echo off
set PATH=%PATH%;mingw\

setlocal enableextensions enabledelayedexpansion
call :getargc argc %*

echo TrueFX tick data downloader v0.2
echo It downloads the tick data into one single csv file
echo Created by Laszlo T.
echo.

if not "%argc%" == "5" (
    echo Usage:
    echo %0 SYMBOL startYear startMonth endYear endMonth"
    echo Example: %0 EURUSD 2012 1 2013 1
	exit /b 1
)

bash -c "source libtruefx; download %1 %2 %3 %4 %5"

endlocal
goto :eof

:getargc
    set getargc_v0=%1
    set /a "%getargc_v0% = 0"
:getargc_l0
    if not x%2x==xx (
        shift
        set /a "%getargc_v0% = %getargc_v0% + 1"
        goto :getargc_l0
    )
    set getargc_v0=
    goto :eof
