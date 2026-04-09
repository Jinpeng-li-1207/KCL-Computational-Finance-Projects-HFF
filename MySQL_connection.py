import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        print(f"Attempting to connect to the '{db_name}' database...")
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print(f"Connection to MySQL DB '{db_name}' successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    """Execute a single query that modifies data (INSERT, UPDATE, DELETE)."""
    cursor = connection.cursor()  #Create a cursor object to execute SQL queries
    try:
        cursor.execute(query)  
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def execute_read_query(connection, query):
    """Execute a single query that reads data (SELECT) and returns the result."""
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

if __name__ == "__main__":  # This block will only execute if this script is run directly, not when imported as a module
    HOST = "localhost"
    USER = "root"
    PASSWORD = "L!jp20021207"
    DATABASE = "hff_coursework1"

    conn = create_connection(HOST, USER, PASSWORD, DATABASE)

    if conn and conn.is_connected():
        test_query_1 = "SELECT COUNT(*) FROM Glaxo_order_detail;" # Count the total number of orders
        print("\nExecuting test query to count orders...")
        results_1 = execute_read_query(conn, test_query_1)
        
        if results_1:
            order_number = results_1[0][0] # fetchall() returns a list of tuples
            print("-" * 30)
            print(f"Total number of orders in 'Glaxo_order_detail': {order_number}")
            print("-" * 30)

        cancel_query = "SELECT COUNT(*) FROM Glaxo_order_history WHERE Action = 'D';"
        print("\nExecuting query to count cancelled orders...")
        
        results_2 = execute_read_query(conn, cancel_query)
        
        # 5. Extract and format the result safely
        if results_2:
            cancelled_count = results_2[0][0]
            print("-" * 30)
            print(f"Total number of cancelled orders (Action = 'D'): {cancelled_count}")
            print("-" * 30)
            
        conn.close()
        print(" Database connection closed safely.")