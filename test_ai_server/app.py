from flask import Flask, request, jsonify
from flask_restx import Api, Resource #flask restful
from flask_cors import CORS
from resources.post_image import api as post_namespace
import os

app = Flask(__name__)
CORS(app)
api = Api(
    app,
    version = '0.1',
    title = "Colorful World deep learing Server",
    terms_url = "/"
    )

app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'images')

@app.route('/')
def index():
    app.logger.info('Web connection established.')
    return 'Hello, World!'

api.add_namespace(post_namespace, path="/colorization")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5100, debug=True)