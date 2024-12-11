import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/temperature', methods=['GET'])
def get_temperature():
    # Generate a random temperature between -10°C and 40°C
    temperature = round(random.uniform(-10, 40), 2)
    return jsonify({"temperature": temperature})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
