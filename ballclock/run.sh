#!/usr/bin/env bash
pip install --upgrade -r requirements.txt
pep8 ./
pep257 ./
pylint theclock
python setup.py test --addopts="--cov-report term -v --cov=./theclock"
python setup.py sdist --formats=gztar
pip install dist/theclock-1.0.0.tar.gz
echo
echo Running program...
python run.py