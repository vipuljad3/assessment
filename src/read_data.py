
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