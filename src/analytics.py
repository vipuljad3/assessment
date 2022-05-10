from src.read_data import *
from datetime import datetime

## Returns sum of all the count in the file.
def total_cars(df, count_col):
    return df[count_col].sum()

## Groups data by date and returns the sum of cars for each day.
def total_cars_in_each_day(df, timestamp_col):
    df['date'] = pd.to_datetime(df[timestamp_col]).dt.date
    return df.groupby('date').sum().reset_index()

## Subsets the data to filter out times with 30 minute differences and returns the top three largest count for 30 minute times.
def top_three_hours(df, timestamp_col, count_col):
    df[str(timestamp_col+'_temp')] = df[timestamp_col].apply(lambda x: datetime.strftime(x, '%Y-%m-%dT%H:%M:%S'))  
    df = df.nlargest(3, count_col).reset_index()\
            [[str(timestamp_col+'_temp'),count_col]] 
    return df


## Iterates over each dataframe calculates top 3 consecutive times if they fall within the range on 90 minutes. 
def least_three_half_hours(df, timestamp_col, count_col):
    df['consecutive_count'] = df.rolling(3).sum()
    df['start_timestamp'] = df[timestamp_col] - pd.Timedelta(minutes=90)
    df = df.rename(columns = {timestamp_col:'end_timestamp'})\
                [df['consecutive_count']!=0]\
                    .sort_values(by='consecutive_count').head(3)\
                        .reset_index()\
                            [['start_timestamp', 'end_timestamp', 'consecutive_count']]
    return(df)


def present_output(df):
    df = df.reset_index()
    for i in range(len(df)):
        for cols in df.columns:
            if cols != 'index':
                print(str(df[cols][i]) + '\t', end=" ")
        print('\n')



