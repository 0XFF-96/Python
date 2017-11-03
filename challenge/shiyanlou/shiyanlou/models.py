from sqlchemy import create_engine
from sqlchemy.ext.declarative import declarative_base
from sqlchemy import Column, Integer, String, DataTime

engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlougithub?charset=utf8')

Base = declarative_base()

class Repository(Base):

    __tablename__='respositories'
    id = Column(integer, primary_key=True)
    name = Column(String(64))
    update_time = Column(DataTime)

if __name__=='__main__':
    Base.metadata.create_all(engine)


