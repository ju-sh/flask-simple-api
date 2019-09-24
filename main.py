from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return f"{a+b}"

@app.route('/sub', methods=['GET', 'POST'])
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return f"{a-b}"

@app.route('/mult', methods=['GET', 'POST'])
def mult():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return f"{a*b}"

@app.route('/div', methods=['GET', 'POST'])
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if b==0:
        return "Error: Cannot divide by zero"
    return f"{a/b}"
