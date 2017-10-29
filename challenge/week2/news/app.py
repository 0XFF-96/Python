from flask import Flask
from flask import  abort, redirect, url_for


app = Flask(__name__)
#app.run(port=3000)


@app.route('/')
def index():
    # show the arcticle list    
    # show all the json type file under  his fodler /files   `title`
    return "hollo world"




@app.route('/files/')
def file():
    # read filename.json  , and show the content of it 

# if filename ='helloshiyanlou'   show helloshiyanlou.json
# if filename not exist , return shiyanlou 404 page
#    return render_template('/files/file.html') 
    return "ok"

#   if filename == 'helloshiyanlou':
#        return " isOk" 

#   elif filename == 'helloworld':
#        return "is ok"

 #  else:
    #something went wrong !

#        return redirect(url_for('File_not_found_page'))



@app.errorhandler(404)
def File_not_found_page(error):
    return render_template('404.html'),404

    





if __name__=='__main__':
    app.run(DEBUG=True)


