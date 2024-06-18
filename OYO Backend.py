import mysql.connector
from mysql.connector import Error

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Saurav121@__",
        database="OYO"
    )

conn = create_connection()
if conn.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect")

def register_customer(cname="John Doe", contact="1234567890", address="New York", registration_date="2023-06-15"):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Customer (Cname, contact, Address, Registration_Date) VALUES (%s, %s, %s, %s)",
                           (cname, contact, address, registration_date))
            conn.commit()
            print("Customer registered successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database")

def search_hotels(identifier):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Hotel WHERE Hname = %s OR Address = %s", (identifier, identifier))
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database")
        return []

def search_customer(identifier):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customer WHERE Cname = %s OR contact = %s OR Address = %s", (identifier, identifier, identifier))
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database")
        return []

def search_booking(identifier):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Booking WHERE HID = %s OR CID = %s OR RID = %s", (identifier, identifier, identifier))
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database")
        return []

def search_payment(identifier):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Payment WHERE PID = %s OR CID = %s OR BID = %s", (identifier, identifier, identifier))
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database")
        return []

if __name__ == "__main__":
    register_customer()
    
    identifier = input("Enter an identifier (hotel name, customer name, contact, address, booking ID, payment ID): ")
    print("Details:")
    customers = search_customer(identifier)
    hotels = search_hotels(identifier)
    bookings = search_booking(identifier)
    payments = search_payment(identifier)

    for result in customers + hotels + bookings + payments:
        print(result)
