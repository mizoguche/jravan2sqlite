from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Race(Base):
    __tablename__ = 'races'

    id = Column(String, primary_key=True)
    date = Column(Date, nullable=False)
    course = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    class_code = Column(Integer, nullable=False)
    grade_code = Column(Integer, nullable=True)
    turf_or_dirt = Column(String, nullable=False)
    track_code_jv = Column(Integer, nullable=False)
    corner_number = Column(Integer)
    distance = Column(Integer, nullable=False)
    course_division = Column(String, nullable=True)
    state = Column(String, nullable=False)
    weather = Column(String, nullable=False)
    total_horse_number = Column(Integer, nullable=False)
    age_limitation_code = Column(String, nullable=False)
    symbol_code = Column(String, nullable=False)
    weight_code = Column(String, nullable=False)
    results = relationship('Result', lazy='joined')


class Result(Base):
    __tablename__ = 'results'

    id = Column(String, primary_key=True)
    race_id = Column(Integer, ForeignKey('races.id'), nullable=False)
    number = Column(Integer, nullable=False)
    post_position = Column(Integer, nullable=False)
    horse_id = Column(String, ForeignKey('horses.id'), nullable=False)
    age = Column(Integer, nullable=False)
    jockey_code = Column(String, nullable=False)
    jockey_weight = Column(Float, nullable=False)
    blinker = Column(Integer, nullable=True)
    order_of_finish = Column(Integer, nullable=False)
    margin = Column(Float, nullable=False)
    order_of_favorite = Column(Integer)
    odds_of_win = Column(Float)
    time = Column(Float, nullable=False)
    order_of_1st_corner = Column(Integer)
    order_of_2nd_corner = Column(Integer)
    order_of_3rd_corner = Column(Integer)
    order_of_4th_corner = Column(Integer)
    running_style = Column(String)
    last_3furlong_time = Column(Float)
    last_3furlong_order = Column(Integer)
    average_3furlong_time = Column(Float)
    horse_weight = Column(Integer)
    horse_weight_delta = Column(Integer)
    horse = relationship('Horse', lazy='joined')


class Horse(Base):
    __tablename__ = 'horses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    trainer_code = Column(Integer, nullable=False)
    producer = Column(String, nullable=False)
    sire = Column(String, nullable=False)
    broodmare_sire = Column(String, nullable=False)
    results = relationship('Result')


class Jockey(Base):
    __tablename__ = 'jockeys'

    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)


class Trainer(Base):
    __tablename__ = 'trainers'

    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)
