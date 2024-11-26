from datetime import datetime, timezone
from .db import BaseClass
from sqlalchemy import Column, Integer, String, Float, DateTime

class Users(BaseClass):
    __tablename__ = 'users'
    email = Column(String, primary_key=True, unique=True, index=True)
    ticker = Column(String)

class FinancialData(BaseClass):
    __tablename__ = 'fydata'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ticker = Column(String)
    value = Column(Float)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))