# Python program to use flask
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/sum',methods=['POST'])

def sum():
    data = request.get_json()
    a = data.get('a',0)
    b = data.get('b',0)
    result = a+b
    return jsonify({"a":a,"b":b,"sum":result})

@app.route('/testing',methods=['GET'])
def testing():
    error = None
    if request.method == 'GET':
        return "Testing flask application !"

if __name__ =="__main__":
    app.run(debug=True)