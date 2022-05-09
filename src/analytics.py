from src.read_data import *

def total_cars(df, count_col):
    return df[count_col].sum()

def total_cars_in_each_day(df, timestamp_col):
    df['date'] = pd.DatetimeIndex(df[timestamp_col]).normalize() 
    return df.groupby('date').sum().reset_index()

def top_three_hours(df, timestamp_col, count_col):
    df['delta'] = (df[timestamp_col]-df[timestamp_col].shift()).dt.total_seconds()
    df = df[df.delta == 1800]
    df = df.nlargest(3, count_col).reset_index() 
    return df[[timestamp_col,count_col]]

def index_in_list(a_list, index):
    return (index < len(a_list))

def least_three_half_hours(df, timestamp_col, count_col):
    df['date_'] = pd.to_datetime(df[timestamp_col]).dt.date
    df['time_'] = pd.to_datetime(df[timestamp_col]).dt.time
    df = df[[timestamp_col, 'date_', 'time_', count_col]]
    field_list= []
    for date in df.date_.unique():
        temp_df = df[df.date_ == date].sort_values(by=timestamp_col).reset_index()
        for i in range(len(temp_df)):
            if index_in_list(temp_df[count_col], i+2) and (pd.Timedelta(temp_df[timestamp_col][i+2] - temp_df[timestamp_col][i]).seconds) == 3600:
                sum_val = temp_df[count_col][i]+temp_df[count_col][i+1]+temp_df[count_col][i+2]
                field_list.append((str(date), str(temp_df['time_'][i]),str(temp_df['time_'][i+2]),sum_val))
                
    df = pd.DataFrame.from_records(field_list, columns =['date', 'start_time', 'end_time', count_col])
    return(df.sort_values(by=count_col).head(3))
            
