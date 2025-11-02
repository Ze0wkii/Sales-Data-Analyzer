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
            # Read the CSV file, ignoring the unwanted index column
            sales_csv = pd.read_csv(cls.CSV_file)


            # Clean up column names and data (remove spaces, fix capitalization)
            sales_csv.columns = sales_csv.columns.str.strip()
            sales_csv['Date'] = sales_csv['Date'].astype(str).str.strip()
            sales_csv['Region'] = sales_csv['Region'].astype(str).str.strip().str.title()

            # Filter the DataFrame to match the given date and region
            filtered_df = sales_csv[
                (sales_csv['Date'] == date) &
                (sales_csv['Region'] == region.title())
            ]

            # Check if any rows matched the given date & region
            if not filtered_df.empty:
                products = filtered_df['Product'].values

                # Extract price and cost per unit arrays
                ppu = filtered_df['Price Per Unit'].values
                cpu = filtered_df['Cost Per Unit'].values

                # Calculate total revenue and total cost
                total_ppu = ppu.sum()
                total_cpu = cpu.sum()

                # Calculate profit or loss
                total_sales = total_ppu - total_cpu

                # Determine the "condition" — performance category
                if total_sales >= 20:
                    condition = True   # strong profit
                elif 0 <= total_sales < 20:
                    condition = False  # low profit
                else:
                    condition = None   # loss

                # Display appropriate message
                if condition == True:
                    print(f"✅ Your sales are really positive.\nTotal Sales: ${total_sales} on products: {products}")
                elif condition == False:
                    print(f"⚠️ Your sales are low but still positive.\nTotal Sales: ${total_sales} on products: {products}")
                else:
                    print(f"❌ You're in loss.\nTotal Sales: ${total_sales} on products: {products}")

            # If no matching rows were found
            else:
                print(filtered_df['Date'], filtered_df['Region'])
                print('The provided date and region do not exist')

        except Exception as e:
            print(e)


        




Sales.initializer()
Sales.sales('01-11-25', 'Mumbai')


