from flask import Flask, abort,render_template,  redirect,url_for
import os


app = Flask(__name__)


@app.route('/')
def index():
    # show the list of the article
    # show all the information  behind /home/shiyanlou/files 
    #OS. path....

    #read the folder 
    path = 'files/'





@app.route('/files/<filename>')
def file(filename):
    # read filename.json content

    pass


#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'),404


if __name__ == '__main__':
    app.run(debug=True)
