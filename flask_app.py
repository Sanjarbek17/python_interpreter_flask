import subprocess
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/getME')
@cross_origin()
def start():
    print('hello')
    return 'Hello World!'


@app.route('/', methods=['POST'])
@cross_origin()
def main():
    try:
        code = request.get_json()['code']
        output = subprocess.run(["python", '-c', code], text=True, capture_output=True, check=True)
    except Exception as e:
        print(e)
        return e.stderr
    print(output.stdout)
    return output.stdout