from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Race, Result, Jockey, Horse, Trainer

engine = create_engine('sqlite:///db.sqlite3', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class RaceModel:
    def __init__(self, date):
        self.date = date
        self.course
        self.class_code
        self.turf_or_dirt
        self.distance
        self.state
        self.weather
        self.total_horse_number
        self.horses


class HorseModel:
    def __init__(self, number):
        self.number = number
        self.post_position
        self.sire
        self.broodmare_sire
        self.odds_of_win
        self.jockey_code
        self.jockey_weight

class Result:
    def __init__(self):
        self.first
        self.second
        self.third
