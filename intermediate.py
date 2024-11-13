course_ratings = {"LLM Concepts": 4.7, 
                  "Introduction to Data Pipelines": 4.75, 
                  "AI Ethics": 4.62, 
                  "Introduction to dbt": 4.81}

# Print the number of key-value pairs
num_courses = len(course_ratings)
print(num_courses)

# =================================================================================================

# Print the average number of completions, rounded to one decimal places
print(round(sum(course_completions) / len(course_completions), 1))
