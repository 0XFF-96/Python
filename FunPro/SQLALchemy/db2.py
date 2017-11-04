from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship 
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from faker import Factory
from sqlalchemy.orm import sessionmaker, relationship
import random

engine = create_engine('mysql+mysqldb://root@localhost:3306/blog')
Base = declarative_base()




article_tag = Table(
	'article_tag', Base.metadata,
	Column('article_id',Integer, ForeignKey('articles.id')),
	Column('tag_id',Integer,ForeignKey('tags.id'))
)

class Tag(Base):

	__tablename__='tags'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(64), nullable=False,index=True)

class User(Base):

	__tablename__='users'

	id = Column(Integer, primary_key=True)	

	username = Column(String(64), nullable=False, index=True)

	password = Column(String(64), nullable=False)

	email = Column(String(64), nullable=False, index=True)

	def __repr__(self):

		return '%s(%r)' %(self.__class__.__name__, self.username)


class Article(Base):

	__tablename__ = 'articles'

	id = Column(Integer, primary_key=True)

	title = Column(String(255), nullable=False, index=True)

	user_id = Column(Integer, ForeignKey('users.id'))
	
	cate_id = Column(Integer,ForeignKey('categories.id'))
	
	content = Column(Text)
	
	tags = relationship('Tag', secondary='article_tag',backref='articles')
	author = relationship('User')	

	def __repr__(self):

		return '%s(%r)' %(self.__class__.__name__, self.title)



class UserInfo(Base):

	__tablename__='userinfos'

	id = Column(Integer, primary_key = True)
	name = Column(String(64))
	qq = Column(String(11))
	phone = Column(String(11))
	link = Column(String(64))
	user_id = Column(Integer, ForeignKey('users.id'))

class Category(Base):

	__tablename__ = 'categories'

	id = Column(Integer, primary_key=True)
	name = Column(String(64),nullable=False, index=True)

	articles = relationship('Article', backref='category')

	def __repr__(self):

		return '%s(%r)' %(self.__class__.__name__, slef.name)
	


if __name__=='__main__':



	Base.metadata.create_all(engine)
	
	faker = Factory.create()
	Session = sessionmaker(bind=engine)
	session = Session()

	faker_users = [User(
				username = faker.name(),
				password=faker.word(),
				email= faker.email(),
				)for i in range(10)]
	
	session.add_all(faker_users)

	faker_categories = [Category(name=faker.word()) for i in range(5)]
	session.add_all(faker_categories)

	faker_tags = [Tag(name=faker.word()) for i in range(20)]

	session.add_all(faker_tags)

	for i in range(100):
		
		article = Article(
	
			title = faker.sentence(),
			content=''.join(faker.sentences(nb=random.randint(20,20))),
			author = random.choice(faker_users),
			category = random.choice(faker_categories)
		)

		for tag in random.sample(faker_tags, random.randint(2,5)):

			article.tags.append(tag)
		session.add(article)
	session.commit()

	
