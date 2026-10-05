#!/usr/bin/env bash
#
# run_tests.sh — Harness: één commando draait alles (lint, type check, tests)
#
# Gebruik:
#   bash harness/run_tests.sh
#
# In Deel 1 en 2 bestaat er nog geen code. Dat is normaal: de harness werkt
# dan gewoon en meldt dat er niets te testen valt.

set -uo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

echo "========================================"
echo " Harness: lint + type check + tests"
echo "========================================"

FAIL=0

if compgen -G "src/*.py" > /dev/null || compgen -G "tests/*.py" > /dev/null; then
    echo ""
    echo "--- ruff (lint) ---"
    ruff check src tests || FAIL=1
    echo ""
    echo "--- mypy (type check) ---"
    mypy src tests || FAIL=1
    echo ""
    echo "--- pytest ---"
    python -m pytest tests -v --tb=short || FAIL=1
else
    echo ""
    echo "Geen src/*.py of tests/*.py gevonden."
    echo "Dit is normaal in Deel 1 (nog geen code) en Deel 2 (alleen tests mag ook)."
fi

echo ""
if [ "$FAIL" -eq 0 ]; then
    echo "✓ Harness geslaagd!"
    exit 0
else
    echo "✗ Harness faalt — laat de agent de fouten oplossen."
    exit 1
fi
