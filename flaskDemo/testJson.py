import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
app = Flask(__name__)

@app.route('/<path:name>' , methods=['GET', 'POST'])
def index(name):
    if request.method == 'POST':
        a = request.get_data()
        print('req:{}'.format(a))
        dict1 = json.loads(a)
        return json.dumps(dict1["data"])
    else:
        return '<h1>只接受post请求-{}！</h1>'.format(name)

@app.route('/user/<name>')
def user(name):
    return'<h1>hello, %s</h1>' % name

if __name__ =='__main__':
    app.run(debug=True)
'''
请求数据为{
    "opr": "add",
    "data": {
        "userName": "98997",
        "disc": "hudihiudhu",
        "expDate":"2",
        "ip": [
            "10.10.11.1",
            "10.10.11.2",
            "10.10.11.3"
        ]
    }
}
返回{"userName": "98997", 
"ip": ["10.10.11.1", "10.10.11.2", "10.10.11.3"],
"disc": "hudihiudhu", "expDate": "2"} 
'''
