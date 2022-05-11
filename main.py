#! /venv/bin/python3

## importing required modules
from src.analytics import *
from src.read_data import *
from src.read_config import read_config
import warnings
## Skipping future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

## Reading config file and assigning values to variables
config = read_config('config.yaml')
filename = config['vehicle_counter']['filename']
directory = config['vehicle_counter']['directory']
count_col= config['vehicle_counter']['count_col']
timestamp_col = config['vehicle_counter']['timestamp_col']

## Reading and processing data
data = read_file(directory, filename)
processed_data = process_input(data)
data_frame = convert_dataframe(processed_data, timestamp_col, count_col)
data_frame = fill_missing_times(data_frame,timestamp_col,count_col)

## Performing data analysis and printing output
print('\n1. The number of cars seen in total =',total_cars(data_frame, count_col))
print("\n2. A sequence of lines where each line contains a date (in yyyy-mm-dd format) and the number of cars seen on that day (eg. 2016-11-23 289) for all days listed in the input file.\n")
present_output(total_cars_in_each_day(data_frame,timestamp_col))
print("\n3. The top 3 half hours with most cars, in the same format as the input file \n")
present_output(top_three_hours(data_frame,timestamp_col , count_col))
print("\n4. The 1.5 hour period with least cars (i.e. 3 contiguous half hour records)\n")
present_output(least_three_half_hours(data_frame, timestamp_col, count_col))