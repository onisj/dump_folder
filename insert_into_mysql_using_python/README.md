# MySQL Database Insertion using Python

This project demonstrates how to insert data into a MySQL database using Python scripts within a Pipenv environment on a Windows machine.

## Prerequisites

Before running the scripts, ensure you have the following installed:
- Python
- MySQL Server

## Setup Instructions


## 1.  Setup Instructions for Running the project on Docker

A. **Creating the Dicker Image:**
   Run the following command in your terminal:
   
   ```bash
   docker-compose up --build
   ```

B. **Connect to MySQL database:**

   - **Check running containers:**
      To connect to MySQL Database on Docker, run the following code in another terminal:

      ```bash
      docker ps
      ```
      You shold see something similar to this:

      ```bash
      CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
      b3d34503e54b   mysql:8.0   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   mysql_db
      ```

   - **Access MySQL command line:**
      Access MySQL ciommand line using the following code:
      
      ```bash
      docker exec -it mysql_db mysql -u root -p
      ```

      The code above will prompt yu to enter a password, which was initially set as **`rootpassword`** in the `dockeer-compose.yml` file

C. **Create a database (`staff`) and user (`jack`) and GRANT (`ALL`) rights:**
     
     ```sql
     CREATE DATABASE staff;
     CREATE USER 'jack'@'%' IDENTIFIED BY 'jackroot';
     GRANT ALL PRIVILEGES ON staff.* TO 'jack'@'localhost';
     FLUSH PRIVILEGES;
     ```

D. **Create the table:**
   Create the table `editorial` with the following code:

   ```sql
   USE staff;

   CREATE TABLE editorial (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), email VARCHAR(30) UNIQUE);
   ```



## 2. Setup Instructions for Running on Local machine

A. **Create and Activate the Pipenv Environment:**
   - Open your terminal or command prompt.
   - Navigate to your project directory.
   - Create and activate a new `pipenv` environment:
     
     ```python
     pip install pipenv
     pipenv shell
     ```

B. **Install Required Packages:**
   - While in the `pipenv` environment, install the required packages:
     
     ```pyhton
     pipenv install pandas mysql-connector-python jupyter
     ```

C. **Install MySQL Server:**
   - If MySQL server is not already installed on your Windows machine, download and install it from the official [MySQL](https://dev.mysql.com/downloads/mysql/) website.

D. **Create MySQL Database and User:**
   - Open the MySQL command line client.
   - Log in as the root user and create a database (`staff`) and user (`jack`):
     
   ```sql
   CREATE DATABASE staff;
   CREATE USER 'jack'@'localhost' IDENTIFIED BY 'jackroot';
   GRANT ALL PRIVILEGES ON staff.* TO 'jack'@'localhost';
   FLUSH PRIVILEGES;
   ```

E. **Create the table:**
   Create the table `editorial` with the following code:

   ```sql
   USE staff;

   CREATE TABLE editorial (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), email VARCHAR(30) UNIQUE);
   ```



## 3. **Create the Python Scripts**

A. **Create the following Python scripts in your project directory:**

   - `insert_sing.py`: Inserts a single record into the `editorial` table.
   - `insert_many.py`: Reads from a CSV file (`data.csv`) drom the data directory and inserts multiple records into the `editorial` table.
   - `generate_csv.py`: Generates sample data and writes it to `data/data.csv`.

B. **Run the Python Scripts:**
   - While still in the Pipenv environment, run the scripts in the particular order:
     
   ```python
   python generate_csv.py
   python insert_sing.py
   python insert_many.py
   ```

## 4. **Verify Data Insertion:**

Go back into the MySQL command line to Verify the data was inserted:

```sql
SELECT COUNT(*) FROM editorial;
```

---

## Additional Notes

- **Log in as the Root User:** If you are not logged in as the root user in MySQL, use:

```sql
mysql -u root -p
```
Enter the root password when prompted.

- **Granting Privileges:** After creating the `jack` user, grant the necessary privileges using:

```sql
GRANT ALL ON staff.* TO 'jack'@localhost' IDENTIFIED BY 'jackroot';
FLUSH PRIVILEGES;
```


- **CSV File Population:** You can use `insert_many.py` to populate the `editorial` table from a CSV file (`data.csv`). Ensure the CSV file format matches the expected columns (`name`, `email`).

---

By following these steps, you should be able to set up and use this project to insert data into a MySQL database on your Windows machine using Python scripts within a `pipenv` environment.
