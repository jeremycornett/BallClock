docker build -t ballclock .
docker run -a stdin -a stdout -i -t ballclock /bin/bash run.sh