import json
import re
from statistics import mean, median
from numpy import std
import pandas as pd

'''
This functions process the file based on the file format. 
Accepted file formats are csv, json, and txt.

Args:
    file_path: str: The path to the file to be processed.

Returns:
    dict: A dictionary containing summary information about the file.
'''

def process_csv(file_path):
    def extract_columns():
        '''
        Extract the columns in the data.
        '''
        columns.update(data.columns)

    def extract_unique_values():
        '''
        Extract unique values from the data.
        '''
        for column in columns:
            unique_values.update(data[column].astype(object).unique())

    def extract_columns_sum():
        '''
        Extract the sum of numerical columns in the data.
        '''
        columns_sum = {}
        for column in columns:
            if data[column].dtype != 'object':
                columns_sum[column] = int(data[column].sum())
        return columns_sum
    
    def extract_columns_avg():
        '''
        Extract the average of numerical columns in the data.
        '''
        columns_avg = {}
        for column in columns:
            if data[column].dtype != 'object':
                columns_avg[column] = int(data[column].mean())
        return columns_avg
    
    def extract_columns_max():
        '''
        Extract the maximum value of numerical columns in the data.
        '''
        columns_max = {}
        for column in columns:
            if data[column].dtype != 'object':
                columns_max[column] = int(data[column].max())
        return columns_max
    
    def extract_columns_min():
        '''
        Extract the minimum value of numerical columns in the data.
        '''
        columns_min = {}
        for column in columns:
            if data[column].dtype != 'object':
                columns_min[column] = int(data[column].min())
        return columns_min
    
    def extract_columns_median():
        '''
        Extract the median of numerical columns in the data.
        '''
        columns_median = {}
        for column in columns:
            if data[column].dtype != 'object':
                columns_median[column] = int(data[column].median())
        return columns_median
    
    def extract_columns_std():
        '''
        Extract the standard deviation of numerical columns in the data.
        '''
        columns_std = {}
        for column in columns:
            if data[column].dtype != 'object':
                columns_std[column] = int(data[column].std())
        return columns_std
    
    data = pd.read_csv(file_path)
    num_rows = len(data)
    unique_values = set()
    columns = set()
    extract_columns()
    extract_unique_values()
    

    response_data = {
    'num_rows': num_rows,
    'unique_values': list(unique_values),
    'columns': list(columns),
    'statistical_measures': {
        'sum': extract_columns_sum(),
        'avg': extract_columns_avg(),
        'max': extract_columns_max(),
        'min': extract_columns_min(),
        'median': extract_columns_median(),
        'std': extract_columns_std()
        }
    }
    return response_data

def process_json(file_path):
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
        num_records = len(data)
        unique_values = set()
        columns = set()

        def extract_columns():
            '''
            Extract the columns in the data.
            '''
            columns.update(data.keys())

        def extract_unique_values(data):
            '''
            Recursively extract unique values from nested lists and dictionaries.

            Args:
                data: list or dict: The data to extract unique values from.
            '''
            if isinstance(data, dict):
                for value in data.values():
                    if isinstance(value, (list, dict)):
                        extract_unique_values(value)
                    else:
                        unique_values.add(value)
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, (list, dict)):
                        extract_unique_values(item)
                    else:
                        unique_values.add(item)               

        def extract_columns_sum():
            '''
            Extract the sum of numerical columns in the data.
            '''
            columns_sum = {}
            for column in columns:
                if not isinstance((data[column][0]), str) and not isinstance((data[column][0]), list) and not isinstance((data[column][0]), dict) and not isinstance((data[column][0]), bool):
                    columns_sum[column] = round(sum(data[column]),2)
            return columns_sum
        
        def extract_columns_avg():
            '''
            Extract the average of numerical columns in the data.
            '''
            columns_avg = {}
            for column in columns:
                if not isinstance((data[column][0]), str) and not isinstance((data[column][0]), list) and not isinstance((data[column][0]), dict) and not isinstance((data[column][0]), bool):
                    columns_avg[column] = round(mean(data[column]),2)
            return columns_avg
        
        def extract_columns_max():
            '''
            Extract the maximum of numerical columns in the data.
            '''
            columns_max = {}
            for column in columns:
                if not isinstance((data[column][0]), str) and not isinstance((data[column][0]), list) and not isinstance((data[column][0]), dict) and not isinstance((data[column][0]), bool):
                    columns_max[column] = round(max(data[column]),2)
            return columns_max
        
        def extract_columns_min():
            '''
            Extract the minimum of numerical columns in the data.
            '''
            columns_min = {}
            for column in columns:
                if not isinstance((data[column][0]), str) and not isinstance((data[column][0]), list) and not isinstance((data[column][0]), dict) and not isinstance((data[column][0]), bool):
                    columns_min[column] = round(min(data[column]),2)
            return columns_min
        
        def extract_columns_median():
            '''
            Extract the median of numerical columns in the data.
            '''
            columns_median= {}
            for column in columns:
                if not isinstance((data[column][0]), str) and not isinstance((data[column][0]), list) and not isinstance((data[column][0]), dict) and not isinstance((data[column][0]), bool):
                    columns_median[column] = round(median(data[column]),2)
            return columns_median
        
        def extract_columns_std():
            '''
            Extract the standard deviation of numerical columns in the data.
            '''
            columns_std= {}
            for column in columns:
                if not isinstance((data[column][0]), str) and not isinstance((data[column][0]), list) and not isinstance((data[column][0]), dict) and not isinstance((data[column][0]), bool):
                    columns_std[column] = round(std(data[column]),2)
            return columns_std
        
        extract_columns()
        extract_unique_values(data)

        response_data = {
        'num_rows': num_records,
        'columns': list(columns),
        'unique_values': list(unique_values),
        'statistical_measures': {
            'sum': extract_columns_sum(),
            'average': extract_columns_avg(),
            'max': extract_columns_max(),
            'min': extract_columns_min(),
            'median': extract_columns_median(),
            'std': extract_columns_std()
            }
        }
        return response_data

def process_txt(file_path):
    def search_pattern(pattern, text):
            '''
            Search for a pattern in a given text.

            Args:
                pattern: str: The pattern to search for.
                text: str: The text to search in.
            '''
            return re.findall(pattern, text)
    
    with open(file_path, 'r') as txtfile:
        lines = txtfile.readlines()
        num_rows = len(lines)

        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = search_pattern(email_pattern, ' '.join(lines))

        phone_pattern = r'(?:\+\d{2}\s?(?:\d{3}\s?|\(\d{3}\)\s?)?\d{3}\s?\d{3}\s?\d{3}|(?:\d{3}\s?|\(\d{3}\)\s?)?\d{3}\s?\d{3}\s?\d{3})'
        phones = search_pattern(phone_pattern, ' '.join(lines))

        def check_word_in_phone_number(word):
            '''
            Check if a word is in a phone number.

            Args:
                word: str: The word to check.
            '''
            return any(word in phone for phone in phones)

        words = ' '.join(lines).split()
        words = [word for word in words if not check_word_in_phone_number(word) and word not in emails]
        unique_values = sorted(set(words))

        unique_characters = sorted(set(''.join(words)))

        response_data = {
        'num_rows': num_rows,
        'unique_values': list(unique_values),
        'unique_characters': ' '.join(unique_characters),
        'emails': emails,
        'phones': phones
        }

        return response_data