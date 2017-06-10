pip install --upgrade -r requirements.txt
cd ballclock
pep8 .\
pep257 .\
pylint theclock
python setup.py test --addopts="--cov-report term -v --cov=./theclock"
python setup.py sdist --formats=gztar