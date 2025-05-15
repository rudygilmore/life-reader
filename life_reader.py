import numpy as np
import pandas as pd
import datetime as dt
import re

dmonths={'Jan':1,'Feb':2,'March':3,'April':4,'May':5,'June':6,'July':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12,'Mar':3,'Apr':4,'Jun':6,'Jul':7}

class LifeReader:
    def __init__(self, data_type = float, impute = 0, column_name = 'data'):
        self.data_type = data_type
        self.impute = impute
        self.column_name = column_name
        
    def _read(self, filepath):
        data = []
        with open(filepath,'r') as infile:
            year = 0; month = 0; day = 0
            for line in infile:                
                line = line.strip()
                
                if '#' in line: 
                    line = line.split('#')[0]
                if len(line)<3: continue
                    
                if re.search('\d\d\d\d:',line):
                    year = int(line.split(':')[0])

                elif line.split(':')[0] in dmonths:
                    month = dmonths[line.split(':')[0]]

                elif ' - ' in line and not re.search('\d\d\d\d\d\d',line):
                    if year==0 or month==0: 
                        print('Error, month or year not properly set')
                        raise 'BadDateException'
                    day = int(line.split(' - ')[0])
                    assert day > 0 and day < 32
                    value = self.data_type(line.split(' - ')[1])
                    data.append(([year, month, day], value))
                else:
                    continue
        return data

    def _data_fill(self):
        data_df = pd.DataFrame(self.data)
        data_df = pd.DataFrame(lr.data, columns = ['dates_raw',self.column_name])
        data_df['date'] = data_df.dates_raw.apply(lambda x:dt.date(*x))
        data_df = data_df[['date', self.column_name]].sort_values('date').set_index('date')
        idx = pd.date_range(data_df.index.min(), data_df.index.max())

        if self.impute == 'intermediate':
            pass #TODO
        else:
            data_df = data_df.reindex(idx, fill_value=self.impute)

        return data_df
        

    def read(self, filepaths):
        if isinstance(filepaths, str):
            self.data = self._read(filepaths)

        elif isinstance(filepaths, list):
            self.data = []
            for filepath in filepaths:
                self.data+=(self._read(filepath))

        else:
            print('need a filename or list of filenames')

        self.data_df = self._data_fill()