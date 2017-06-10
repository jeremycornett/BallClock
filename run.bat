cd ballclock
pip install --upgrade -r requirements.txt
pep8 .\
pep257 .\
pylint theclock
python setup.py test --addopts="--cov-report term -v --cov=./theclock"
python setup.py sdist --formats=gztar
cd ..
docker build -t ballclock .
docker run -a stdin -a stdout -i -t ballclock python run.py