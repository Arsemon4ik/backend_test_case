from flask import Flask, request, jsonify
import redis

from config import USERNAME, PASSWORD

app = Flask(__name__)

# Я обрав Redis тому, що на мою думку він дуже підходить під завдання.
# Це NoSql база даних тобто (key, value) - те, що нам і потрібно.
db = redis.Redis.from_url(url=f'redis://{USERNAME}:{PASSWORD}@redis-19255.c16.us-east-1-2.ec2.cloud.redislabs.com:19255')


@app.route('/add', methods=['POST'])
def post():
    """
    функція для відправлення ПОСТ запиту
    наприклад {'key': '1', 'value': 'value1'}
    """
    try:
        key = request.json.get('key', None)
        value = request.json.get('value', None)
        if not all([key, value]):
            return jsonify({"Key and value are mandatory!": True}), 400
        if db.exists(key):
            return jsonify({f"Key {key} is already in DB!": True}), 400

        encoded_value = value.encode('utf-8')
        db.set(key, encoded_value)
        return jsonify({encoded_value: True}), 201

    except Exception as e:
        return jsonify({f"An error occurred: {e}": True})


@app.route('/list/<int:key>', methods=['GET'])
def get(key):
    """функція для зчитування даних по ключу"""
    try:
        if not key or db.exists(key) == 0:
            return jsonify({f'Key {key} does not exist!': True}), 404

        value = db.get(key).decode('utf-8')
        return jsonify({value: True}), 200

    except Exception as e:
        return jsonify({f"An error occurred: {e}": True}), 400


@app.route('/update', methods=['PUT'])
def put():
    """
    функція для редагування даних
    наприклад {'key': 1, 'value': 'new value1'}
    """
    try:
        key = request.json['key']
        new_value = request.json['value']

        if not all([key, new_value]):
            return jsonify({"Key and new value are mandatory!": True}), 400
        if db.exists(key) == 0:
            return jsonify({f'Key {key} does not exist!': True}), 404

        encoded_value = new_value.encode('utf-8')
        db.set(key, encoded_value)
        return jsonify({encoded_value: True}), 200

    except Exception as e:
        return jsonify({f"An error occurred: {e}": True}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)