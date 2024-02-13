from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # HTML file with input form

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    print("Received text:", text)

    function_url = os.environ.get('FUNCTION_URL')
    if not function_url:
        return jsonify({'error': 'Function URL is not configured'})

    # Trigger the Azure Function
    response = requests.post(function_url, json={'text': text})
    if response.status_code != 202:
        return jsonify({'error': 'Failed to start the analysis'})

    # Get the status query URL
    status_query_url = response.headers['Location']

    # Poll the status endpoint
    while True:
        status_response = requests.get(status_query_url)
        status_response_json = status_response.json()

        if status_response_json['runtimeStatus'] in ['Completed']:
            # The result should be directly in the output
            results = status_response_json.get('output', [])
            return jsonify({'results': results})
        elif status_response_json['runtimeStatus'] in ['Failed', 'Terminated']:
            return jsonify({'error': 'Analysis failed or terminated'})
        # Implement a delay here if necessary

if __name__ == '__main__':
    app.run(debug=True)
