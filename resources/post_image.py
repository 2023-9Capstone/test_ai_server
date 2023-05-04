from flask import request, jsonify, url_for
from flask_restx import Resource, Namespace
import os

from flask import current_app as app

api = Namespace(
    name="model_serving",
    description="모델을 가져오는 API.",
)


# Define a route for colorization
@api.route('', endpoint='uploaded_file')
class Colorize(Resource):
    def post(self):
        image = request.files['image']
        filename = image.filename
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_url = url_for('static', filename='images/' + filename)

        idx =  request.form['idx']
        result = image_url
        
        return jsonify({'url': result})
