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
    @classmethod
    def add_entry(cls, date, region, product, units_sold, price):
        sales_data = {
            'Date': date,
            'Region': region,
            'Product': product,
            'Units Sold': units_sold,
            'Price': price
        }
        with open(cls.CSV_file, 'a', newline="") as df:
            writer = csv.DictWriter(df, fieldnames=cls.COLUMNS)
            writer.writerow(sales_data)

        print('Entry Successfully added.')
    @classmethod
    def sales(cls, date, region):
        try:
            sales_csv = pd.read_csv(cls.CSV_file)
            filtered_df = sales_csv[(sales_csv['Date'] == date) & (sales_csv['Region'] == region)]


            # print(sales_csv)
            if not filtered_df.empty:
                print(filtered_df)
                product_values = filtered_df['Product'].values
                sales_values = filtered_df['Units Sold'].values
                price_values = filtered_df['Price'].values
                print(sales_values, product_values, price_values)
                
            else:
                print('The provided date and region does not exist')
        except Exception as e:
            print(e)
        




Sales.initializer()
# Sales.add_entry('12-12-25', 'Thane', 'Ethanol', 500, 5000)
Sales.sales('12-12-25', 'Thane')