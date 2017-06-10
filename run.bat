pip install --upgrade -r requirements.txt
pep8 .\
pep257 .\
pylint .\
pytest ball_clock.py --cov=BallClock --verbose
python ball_clock.py