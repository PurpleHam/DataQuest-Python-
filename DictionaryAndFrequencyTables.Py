# What percentage of apps has a content rating of '17+'?
# What percentage of apps can a 15-year-old download?


opened_file = open('AppleStore.csv') # Opens desired file
from csv import reader # Import reader
read_file = reader(opened_file) # Reads file
apps_data = list(read_file) # Converts file to list

content_ratings = {} # Initialize content dictionary

for row in apps_data[1:]: # For each row in list excluding the header in apps_data[0] 
    c_rating = row[10] # Content rating is the 11th for each row 
    if c_rating in content_ratings: # If c_rating is in content_ratings dictionary, add 1 to counter  
        content_ratings[c_rating] += 1
    else: # Else, if it not yet in content_ratings dictionary, initialize counter at 1
    	content_ratings[c_rating] = 1
        
total_number_of_apps = 0 
        
for c_rating in content_ratings:
	total_number_of_apps = content_ratings[c_rating] + total_number_of_apps # Total number of apps


for dict_key in content_ratings: 
    content_ratings[dict_key] /= total_number_of_apps # Convert dictionary value to proportion 
    content_ratings[dict_key] *= 100 # Convert updated proportional dictionary value to percentage
    
print(content_ratings)

percentage_17_plus = content_ratings['17+'] # Percentage of apps that has a content rating of 17+
percentage_15_allowed = 100-percentage_17_plus # Percentage of apps that 15 year olds can download

