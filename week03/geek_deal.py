#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:My
@file:geek_deal.py
@time:2020/12/14
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, create_engine, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User_table(Base):
    __tablename__ = 'user'
    uid = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(15), nullable=True, unique=True)


class Asset_table(Base):
    __tablename__ = 'asset'
    uid = Column(Integer(), primary_key=True, nullable=True)
    asset = Column(DECIMAL(19, 4), nullable=True)


class Record_tabl(Base):
    __tablename__ = 'record'
    one_id = Column(Integer(), primary_key=True)
    other_id = Column(Integer(), primary_key=True)
    deal = Column(DECIMAL(19, 4), nullable=True)
    create_date = Column(DateTime(), nullable=True)



def deal(one, other, deal, session):
    one_id = session.query(User_table.uid).filter(User_table.name == one).one()[0]
    other_id = session.query(User_table.uid).filter(User_table.name == other).one()[0]
    one_mon = session.query(Asset_table.asset).filter(Asset_table.uid == one_id, Asset_table.asset > deal).one()[0]
    other_mon = session.query(Asset_table.asset).filter(Asset_table.uid == other_id).one()[0]

    one_mon -= deal
    other_mon += deal
    session.query(Asset_table.asset).filter(Asset_table.uid == one_id).update({Asset_table.asset: one_mon})
    session.query(Asset_table.asset).filter(Asset_table.uid == other_id).update({Asset_table.asset: other_mon})

    record = Record_tabl(one_id=one_id,
                         other_id=other_id,
                         create_date=datetime.now(),
                         deal=deal)
    session.add(record)


if __name__ == '__main__':
    dburl = "mysql+pymysql://testuser:testpass@localhost:3306/testdb?charset=utf8mb4"
    engine = create_engine(dburl, echo=True, encoding='utf-8')
    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()
    Base.metadata.create_all(engine)

    try:
        deal('张三', '李四', 100, session)
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.commit()
