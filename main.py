# Things to do/focus: 
# 1. Proper Data Handling System
# 2. Proper Error System
# 3. Clean & Simple code
# 4. !!90/10 (90% Self & 10% AI)!!

# PROJECT: SALES DATA ANALYZER!!

# Things to Add: 
#  1. Total sales by region
#  2. top-selling products
#  3. month-on-month trends.

import pandas as pd
import csv

class Sales:
    CSV_file = 'sales.csv'
    COLUMNS = ['Date', 'Region', 'Product', 'Units Sold', 'Price']

    @classmethod
    def initializer(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_file)
            print('File initialized Successfully.')

Sales.initializer()