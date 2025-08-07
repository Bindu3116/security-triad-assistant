from flask import Flask, request, jsonify
from alert_processor import process_alert

app = Flask(__name__)

@app.route('/triage', methods=['POST'])
def triage():
    alert = request.get_json()
    if not alert:
        return jsonify({'error': 'Invalid alert format'}), 400

    result = process_alert(alert)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
