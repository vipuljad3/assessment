#! /venv/bin/python3

from src.analytics import *
from src.read_data import *

filename = 'sample.txt'
directory = '/home/vipuljad/assessment/raw_data/'
count_col='count'
timestamp_col = 'timestamp'

data = read_file(directory, filename)
processed_data = process_input(data)
data_frame = convert_dataframe(processed_data, 'timestamp', 'count')

print(total_cars(data_frame, count_col))
print(total_cars_in_each_day(data_frame,timestamp_col))
print(top_three_hours(data_frame,timestamp_col , count_col))
print(least_three_half_hours(data_frame, timestamp_col, count_col))