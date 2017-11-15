import pytest 
from rmon.app import create_app
from rmon.models import Server 
from rmon.models import db as database

@pytest.fixture 
def app():
    """ Flask app
    """

    return create_app()

@pytest.yield_fixture
def db(app):
    """database
    """

    with app.app_context():
        database.create_all()
        yield db 
        database.drop_all()

@pytest.fixture
def server(db):
    """ test the service record
    """

    server = Server(name='redis_test', description='this is a test record',
            host='123.0.0.1', port='6379')

    server.save()
    return server 
