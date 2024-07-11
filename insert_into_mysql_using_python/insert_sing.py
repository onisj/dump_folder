import mysql.connector
from mysql.connector import Error

name = input("Type a name: ")
email = input("Type an email: ")

try:
    mydb = mysql.connector.connect(
        host="db",  # change to 'locahost' if runnig this locally, but use 'db' ir running on docker 
        user="jack",
        password="jackroot",  # Replace with your MySQL user password
        database="staff"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO editorial (name, email) VALUES (%s, %s)"
    val = (name, email)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

except Error as err:
    if err.errno == 1062:  # Duplicate entry error code
        print("Error: This email is already in use.")
    else:
        print(f"Error: {err}")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()