import mysql.connector
import csv

# Database connection
mydb = mysql.connector.connect(
    host="db",  # change to 'locahost' if runnig this locally, but use 'db' ir running on docker
    user="jack",
    password="jackroot",  # Use your own password here
    database="staff"
)

mycursor = mydb.cursor()

try:
    # Open the CSV file
    with open('data/data.csv', mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        # Skip the header row
        next(csv_reader)
        # Iterate over the rows in the CSV file
        for row in csv_reader:
            name, email = row
            sql = "INSERT INTO editorial (name, email) VALUES (%s, %s)"
            val = (name, email)
            mycursor.execute(sql, val)

    # Commit the transaction
    mydb.commit()
    print(mycursor.rowcount, "records inserted.")

except mysql.connector.Error as err:
    if err.errno == 1062:  # Duplicate entry error code
        print("Error: This email is already in use.")
    else:
        print(f"Error: {err}")
        mydb.rollback()

finally:
    # Close the cursor and connection
    mycursor.close()
    mydb.close()

print("Data inserted successfully.")
