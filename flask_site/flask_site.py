from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('error.html',error=error)


@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/instructable')
def instructable():
    return render_template('instructable.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
