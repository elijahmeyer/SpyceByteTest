from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'Spahgetti'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'Your mom goes to college!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
