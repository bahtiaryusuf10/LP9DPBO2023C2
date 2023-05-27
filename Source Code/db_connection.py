import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_vehicle",
)

dbcursor = mydb.cursor()

sql1 = "INSERT INTO supercars (brand, type, price, top_speed) VALUES (%s, %s, %s, %s)"
values1 = [
    ("Lamborghini", "Aventador", 7500000000, 2000),
    ("Ferrari", "458 Italia", 3500000000, 2100),
    ("Porsche", "911 GT3", 3000000000, 2200),
    ("McLaren", "P1", 5000000000, 2170),
    ("Bugatti", "Veyron", 10000000000, 2530)
]

dbcursor.executemany(sql1, values1)
mydb.commit()
print(dbcursor.rowcount, "supercar inserted.")

dbcursor.execute("SELECT * FROM supercars")
myresult = dbcursor.fetchall()

print("\nContents of the supercars table :")
for x in myresult:
    print(x)


sql2 = "DELETE FROM supercars WHERE top_speed < %s"
values2 = (2200,)

dbcursor.execute(sql2, values2)
mydb.commit()
print("\n")
print(dbcursor.rowcount, "supercar deleted.")

dbcursor.execute("SELECT * FROM supercars")
myresult = dbcursor.fetchall()

print("\nContents of the supercars table (after delete) :")
for x in myresult:
    print(x)