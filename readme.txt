follows instructions from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

First time to create database scripts

$ flask db init

On every database changes (models.py):

$ flask db migrate -m "change"
$ flask db upgrade

You can populate some records to play

$ python populate.py