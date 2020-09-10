from flask import render_template, request
from flask.views import MethodView

from datetime import datetime

from google.cloud import datastore
from google.cloud import vision
from google.cloud import storage
client = vision.ImageAnnotatorClient()
image_formats = ['image/jpeg', 'image/png', 'image/apng', 'image/bmp', 'image/gif', 
                 'image/x-icon', 'image/svg+xml', 'image/tiff', 'image/webp']

class UploadPhoto(MethodView):
    def post(self):
        is_coffee = False
        coffee_text = 'That is not coffee!'

        # gets image submitted from the post request
        photo = request.files['file']
        if not photo.content_type in image_formats:
            return render_template('error.html')

        # sets up the image for the vision client
        image = vision.types.Image(content=photo.read())

        # sends the image to cloud visions label detection
        response = client.label_detection(image=image)

        # checks image labels to see if one is coffee
        for label in response.label_annotations:
            if label.description is 'Coffee':
                is_coffee = True
                break

        if is_coffee:
            coffee_text = 'MMMM that is some good looking coffee!'

        entries = {'coffee': coffee_text, 'image_labels': response.label_annotations}

        return render_template('upload_photo.html', entries=entries)
