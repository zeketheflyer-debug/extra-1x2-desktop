# build c5541283b5
# (auto) 75e1f8
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
