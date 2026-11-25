import os
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Ensure captures directory exists
captures_dir = os.path.join(os.path.dirname(__file__), 'captures')
os.makedirs(captures_dir, exist_ok=True)

@app.route('/save', methods=['GET','POST'])
def save_image():
    if request.method == 'GET':
        return jsonify({'status':'ready'})
    data_url = request.json.get('data')
    if not data_url:
        return jsonify({'error':'No data'}),400
    # Data URL format: data:image/png;base64,XXXXX
    header, encoded = data_url.split(',',1)
    import base64, datetime
    img_bytes = base64.b64decode(encoded)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    filename = f'capture_{timestamp}.png'
    filepath = os.path.join(captures_dir, filename)
    with open(filepath,'wb') as f:
        f.write(img_bytes)
    return jsonify({'saved':filename})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
