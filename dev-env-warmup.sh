#!/usr/bin/env bash

python3 -mvenv .venv
. .venv/bin/activate
pip install -r requirements.txt
pre-commit install
