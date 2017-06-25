from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from models import Race, Result, Jockey, Horse, Trainer


class RaceModel:
    def __init__(self, month, course, class_code, turf_or_dirt, state, distance, weather, total_horse_number, horses):
        self.month = month
        self.course = course
        self.class_code = class_code
        self.turf_or_dirt = turf_or_dirt
        self.distance = distance
        self.state = state
        self.weather = weather
        self.total_horse_number = total_horse_number
        self.horses = horses


class HorseModel:
    def __init__(self, number, post_position, sire, broodmare_sire, odds_of_win, jockey_code, jockey_weight):
        self.number = number
        self.post_position = post_position
        self.sire = sire
        self.broodmare_sire = broodmare_sire
        self.odds_of_win = odds_of_win
        self.jockey_code = jockey_code
        self.jockey_weight = jockey_weight


class ResultModel:
    def __init__(self, orders_of_finish):
        self.orders_of_finish = orders_of_finish


def load_data():
    engine = create_engine('sqlite:///db.sqlite3', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    races = session.query(Race).\
        limit(100).\
        all()
    for r in races:
        print(str(r.date) + ' ' + r.course + str(r.number) + 'R')
        for res in r.results:
            print(('%02d: ' % res.number) + res.horse.name + "    " + str(res.order_of_finish) + '着')
        print('')


load_data()
