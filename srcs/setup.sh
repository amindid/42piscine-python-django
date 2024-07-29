#!/bin/bash

VENV="django_venv"

python3 -m venv $VENV

source $VENV/bin/activate

python3 -m pip install -r requirements.txt