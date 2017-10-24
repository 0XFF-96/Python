app = Flask=(__name__)
app.config.update({
    'SECRET_KEY':'a random string'
    })

app.config.from_pyfile('path/to/config.py')


