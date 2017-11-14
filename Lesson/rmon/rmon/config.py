""" rmon.config

"""
import os

class DevConfig:
    """
    """

    DEBUG = True
    SQLALCHEMY_TRACK-MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TEMPLATES_AUTO_RELOAD = True

class ProductConfig(DecConfig):

    """ 
    """

    DEBUG = False

    # sqlite 
    path =os.path.join(os.getcwd(), 'rmon.db').replace('\\','/')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' %path

    
