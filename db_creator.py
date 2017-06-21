import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Race, Result, Jockey, Horse, Trainer, Base

names = ('Year', 'Month', 'Day', 'Course', 'RaceNumber', 'ClassCode', 'GradeCode', 'TurfOrDirt', 'TrackCode',
         'TrackCodeJV', 'CornerNumber', 'Distance', 'CourseDivision', 'State', 'Weather', 'TotalHorseNumber',
         'AgeLimitationCode', 'RaceSymbolCode', 'WeightCode', 'RaceIDOld', 'RaceID', 'HorseNumber', 'PostPosition',
         'Name', 'Gender', 'Age', 'Jockey', 'Weight', 'Blinker', 'OfficialOrderOfFinish', 'OrderOfFinish', 'ErrorCode',
         'Margin', 'OrderOfFavorite', 'OddsOfWin', 'TimeOfSeconds', 'OrderOf1stCorner', 'OrderOf2ndCorner',
         'OrderOf3rdCorner', 'OrderOf4thCorner', 'RunningStyle', 'Last3FurlongTime', 'Last3FurlongOrder',
         'Average3FurlongTime', 'HorseWeight', 'HorseWeightDelta', 'Trainer', 'BloodRegistrationID', 'JockeyCode',
         'TrainerCode', 'Producer', 'Sire', 'Broodmare', 'BroodmareSire', 'BirthDate')

df = pd.read_csv('~/Desktop/results_test.csv', names=names)

engine = create_engine('sqlite:///db.sqlite3', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for index, row in df.iterrows():
    race_id = str(row['RaceID'])[:16]
    race_count = session.query(Race).filter(Race.id == race_id).count()
    if race_count == 0:
        race = Race(id=race_id, year=row['Year'], month=row['Month'], day=row['Day'], course=row['Course'],
                    number=row['RaceNumber'], class_code=row['ClassCode'], grade_code=row['GradeCode'],
                    turf_or_dirt=row['TurfOrDirt'], track_code_jv=row['TrackCodeJV'], corner_number=row['CornerNumber'],
                    distance=row['Distance'], course_division=row['CourseDivision'], state=row['State'],
                    weather=row['Weather'], total_horse_number=row['TotalHorseNumber'],
                    age_limitation_code=row['AgeLimitationCode'], symbol_code=row['RaceSymbolCode'],
                    weight_code=row['WeightCode'])
        session.add(race)

    horse_id = row['BloodRegistrationID']
    horse_count = session.query(Horse).filter(Horse.id == horse_id).count()
    if horse_count == 0:
        horse = Horse(id=horse_id, name=row['Name'], gender=row['Gender'],
                      trainer_code=row['TrainerCode'], producer=row['Producer'], sire=row['Sire'],
                      broodmare_sire=row['BroodmareSire'])
        session.add(horse)

    jockey_code = str(row['JockeyCode'])
    jockey_count = session.query(Jockey).filter(Jockey.code == jockey_code).count()
    if jockey_count == 0:
        jockey = Jockey(code=str(row['JockeyCode']), name=row['Jockey'])
        session.add(jockey)

    trainer_code = str(row['TrainerCode'])
    trainer_count = session.query(Trainer).filter(Trainer.code == trainer_code).count()
    if trainer_count == 0:
        trainer = Trainer(code=trainer_code, name=row['Trainer'])
        session.add(trainer)

    print(row['Average3FurlongTime'])
    result_id = row['RaceID']
    result_count = session.query(Result).filter(Result.id == result_id).count()
    if result_count == 0:
        margin = -1.0 if row['Margin'] == '----' else row['Margin']
        result = Result(id=result_id, race_id=race_id, number=row['HorseNumber'], post_position=row['PostPosition'],
                        horse_id=horse_id, age=row['Age'], jockey_code=row['JockeyCode'], jockey_weight=row['Weight'],
                        blinker=row['Blinker'], order_of_finish=row['OrderOfFinish'], margin=margin,
                        order_of_favorite=row['OrderOfFavorite'], odds_of_win=row['OddsOfWin'], time=row['TimeOfSeconds'],
                        order_of_1st_corner=row['OrderOf1stCorner'], order_of_2nd_corner=row['OrderOf2ndCorner'],
                        order_of_3rd_corner=row['OrderOf3rdCorner'], order_of_4th_corner=row['OrderOf4thCorner'],
                        running_style=row['RunningStyle'], last_3furlong_time=row['Last3FurlongTime'],
                        last_3furlong_order=row['Last3FurlongOrder'], average_3furlong_time=row['Average3FurlongTime'],
                        horse_weight=row['HorseWeight'], horse_weight_delta=row['HorseWeightDelta'])
        session.add(result)

    session.commit()
