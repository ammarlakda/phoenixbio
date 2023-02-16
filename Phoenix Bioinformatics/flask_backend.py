from split_article import split_article
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/send-data', methods=['POST'])
def send_data():
    message = request.get_json().get('message')
    modified_message = split_article(message)
    return jsonify({'message': modified_message})

if __name__ == '__main__':
    app.run(debug=True)
