opened_file = open('AppleStore.csv') # Open file
from csv import reader # Import reader
read_file = reader(opened_file) # Read file
apps_data = list(read_file) # Convert file to a list

for app in apps_data[1:]: # For each row after the header in the apps_data list
    price = float(app[4]) # Set price to equal the 4th indexed item in each row as a float
    if price == 0: # If price is 0, label the app as free by appending the string 'free' at the end of the current row
        app.append('free')
    elif 0 < price < 20:
        app.append('affordable')
    elif 20 <= price < 50: 
        app.append('expensive')
    else:
        app.append('very expensive')
        
apps_data[0].append('price_label') # Append the strong 'price_label' to the first (header) row of the apps_data list
print(apps_data[:6]) # Print the header row and first 5 data rows
