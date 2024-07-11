#!/bin/bash

VENV=".venv"

python3 -m venv $VENV
source $VENV/bin/activate

python3 -m pip install -r requirement.txt