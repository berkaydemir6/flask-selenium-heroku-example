from flask import Flask
import selenium_process


app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'


if __name__ == '__main__':
    app.run()