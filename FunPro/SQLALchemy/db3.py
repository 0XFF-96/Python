import random 
from faker import Factory

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship
