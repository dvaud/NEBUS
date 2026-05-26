from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_url_path='', static_folder='.')
DOWNLOAD_DIRECTORY = "downloadables"

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(DOWNLOAD_DIRECTORY, filename, as_attachment=True)

if __name__ == '__main__':
    os.makedirs(DOWNLOAD_DIRECTORY, exist_ok=True)
    app.run(debug=True, port=5000)