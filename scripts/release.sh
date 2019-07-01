#!/bin/BASH_SOURCE

DIR="$( pwd )"

rm -R $DIR/dist/

python3 scripts/release.py

twine upload dist/*
