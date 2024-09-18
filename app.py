from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os
import logging
from roboflow import Roboflow
from inference_sdk import InferenceHTTPClient
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'Static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi'}
api_key = "BmMMnG8NTZJK8ATR3dfh"
rf = Roboflow(api_key=api_key)
project = rf.workspace("construction-goods-counter-akffd").project("material-counter")
image_model_version = project.version(17)
video_model_version = project.version(15)
logging.basicConfig(level=logging.DEBUG)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Perform image inference
        try:
            CLIENT = InferenceHTTPClient(
                api_url="https://detect.roboflow.com",
                api_key=api_key
            )
            result = CLIENT.infer(filepath, model_id="material-counter/17")
            logging.debug(f"Inference result: {result}")
            return render_template('result.html', result=result, filename=filename)
        except Exception as e:
            logging.error(f"Error during image inference: {e}")
            return redirect(url_for('index'))
    return redirect(request.url)

@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Perform video inference
        try:
            job_id, signed_url, expire_time = video_model_version.predict_video(
                filepath,
                fps=5,
                prediction_type="batch-video",
            )
            results = video_model_version.poll_until_video_results(job_id)
            logging.debug(f"Video inference results: {results}")
            return render_template('result.html', result=results, filename=filename)
        except Exception as e:
            logging.error(f"Error during video inference: {e}")
            return redirect(url_for('index'))
    return redirect(request.url)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
