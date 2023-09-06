import pandas as pd
import re
from data import get_data

def clean_data(dataframe):

    cleaned_data = []

    for index, row in dataframe.iterrows():

        # Get the values from the dataframe
        bucket_number = row['List the bucket numbers collected'].strip().lower()
        expected_bucket = row['How many clean containers are dropped off?']

        # 1. Split the bucket numbers and count them
        bucket_numbers = bucket_number.split(', ')
        num_bucket_numbers = len(bucket_numbers)

        # 2. If the number of bucket numbers is less than the expected, add "-" characters. Skip if expected buckets is empty
        if len(expected_bucket) < 1 or len(expected_bucket) > 2:
          continue 

        if num_bucket_numbers < int(expected_bucket):
            diff = int(expected_bucket) - num_bucket_numbers
            bucket_numbers += ['-'] * diff

        # 3. Replace all occurrences of a comma followed by a space with just a comma
        bucket_number = ', '.join(bucket_numbers)

        # Rest of the cleaning steps
        number_words = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0',
            'oh': '0',
            'dash': '-'
        }

        for word, replacement in number_words.items():
            bucket_number = bucket_number.replace(word, replacement)

        # 4. Replace "Dash" with "-"
        bucket_number = bucket_number.replace('dash', '-')

        # 5. Check for duplicate numbers
        if bucket_number not in cleaned_data:
            cleaned_data.append(bucket_number)

    return cleaned_data

data = get_data("(live) customer bucket tracking","Test_Validation_Dataset")

cleaned_data = clean_data(data)

print(cleaned_data)
