import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://hw1:password@database:5432/mydb')

Engine = create_engine(
    DATABASE_URL,
    connect_args={"connect_timeout": 10},
    pool_pre_ping=True
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
BaseClass = declarative_base()
