from flask import Flask
app = Flask(__name__)
#app.run(port=3000)


@app.route('/')
def index():
    # show the arcticle list    
    # show all the json type file under  his fodler /files   `title`
    return 'Heloo world'   




@app.route('/files/<filename>')
def file(filename):
    # read filename.json  , and show the content of it 

# if filename ='helloshiyanlou'   show helloshiyanlou.json
# if filename not exist , return shiyanlou 404 page
    pass
@app.errorhandler(404)
def File_not_found_page(error):
    return render_template('404.html'),404

    pass


if __name__=='__main__':
    app.run(DEBUG=True)


