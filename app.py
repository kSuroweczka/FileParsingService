from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import time
import os
from process_file_format import process_csv, process_json, process_txt

app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Application Request Latency',
    ['method', 'endpoint']
)

def process_file(file):
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    if filename.endswith('.csv'):
        return process_csv(file_path)
    elif filename.endswith('.json'):
        return process_json(file_path)
    elif filename.endswith('.txt'):
        return process_txt(file_path)
    else:
        return "Unsupported file format"

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    start_time = time.time()
    file = request.files['file']
    response = process_file(file)
    REQUEST_COUNT.labels('POST', '/upload', 200).inc()
    REQUEST_LATENCY.labels('POST', '/upload').observe(time.time() - start_time)
    # return jsonify(response)  ## If you want to return response as JSON

    return render_template('summary.html', response=response)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=5000)