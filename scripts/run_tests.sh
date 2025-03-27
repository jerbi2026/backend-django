#!/bin/bash

source venv/bin/activate

pytest tests/ -v

pytest --cov=tasks --cov=users --cov-report=html