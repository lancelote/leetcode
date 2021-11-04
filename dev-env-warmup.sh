#!/usr/bin/env bash

python -mvenv .venv
source .venv/bin/activate
pip install -r requirements.txt
pre-commit install
