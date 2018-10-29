# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return 'Hello WINTER CODING!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
