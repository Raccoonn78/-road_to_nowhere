from typing import Any
from flask_sqlalchemy import SQLAlchemy 
import datetime
# from flask_sqlalchemy import Base, Integer,Column, VARCHAR
from db import conn
import time


class BaseModel(conn.Model):
    __abstract__ = True
    TIMESTAMP=datetime.datetime.today().strftime('%Y-%m-%d  %H:%M:%S')
    id = conn.Column(conn.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    created_at = conn.Column(TIMESTAMP, nullable=False)
    updated_at = conn.Column(TIMESTAMP, nullable=False)


    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
    
    @staticmethod
    def get_all_tables():
        print(f"{conn.metadata.tables.keys()}")
        return conn.metadata.tables.keys()
