from flask import Flask
from GenPubTrends.main.views import main
from os import urandom

SECRET_KEY = urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(main, url_prefix='/')

