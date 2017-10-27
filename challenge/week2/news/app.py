from flask import Flask
app = Flask(__name__)
app.run(port=3306)


@app.route('/')
def index():
    # show the arcticle list    
    # show all the json type file under  this fodler /files   `title`
    return 'Heloo world'   


@app.route('/files/<filename>')
def file(filename):
    # read filename.json  , and show the content of it 

# if filename ='helloshiyanlou'   show helloshiyanlou.json
# if filename not exist , return shiyanlou 404 page
    pass
@app.route('/404')
def File_not_found_page():

    pass


if __name__=='__main__':
    app.run(DEBUG=True)


