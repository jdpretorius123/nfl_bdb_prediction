## loading dependent packages
import pandas as pd
import glob
import os

## defining the data directory
data_dir = './data/train/'

## locating all files that match the pattern input_2023_w[01-18].csv
input_files = glob.glob(os.path.join(data_dir, 'input_2023_w*.csv'))

## loading all input files into a list of data frames
input_df_list = [pd.read_csv(file) for file in input_files]

## concatenating all input data frames into a single data frame
input_data = pd.concat(input_df_list, ignore_index = True)

## getting an overview of the input data
print(input_data.info())
print(input_data.describe())
print(input_data.head())
print(input_data.tail())

## locating all files that match the pattern output_2023_w[01-18].csv
output_files = glob.glob(os.path.join(data_dir, 'output_2023_w*.csv'))

## loading all output files into a list of data frames
output_df_list = [pd.read_csv(file) for file in output_files]

## concatenating all output data frames into a single data frame
output_data = pd.concat(output_df_list, ignore_index = True)

## getting an overview of the output data
print(output_data.info())
print(output_data.describe())
print(input_data.head())
print(input_data.tail())