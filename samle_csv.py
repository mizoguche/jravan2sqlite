import pandas as pd

names = ('Year', 'Month', 'Day', 'Course', 'RaceNumber', 'ClassCode', 'GradeCode', 'TurfOrDirt', 'TrackCode',
         'TrackCodeJV', 'CornerNumber', 'Distance', 'CourseDivision', 'State', 'Weather', 'TotalHorseNumber',
         'AgeLimitationCode', 'RaceSymbolCode', 'WeightCode', 'RaceIDOld', 'RaceID', 'HorseNumber', 'PostPosition',
         'Name', 'Gender', 'Age', 'Jockey', 'Weight', 'Blinker', 'OfficialOrderOfFinish', 'OrderOfFinish', 'ErrorCode',
         'Margin', 'OrderOfFavorite', 'OddsOfWin', 'TimeOfSeconds', 'OrderOf1stCorner', 'OrderOf2ndCorner',
         'OrderOf3rdCorner', 'OrderOf4thCorner', 'RunningStyle', 'Last3FurlongTime', 'Last3FurlongOrder',
         'Average3FurlongTime', 'HorseWeight', 'HorseWeightDelta', 'Trainer', 'BloodRegistrationID', 'JockeyCode',
         'TrainerCode', 'Producer', 'Sire', 'Broodmare', 'BroodmareSire', 'BirthDate')

df = pd.read_csv('~/Desktop/results_test.csv', names=names)

for index, row in df.iterrows():
    print(row['Year'] + 2000, row['Month'], row['Day'], row['Course'], row['RaceNumber'], row['RaceID'], row['Name'], row['PostPosition'], row['OrderOfFinish'])
