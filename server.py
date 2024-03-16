from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
import random


app = Flask(__name__)
CORS(app)
# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

from flask_cors import cross_origin

@app.route('/forecast', methods=['POST'])
@cross_origin()
def forecast():
    if 'csvFile' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['csvFile']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        algorithm = request.form.get('algorithm', 'ARIMA') # Default to ARIMA if algorithm is not specified

        # Here, you would implement your forecasting logic using the uploaded file and chosen algorithm
        # Replace this with your actual forecasting code

        result = {
            'filename': filename,
            'algorithm': algorithm,
            'data': [[random.uniform(0, 10) for _ in range(20)] for _ in range(3)],
            'message': 'Forecasting completed successfully'
        }
        return jsonify(result), 200
    else:
        return jsonify({'error': 'File format not supported'}), 400

if __name__ == '__main__':
    app.run(port=8888)  # Remove debug=True in production
