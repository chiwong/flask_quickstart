from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'This is the index page!'

@app.route('/hello')
def hello_world():
	return 'Hello World!!'

# One example of Variable Routing, used to pass
# variables from an url into a Flask function
@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return 'User %s' % username

# Another example of Variable Routing
# This time, showing the use of an integer converter
@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id

# Let's try an example to pass two variables into a function
@app.route('/multiply/<int:x> <int:y>')
def multiply_two(x, y):
	z = x * y
	return '%d * %d = %d' % (x, y, z)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=10080)
