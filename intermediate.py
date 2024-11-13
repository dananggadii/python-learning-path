course_ratings = {"LLM Concepts": 4.7, 
                  "Introduction to Data Pipelines": 4.75, 
                  "AI Ethics": 4.62, 
                  "Introduction to dbt": 4.81}

# Print the number of key-value pairs
num_courses = len(course_ratings)
print(num_courses)

# =================================================================================================

# Print the average number of completions, rounded to one decimal places
print(round(sum(course_ratings) / len(course_ratings), 1))

# =================================================================================================

# Import date from the datetime module
from datetime import date

# Create a variable called deadline
deadline = date(2024, 1, 19)

# Check the data type
print(type(deadline))

# Print the deadline
print(deadline)

# =================================================================================================

import pandas as pd

sales = {
  "user_id" : ["KM37", "PR19", "YU88"],
  "order_value" : [197.75, 208.21, 134.99]
}

sales_df = pd.DataFrame(sales) # read dataframe 
sales_df.head() # preview file 
sales_df # print dataframe

# =================================================================================================

# Read in sales.csv
sales_df = pd.read_csv("sales.csv")

# Print the mean order_value
print(sales_df["order_value"].mean())

# Print the total value of sales
print(sales_df["order_value"].sum())

# =================================================================================================

def average(values):
  average_value = sum(values) / len(values)
  return round(average_value, 2)

sales = [23, 235, 56, 45, 78]

average_sales = average(sales)

print(average_sales)

# =================================================================================================

def find_max(a_list):
  sorted_list = sorted(a_list)
  max_values = sorted_list[-1]
  return max_values

list_value = [20, 4, 11, 9, 10]

max_values = find_max(list_value)

print(max_values)