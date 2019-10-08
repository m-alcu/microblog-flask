follows instructions from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

On every database changes (models.py):

$ flask db migrate -m "change"
$ flask db upgrade