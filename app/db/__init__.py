from typing import Any
from flask_sqlalchemy import SQLAlchemy 
import datetime
# from flask_sqlalchemy import Base, Integer,Column, VARCHAR

import time
conn = SQLAlchemy()
# conn.init_app(app.appl.get_app) # инициализирцем БД для приложения 
"""
БД вынесено в отдельный файл для декомпозиции моделей
"""





# class Users(BaseModel):
#     __tablename__ = 'users'

#     first_name = Column(VARCHAR(255), nullable=False)
#     last_name = Column(VARCHAR(255), nullable=False)
#     login = Column(VARCHAR(255), unique=True, nullable=True)
#     password = Column(VARCHAR(255), nullable=True)