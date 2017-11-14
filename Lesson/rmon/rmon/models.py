"""rmon.model

"""

from flask_sqlalchemy import SQLALchemy
from datetime import datetime

db = SQLAchemy()

class Server(db.Model):
    """
    """

    __tablename__ = 'redis_server'

    id = db.Column(db.Integer, primary_key=True)

#unique = True 

    name = db.Column(db.string(64), unique=True)
    description =db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer, default=6379)
    password = db.Column(db.String())
    update_at = db.Column(db.DataTime, default=datetime.utcnow)
    create_at = db.Column(db.DateTime, default=datetime.utcnoe)

    def __repr__(self):
        return '<Server(name=%s)>' %self.name 

    def save(self):

        """
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        
        """
        """
        db.session.delete(self)
        db.session.commit()

