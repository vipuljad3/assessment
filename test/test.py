#! /venv/bin/python3

import os, sys
import warnings
import logging

sys. path. append(os. path. dirname(os. path. dirname(os. path. abspath(__file__))))
from src.analytics import *
from src.read_data import *

warnings.simplefilter(action='ignore', category=FutureWarning)
logging.basicConfig(filename= 'test/test_logs.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info("Running TESTS")

filename = 'sample.txt'
directory = '/home/vipuljad/assessment/test/test_data/'
count_col = 'count'
count_col='count'
timestamp_col = 'timestamp'

data = read_file(directory, filename)
processed_data = process_input(data)
data_frame = convert_dataframe(processed_data, timestamp_col, count_col)
data_frame = fill_missing_times(data_frame,timestamp_col,count_col)

logging.info('Tetsing total car count with sample data')
assert total_cars(data_frame, count_col) == 398
logging.info('Test 1 passed')

logging.info('Tetsing total car count each day')
df = total_cars_in_each_day(data_frame,timestamp_col)
assert df[count_col][0] == 179
logging.info('Test 2 passed')

logging.info('Tetsing top 3 hours')
df =  top_three_hours(data_frame,timestamp_col , count_col)
assert df[count_col][0] == 46
logging.info('Test 3 passed')

logging.info('Tetsing least 3 half hour periods - 3 contiguous half hour records')
df = least_three_half_hours(data_frame, timestamp_col, count_col)
assert df['consecutive_count'][0] == 6
logging.info('Test 4 passed')

logging.info('All Tests passed')