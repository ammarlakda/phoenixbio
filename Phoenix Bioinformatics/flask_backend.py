from summarizer import summarizer
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/send-data', methods=['POST'])
def send_data():
    message = request.get_json().get('message')
    try:
        modified_message = summarizer(message)
    except:
        modified_message ="An error has occured but message was passed from server to client"+ summarizer(message)
    return jsonify({'message': modified_message})

if __name__ == '__main__':
    app.run(debug=True)
