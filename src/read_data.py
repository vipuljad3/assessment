
## Importing pandas and Numpy as required libraries for data analytics and processing.
import pandas as pd
import numpy as np

## Reads file lines and returns
def read_file(directory,filename):
    with open(f'{directory}/{filename}') as f:
        lines = f.readlines()
    return lines

## Processes Read lines and returns a parsed list of structured data
def process_input(lines):
    return [line.rstrip().split(' ') for line in lines]


## Convert the structured data to a pandas dataframe and define column datatypes
def convert_dataframe(data, timestamp_col, count_col):
    df = pd.DataFrame(list(zip([line[0] for line in data],[line[1] for line in data])), columns=[timestamp_col, count_col])
    df[timestamp_col] = pd.to_datetime(df[timestamp_col])
    df[count_col] = df[count_col].astype('int') 
    return df

### Ideally used to perform tests on test data where there are missing timestamp values, Assuming that the missing timestamp counts are 0.
def fill_missing_times(df, timestamp_col, count_col):
    df['times'] = df[timestamp_col]
    dates  = list(set(pd.to_datetime(df[timestamp_col]).dt.date))
    start = pd.to_datetime(str(df['times'].min()))
    end = pd.to_datetime(str(df['times'].max()))
    time_list = pd.date_range(start=start, end=end, freq='30Min')
    df = df.set_index('times')\
            .reindex(time_list)\
                    .reset_index()[['index', count_col]]\
                            .rename(columns = {'index':timestamp_col})
    
    cols = df.columns.difference([count_col])
    df[cols] = df[cols].ffill()
    
    df = df[(pd.to_datetime(df[timestamp_col]).dt.date).isin(dates)]\
            .reset_index()\
                [[timestamp_col, count_col]].fillna(0)
    return df


