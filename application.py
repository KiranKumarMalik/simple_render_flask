from flask import Flask, render_template

FAI = Flask(__name__)

@FAI.route('/index')
def index():
    return "Hello, Kiran"

@FAI.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    FAI.run(debug=True)