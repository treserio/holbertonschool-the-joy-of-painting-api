import json
import pandas as pd
import re
from datetime import datetime
from sqlalchemy import create_engine
# bob_ross database must be setup first before this will run
engine = create_engine('mysql://root@localhost:3306/bob_ross')

colorsUsed = pd.read_csv('./TJOP - Colors Used')
subjectMatter = pd.read_csv('./TJOP - Subject Matter')

print(subjectMatter)
print(type(subjectMatter))
print(subjectMatter.__dict__)

episodeDates = [re.findall(r'[\w\s]\(([\d\w,\s]+)\)[$ ]?', line)[0] for line in open('TJOP - Episode Dates')]
print(episodeDates)

dtObjs = [datetime.strptime(date, '%B %d, %Y') for date in episodeDates]

df = pd.DataFrame()
df['air_date'] = dtObjs

stuff = pd.concat([colorsUsed, df], axis=1)
print(stuff)

stuff.to_sql('pic_info', con=engine)

# push dataframe to mysql
