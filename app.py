from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/like', methods=['POST'])
def like():
    uid = request.form.get('uid')

    if not uid:
        return jsonify({'error': 'UID is required'})

    # Prepare the API request URL
    api_url = f'api here' # your ff like api

    try:
        response = requests.get(api_url)
        response_data = response.json()
        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
