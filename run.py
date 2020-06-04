from flask import Flask
from flask_simple import Simple

app = Flask(__name__)
simple = Simple(app)

@app.route('/')
def home():
    return 'welcome home!'
