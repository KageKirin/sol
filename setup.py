#!/bin/python
# -*- coding: utf-8 -*-

### for py2exe
"""
from distutils.core import setup
from glob import glob
import py2exe

data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

setup(
    data_files=data_files,
    console=['convert.py'])
"""


### for cx_Freeze
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "convert",
        version = "0.1",
        description = "Sol Convert",
        options = {"build_exe": build_exe_options},
        executables = [Executable("convert.py", base=base)])
