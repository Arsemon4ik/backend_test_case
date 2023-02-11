from flask import Flask, request, jsonify
from routine import json, file_exists, ClientError

app = Flask(__name__)


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
        if file_exists(key):
            return jsonify({f"Key {key} is already in DB!": True}), 400

        encoded_value = str(value.encode('utf-8'))
        json.dump_s3(encoded_value, key+'.json')
        return jsonify({encoded_value: True}), 201

    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return jsonify({f"Key does not exist!: {key}": True})
        else:
            jsonify({f"Unexpected error: {e}": True}), 400
    except Exception as e:
        return jsonify({f"An error occurred: {e}": True}), 400


@app.route('/list/<string:key>', methods=['GET'])
def get(key):
    """Функція для зчитування даних по ключу"""
    try:
        if not key:
            return jsonify({f'Key {key} does not exist!': True}), 404
        binary_value = json.load_s3(key+'.json')
        return jsonify({binary_value: True}), 200

    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return jsonify({f"Key does not exist!: {key}": True}), 404
        else:
            print("Unexpected error: %s" % e)
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
        if not file_exists(key):
            return jsonify({f"No such key {key} in DB to update!": True}), 404

        json.dump_s3(new_value, key+'.json')
        return jsonify({new_value: True}), 200

    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return jsonify({f"Key does not exist!": True})
        else:
            jsonify({f"Unexpected error: {e}": True}), 400

    except Exception as e:
        return jsonify({f"An error occurred: {e}": True}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)