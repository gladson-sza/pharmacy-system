from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(80))
    password = Column(String(30))
    name = Column(String(60))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


class Medicine(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)
    has_recipe = Column(Boolean, default=False)

    def __init__(self, name, quantity, price, has_recipe):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.has_recipe = has_recipe
