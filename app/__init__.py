from flask import Flask
from config import config

app = Flask(__name__)
SECRET_KEY=config.Config.SECRET_KEY
print(SECRET_KEY)

from app import routes
