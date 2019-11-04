''' test module homework 4 follow PEP8'''

import pandas as pd
import requests


def read(url, filename):
    '''read URL and return data file'''
    link = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(link.content)
    output = pd.read_csv(filename)
    return output


def test_create_dataframe(df, column_list):
    '''test if dataframe fulfill the requirements'''
    # count the row amounts
    count = 0
    for i in list(df.columns):
        count = count + 1
    row = df.size//count
    if row < 10:
        return False

    # check the column types
    for i in range(count):
        if df.dtypes[i] != df.dtypes[0]:
            return False

    # check if the DataFrame contains only the columns that you specified as the second argument
    set2 = set(column_list)
    set1 = set(list(df.columns))
    return set1.issubset(set2)
