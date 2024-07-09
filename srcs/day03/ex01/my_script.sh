#!/bin/bash

path="https://github.com/jaraco/path.git"

python3 -m venv local_lib
source local_lib/bin/activate

python3 -m pip --version

python3 -m pip install --upgrade pip --log pip.log --force-reinstall git+$path
python3 my_program.py