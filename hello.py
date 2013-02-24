from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'This is the index page!'

@app.route('/hello')
def hello_world():
	return 'Hello World!!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=10080)
