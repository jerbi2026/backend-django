#!/bin/bash

# Active l'environnement virtuel
source venv/bin/activate

# Lance les tests avec pytest
pytest tests/ -v

# Génère un rapport de couverture
pytest --cov=tasks --cov=users --cov-report=html