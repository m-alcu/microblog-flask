from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging.handlers import RotatingFileHandler

flask_app = Flask(__name__)


flask_app.config.from_object(Config)

formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler('/tmp/flask.log', maxBytes=10000000, backupCount=5)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
flask_app.logger.addHandler(handler)

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from app import routes, models

