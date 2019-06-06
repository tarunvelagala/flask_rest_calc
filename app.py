from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'say': 'Hello'})


@app.route('/add/<int:num1>+<int:num2>', methods=["GET"])
def addNumbers(num1, num2):
    return jsonify({'result': num1+num2})


@app.route('/sub/<int:num1>-<int:num2>', methods=["GET"])
def subtractNumbers(num1, num2):
    return jsonify({'result': num1 - num2})


@app.route('/mul/<int:num1>*<int:num2>', methods=["GET"])
def multiplyNumbers(num1, num2):
    return jsonify({'result': num1 * num2})


@app.route('/sub/<int:num1>/<int:num2>', methods=["GET"])
def divideNumbers(num1, num2):
    return jsonify({'result': int(num1 / num2)})


if __name__ == "__main__":
    app.run(debug=True)
