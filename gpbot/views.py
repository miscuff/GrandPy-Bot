from flask import Flask, render_template, url_for, request, jsonify
from .grandpy import Grandpy

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/grandpy/', methods=['POST'])
def grandpy():
    grandpy = Grandpy()
    return jsonify({'answer': grandpy.grandpy_answer(request.form['input_value'])})


if __name__ == "__main__":
    app.run()
