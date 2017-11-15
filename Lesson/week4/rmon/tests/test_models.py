
from rmon.models import Server

class TestServer:

    def test_save(self, db):

        assert Server.query.count() ==0 
        
        server = Server(name='test', host='127.0.0.1')

        server.save()
        assert Server.query.count() ==1

        assert Server.query.first() == server 

    def test_delete(self, db, server):

        assert Server.query.count() == 1
        server.delete()

        assert Server.query.count() == 0


