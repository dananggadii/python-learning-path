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

# =================================================================================================

# Create the clean_string function
def clean_string(text):
  
  # Replace spaces with underscores
  no_spaces = text.replace(" ", "_")
  
  # Convert to lowercase
  clean_text = no_spaces.lower()
  
  # Return the final text as an output
  return clean_text

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)

# =================================================================================================

password = "not_very_secure_2023"

# Define the password_checker function
def password_checker(submission):
  
  # Check that the password variable and the submission match
  if password == submission:
    print("Successful login!")
  
  # Otherwise, print "Incorrect password"
  else:
    print("Incorrect password")

# Call the function    
password_checker("NOT_VERY_SECURE_2023")

# =================================================================================================

# Create the convert_data_structure function
def convert_data_structure(data, data_type="list"):
  
  # If data_type is "tuple"
  if data_type == "tuple":
    data = tuple(data)
  
  # Else if data_type is set, convert to a set
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

# Call the function to convert to a set
convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")

# =================================================================================================

# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
    data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
    data (list, tuple, or set): Converted data structure.
  """
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

print(help(convert_data_structure))

# =================================================================================================

# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))

# =================================================================================================

# Define a function called concat
def concat(**kwargs):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))

# =================================================================================================

sale_price = 29.99

# Define a lambda function called add_tax
add_tax = lambda x: x * 1.2

# Call the lambda function
print(add_tax(sale_price))

# =================================================================================================

sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x: x * 1.2)(sale_price))

# =================================================================================================

sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x * 1.2, sales_prices)

# Use add_taxes to return a new list with updated values
print(list(add_taxes))

# =================================================================================================

def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")

# =================================================================================================

def snake_case(text):
  # Check the data type
  if type(text) == str:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")


