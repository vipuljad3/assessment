from src.read_data import *


## Returns sum of all the count in the file.
def total_cars(df, count_col):
    return df[count_col].sum()

## Groups data by date and returns the sum of cars for each day.
def total_cars_in_each_day(df, timestamp_col):
    df['date'] = pd.DatetimeIndex(df[timestamp_col]).normalize() 
    return df.groupby('date').sum().reset_index()

## Subsets the data to filter out times with 30 minute differences and returns the top three largest count for 30 minute times.
def top_three_hours(df, timestamp_col, count_col):
    df['delta'] = (df[timestamp_col]-df[timestamp_col].shift()).dt.total_seconds()
    df = df[df.delta == 1800]
    df = df.nlargest(3, count_col).reset_index() 
    return df[[timestamp_col,count_col]]

## A function with boolean return to detect wether the index is present in a list [to be used in least_three_half_hours function]
def index_in_list(a_list, index):
    return (index < len(a_list))



## Iterates over each dataframe calculates top 3 consecutive times if they fall within the range on 90 minutes. 
def least_three_half_hours(df, timestamp_col, count_col):
    df['date_'] = pd.to_datetime(df[timestamp_col]).dt.date
    df['time_'] = pd.to_datetime(df[timestamp_col]).dt.time
    field_list= []
    for i in range(len(df)):
        if index_in_list(df[count_col], i+2) and (pd.Timedelta(df[timestamp_col][i+2] - df[timestamp_col][i]).seconds) == 3600:
            sum_val = df[count_col][i]+df[count_col][i+1]+df[count_col][i+2]
            field_list.append((str(df['date_'][i]), str(df['time_'][i]), str(df['date_'][i+2]), str(df['time_'][i+2]),sum_val))
            
    ndf = pd.DataFrame.from_records(field_list, columns =['start_date', 'start_time', 'end_date', 'end_time', count_col])
    return(ndf.sort_values(by=count_col).head(3))






