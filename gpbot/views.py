from flask import Flask, render_template, jsonify, request

from .grandpy import Grandpy

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/grandpy/', methods=['POST'])
def grandpy():
    grandpy = Grandpy()
    return jsonify({'answer': grandpy.grandpy_answer(request.form[
                                                         'user_text'])})


if __name__ == "__main__":
    app.run()
