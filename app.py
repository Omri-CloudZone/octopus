#!flask/bin/python
from flask import Flask, request, request_started
app = Flask(__name__)
counter = 0
@app.route('/', methods=["POST", "GET"])
def post():
    global counter
    if request.method == "POST":
        counter+=1
        return "Hmm, Plus 1 please "
    else:
        return str(f"The counter isssssssssss: {counter} ")
if __name__ == '__main__':
    app.run(debug=True,threaded=True,host='0.0.0.0',port=443)