import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             database='db',
                             cursorclass=pymysql.cursors.DictCursor)

#with connection:
cursor = db.cursor()

# to excute a SQL query (e.g., SELECT)
cursor.execute("SELECT * FROM your_table")

# fetch the results
results = cursor.fetchall()
print(result)
