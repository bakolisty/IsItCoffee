"""
A simple python, flask app that guesses if a submitted image contains coffee or not.
Written by: Kegan Bako-Listy
"""
import flask
from flask.views import MethodView
from index import Index
from upload_photo import UploadPhoto

app = flask.Flask(__name__)

app.add_url_rule('/', view_func=Index.as_view('index'), methods=["GET"])

app.add_url_rule('/upload_photo', view_func=UploadPhoto.as_view('upload_photo'), methods=["POST"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)