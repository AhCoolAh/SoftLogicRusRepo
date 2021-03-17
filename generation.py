import psycopg2
import random

conn = psycopg2.connect(host="localhost", port = 5432, database="MapDB", user="postgres", password="ThePassword")

# Create a cursor object
cur = conn.cursor()
for i in range(100000):
    latitude = "%.6f" % random.uniform(55.59, 55.94)
    longitude = "%.6f" % random.uniform(37.40, 37.85)
    
    sql = "INSERT INTO mysite_pointgeo (lat_coord, lon_coord, geometry_type, feature_type, baloon_content) VALUES (%s, %s, %s, %s, %s)"
    val = (latitude, longitude, "Point", "Feature", 'Балун')
    cur.execute(sql, val)
    

conn.commit()  
print("Record inserted successfully")  

conn.close()
