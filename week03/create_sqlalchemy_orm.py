#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:My
@file:create_sqlalchemy_orm.py
@time:2020/12/13
"""

from datetime import datetime
from sqlalchemy import DateTime
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
class student_table(Base):
    __tablename__ = 'student'
    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String(50), index=True)
    age = Column(Integer(), nullable=False)
    birthday = Column(DateTime())
    sex = Column(String(2), nullable=False)
    edu = Column(String(50), nullable=False)
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


dburl = "mysql+pymysql://testuser:testpass@localhost:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

SessionClass = sessionmaker(bind=engine)
session = SessionClass()
# Base.metadata.create_all(engine)

for result in session.query(student_table).filter(student_table.user_name == 'Scott').all():
    print(result)
session.commit()
