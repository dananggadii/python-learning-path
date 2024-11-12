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

# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
    print("Inflation decreased")

# Check if September inflation is more than August inflation
elif inflation_september > inflation_august:
    print("Inflation increased")

# Confirm that they are equal
else:
    print("Inflation remained stable")

