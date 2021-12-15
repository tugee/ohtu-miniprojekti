#!/bin/bash

# käynnistetään Flask-palvelin taustalle (huomaa & komennon lopussa)
export FLASK_APP=src/app.py
poetry run python3 -m flask run &
# poetry run python3 src/app.py &


# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä,
# jolloin localhost:5000/ping antaa vastauksen statuskoodilla 200
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/ping)" != "200" ]]; 
  do sleep 1; 
done

# suoritetaan testit
poetry run robot src/tests/index.robot
# poetry run robot src/tests

# pysäytetään Flask-palvelin portissa 5000
function clean_up {
  kill $(lsof -t -i:5000)
}

# suoritetaan clean_up-funktio, kun prosessi lopettaa suorituksen
trap clean_up EXIT

