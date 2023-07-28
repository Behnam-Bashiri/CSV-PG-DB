import csv
import psycopg2

# Database connection parameters
DB_NAME = "DBName"
DB_USER = "DBUser"
DB_PASSWORD = "DBPassword"
DB_HOST = "DBHost"
DB_PORT = "DBPort"

# CSV file path
csv_file_path = "CSV root"  # Replace with the actual CSV file path

# Function to insert data into the database
def insert_data_to_db():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Truncate the table before inserting data (Optional)
        cursor.execute('TRUNCATE TABLE public."tablenameimportecsv";')
        conn.commit()

        # Open the CSV file and insert the data into the table
        with open(csv_file_path, "r", newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header row
            for row in csvreader:
                id, header1, header2, header3 = row
                cursor.execute(
                    'INSERT INTO public."tablenameimportecsv" (id, "header1", "header2", "header3") VALUES (%s, %s, %s, %s);',
                    (id, Day, E_Grid, PR)
                )

        # Commit the changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        print("Data inserted successfully!")
    except psycopg2.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    insert_data_to_db()
