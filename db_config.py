import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user='3ogi8U4vfwbPM1D.root',
        password='qdI47rhMXFuNLBCr',
        database='student_task_manager',
        port = 4000
    )
    return connection


# Test Database Connection
conn = get_database_connection()

if conn.is_connected():
    print("Database Connected Successfully")

# def get_database_connection():
#     connection = mysql.connector.connect(
#         host='localhost',
#         user='Parth',
#         password='Parth4729',
#         database='student_task_manager'
#     )
#     return connection


# # Test Database Connection
# conn = get_database_connection()

# if conn.is_connected():
#     print("Database Connected Successfully")