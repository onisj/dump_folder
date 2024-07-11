import csv

# Define the file name
filename = 'data/data.csv'

# Define the header
header = ['name', 'email']

# Generate sample data
data = []
for i in range(1, 21):
    name = f'User{i} Name'
    email = f'user{i}@example.com'
    data.append([name, email])

# Write the data to a CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print(f"{filename} created successfully with 20 entries.")
