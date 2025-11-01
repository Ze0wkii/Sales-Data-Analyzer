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
import numpy as np
import csv

class Sales:
    CSV_file = 'sales.csv'
    COLUMNS = ['Date', 'Region', 'Product', 'Units Sold', 'Price Per Unit', 'Cost Per Unit']

    @classmethod
    def initializer(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_file)
            print('File initialized Successfully.')
    @classmethod
    def add_entry(cls, date, region, product, units_sold:int, ppu:int, cpu:int):
        sales_data = {
            'Date': date,
            'Region': region,
            'Product': product,
            'Price Per Unit':ppu,
            'Cost Per Unit':cpu,
            'Units Sold': units_sold,
        }
        with open(cls.CSV_file, 'a', newline="") as df:
            writer = csv.DictWriter(df, fieldnames=cls.COLUMNS)
            writer.writerow(sales_data)

        print('Entry Successfully added.')
    @classmethod
    def sales(cls, date, region):
        try:
            sales_csv = pd.read_csv(cls.CSV_file)
            print(sales_csv.columns)
            sales_csv.columns = sales_csv.columns.str.strip()

            filtered_df = sales_csv[(sales_csv['Date'] == date) & (sales_csv['Region'] == region)]
            
            print("Filtering for:", date, region)
            print(filtered_df)
            if not filtered_df.empty:
                products = filtered_df['Product'].values

                ppu = filtered_df['Price Per Unit'].values
                cpu = filtered_df['Cost Per Unit'].values  # fixed column name

                total_ppu = ppu.sum()
                total_cpu = cpu.sum()

                total_sales = total_ppu - total_cpu  # fixed logical direction (profit = revenue - cost)

                if total_sales >= 20:
                    condition = True
                elif 0 <= total_sales < 20:
                    condition = False
                else:
                    condition = None

                # Moved this outside the if-else
                if condition == True:
                    print(f"Your sales are really positive.\nTotal Sales: {total_sales} on products {products}")
                elif condition == False:
                    print(f"Your sales are low but positive.\nTotal Sales: {total_sales} on products {products}")
                else:
                    print(f"You're in loss.\nTotal Sales: {total_sales} on products {products}")

            else:
                print('The provided date and region does not exist')

        except Exception as e:
            print(e)

        




Sales.initializer()
Sales.sales('01-11-25', 'Mumbai')


