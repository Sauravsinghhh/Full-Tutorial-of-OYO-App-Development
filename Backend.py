import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Hardik@25",
            database="OYO"
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
    return None

def close_connection(conn, cursor=None):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def execute_query(query, params=None, fetch=False):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if fetch:
                results = cursor.fetchall()
                columns = cursor.column_names
                return results, columns
            conn.commit()
        except Error as e:
            print(f"Error: {e}")
            return [], []
        finally:
            close_connection(conn, cursor)
    else:
        print("Failed to connect to the database")
        return [], []

def register_customer(cname="John Doe", contact="1234567890", address="New York", registration_date="2023-06-15"):
    query = "INSERT INTO Customer (Cname, contact, Address, Registration_Date) VALUES (%s, %s, %s, %s)"
    params = (cname, contact, address, registration_date)
    execute_query(query, params)
    print("Customer registered successfully!")

def search_hotels(identifier):
    query = "SELECT * FROM Hotel WHERE Hname = %s OR Address = %s"
    params = (identifier, identifier)
    return execute_query(query, params, fetch=True)

def search_customer(identifier):
    query = "SELECT * FROM Customer WHERE Cname = %s OR contact = %s OR Address = %s"
    params = (identifier, identifier, identifier)
    return execute_query(query, params, fetch=True)

def search_booking(identifier):
    query = "SELECT * FROM Booking WHERE HID = %s OR CID = %s OR RID = %s"
    params = (identifier, identifier, identifier)
    return execute_query(query, params, fetch=True)

def search_payment(identifier):
    query = "SELECT * FROM Payment WHERE PID = %s OR CID = %s OR BID = %s"
    params = (identifier, identifier, identifier)
    return execute_query(query, params, fetch=True)

def format_and_display_results(results, columns):
    for result in results:
        for column, value in zip(columns, result):
            print(f"{column}: {value}")
        print()

if __name__ == "__main__":
    # Example usage
    # Register a new customer (defaults used)
    register_customer()
    
    # Search for details based on entered identifier
    identifier = input("Enter an identifier (hotel name, customer name, contact, address, booking ID, payment ID): ")
    print("Details:")

    customers, customer_columns = search_customer(identifier)
    hotels, hotel_columns = search_hotels(identifier)
    bookings, booking_columns = search_booking(identifier)
    payments, payment_columns = search_payment(identifier)

    if customers:
        format_and_display_results(customers, customer_columns)
    if hotels:
        format_and_display_results(hotels, hotel_columns)
    if bookings:
        format_and_display_results(bookings, booking_columns)
    if payments:
        format_and_display_results(payments, payment_columns)
