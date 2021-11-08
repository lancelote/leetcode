#!/usr/bin/env bash

python -mvenv .venv
. .venv/bin/activate
pip install -r requirements.txt
pre-commit install
