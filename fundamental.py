# Create a string variable called name
name = 'John Smith'

# Create an integer variable called age
age = 47

# Create a string variable called address
address = 'The Shard, London, SE1 9SG'

# Print their information
print(name, age,  address)

# =================================================================================================

# Create review_one
review_one = """
I really enjoy the courses,
and they are easy to fit into my busy schedule. 
I wish I had started using your platform sooner.
I'll be recommending you to my friends!!
"""
# Create review_two
review_two = """
One year ago, I was unsure of how to make progress in my career. 
Now, I work as a Prompt Engineer, and I can't thank you enough! 
Keep up the great work.
"""

# Print multiple string
print(review_one)
print(review_two)

# =================================================================================================

most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

# Swap spaces for underscores
most_popular_course = most_popular_course.replace(" ", "_")

# Change to lowercase
most_popular_course = most_popular_course.lower()

print(most_popular_course)

# =================================================================================================

# Create the playlist variable
playlist = [1, 'Blinding Lights', 2, 'One Dance', 3, 'Uptown Funk']

# Print the list
print(playlist)

# =================================================================================================

playlist = [1, 'Blinding Lights', 'The Weeknd', 2, 'One Dance', 'Drake', 3, 'Uptown Funk', 'Mark Ronson', 4, 'Closer', 'The Chainsmokers', 5, 'One Kiss', 'Calvin Harris', 6, 'Mr. Brightside', 'The Killers']

# Print all songs in the playlist
for song in playlist:
    print(playlist[1::3])

# =================================================================================================

# Create the playlist dictionary
playlist = {
    "The Weeknd": "Blinding Lights",
    "Drake": "One Dance",
    "Mark Ronson": "Uptown Funk",
    "The Chainsmokers": "Closer",
    "Calvin Harris": "One Kiss",
    "The Killers": "Mr. Brightside",
    "Coldplay": "Viva La Vida"
}

# Print the playlist
print(playlist)

# Print the song by Coldplay
print(playlist['Coldplay'])

# Add a new song
playlist['Usher'] = 'Yeah!'

# Print the songs in the playlist
print(playlist.values())

# =================================================================================================

# Create a tuple
q3_financials = (325780, 1041, 4271599)

# Print the tuple
print(q3_financials)

# =================================================================================================

hip_hop = ["Drake", "JAY-Z", "50 Cent", "Drake"]

# Create a set
indie_set = {"Kings of Leon", "MGMT", "Stereophonics"}

# Convert hip_hop to a set
hip_hop_set = set(hip_hop)

# Print the indie and hip_hop sets
print(indie_set, hip_hop_set)

# =================================================================================================

# Check the number of beds
if num_beds < min_num_beds:
    print("Insufficient bedrooms")

# Check square feet
elif sq_foot <= min_sq_foot:
    print("Too small")

# Check the rent
elif rent > max_rent:
    print("Too expensive")

# If all conditions met
else:
    print("This looks promising!")

# =================================================================================================

user_ids = ["T42YG4KTK", "VTQ39IDQ0", "CRL11YUWX", 
            "K6Y5URXLR", "V4XCBER7V", "IOGQWC61K"]

# Loop through user_ids
for user_id in user_ids:
    # Print the user_id
    print(user_id)

#  =================================================================================================

# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for tickets in range(1, max_capacity + 1):
    # Add one to tickets_sold in each iteration
    tickets_sold += 1
print("Sold out:", tickets_sold, "tickets sold!")

# =================================================================================================

# Loop through the dictionary's keys and values
for key, value in courses.items():
    
    # Check if the value is "AI"
    if value == "AI":
        print(key, "is an AI course")
    
    # Check if the value is "Programming"
    elif value == "Programming":
        print(key, "is a Programming course")
    
    # Otherwise, print that it is a "Data Engineering" course
    else:
        print(key, "is a Data Engineering course")

# =================================================================================================

tickets_sold = 0
max_capacity = 10

# Create a while loop
while tickets_sold < max_capacity:
    
    # Add one to tickets_sold in each iteration
    tickets_sold += 1

# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!")

# =================================================================================================

release_date = 26
current_date = 22

# Create a conditional loop while current_date is less than or equal to the release_date
while current_date <= release_date:
    
    # Increment current_date by one
    current_date += 1
    
    # Promote purchases
    if current_date <= 24:
        print("Purchase before the 25th for early access")
    
    # Check if the date is equal to the 25th
    elif current_date == 25:
        print("Coming soon!")
    else:
        print("Available now!")

# =================================================================================================

# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
    
    # Check for values less than 25
    if value < 25:
    
    # Append the author to the list
        authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)

# =================================================================================================

for genre, average_sale in genre_sales.items():
    
    # Filter for the maximum sales value
    if average_sale == 5166000000:
        
        # Print the genre
        print("Most popular genre: ", genre)
        print("Average sales: ", average_sale)
    
    # Filter for the minimum sales value
    elif average_sale == 80000000:
        
        # Print the genre
        print("Least popular genre: ", genre)
        print("Average sales: ", average_sale)

# =================================================================================================

# Loop through the dictionary
for genre, sale in genre_sales.items():
    
    # Check if genre is Horror or Mystery
    if genre == "Horror" or genre == "Mystery":
        print(genre, sale)
    
    # Check if genre is Thriller and sale is at least 3 million
    elif genre == "Thriller" and sale >= 3000000:
        print(genre, sale)

# =================================================================================================

