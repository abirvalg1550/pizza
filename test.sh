#!/bin/bash -e 

flake8 --exclude venv/ .
./manage.py test
