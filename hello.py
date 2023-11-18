from flask import *
# constrcutor
app = Flask(__name__)

# this route executes te function
# gauge like parameter settings
@app.route('/welcome/<name>')
def welcome(name):
    return f'Hello, {name}!'

# route names must match function name or build will fail
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('welcome', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('welcome', name=user))

if __name__ == '__main__':
    app.run(debug=True)
