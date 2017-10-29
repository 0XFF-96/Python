from flask import Flask, render_template
from flask import abort, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():

	return "holl"

@app.route('/login')
def login():
	
	abort(401)
	this_is_never_executed()

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'),404

#	resp = make_response(render_template('error.html'),404)
#	resp.headers['X-something'] = 'A value'
#	return resp	

@app.route('/shiyanlou')
def hello():
	
	return "jhi"





@app.route('/user/<username>')
def show_user_profile(username):

	#show user's name

	return 'User %s' %username

@app.route('/post/<int:post_id>')
def show_post(post_id):

	#show user , string  transform to int ..

	return 'Post %d ' %post_id


@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about')
def about():
	return 'THe about page'



#@app.route('/login',methods=['GET','POST'])
#def login():
#
#	if request.method == 'POST':
#
#		do_the_login()
#
#	else:
#		show_the_login_form()


	
#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello(name=None):

#	return render_template('hello.html', name=name)










if __name__ == '__main__':

	app.run(debug=True)



