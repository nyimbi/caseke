#!/usr/bin/env bash
dropdb ctmp; createdb ctmp;
python pony9.py
flask-sqlacodegen postgresql://nyimbi:abcd1234@localhost/ctmp --flask --outfile mod9.py
cp imps.txt models.py
cat mod9.py >> models.py
