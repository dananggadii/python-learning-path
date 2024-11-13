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

sales_df = pd.DataFrame(sales)
print(sales_df)

sales_csv = pd.read_csv(sales.csv)
type(sales_csv) # data type check 

# =================================================================================================

