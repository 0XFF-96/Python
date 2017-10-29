from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/user/<username>')
def user_index(username):
    
    return 'Hello {}'.format(username)


@app.route('/post/<int:post_id>')
def user_index(username):
#get the vairable
    return 'Hello {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    
    return 'Post {}'.format(post_id)

from flask import render_template

@app.route('/user/<username>')
def user_index(username):
    return_template('user_index.html',username=username)


from flask import make_response

@app.route('/user/<username>')
def user_index(username):

    resp = make_response(render_template('user_index.html', username=username))
    resp.set_cookie('username',username)

    return resp 


from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')

    return 'Hello {}'.format(username)


@app.errorhander(404)
def not_found(error):
    return render_template('404.html'), 404



if __name__=='__main__':
    app.run()


