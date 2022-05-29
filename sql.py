import sqlite3 as sql
import os
import csv
from sqlite3 import Error

try:
  conn=sql.connect('mydatabase')

  cursor = conn.cursor()
  cursor.execute("SELECT  product_product.slug,order_orderitem.quantity AS sl, product_product.price,order_orderitem.quantity*product_product.price as Tongtien  FROM product_product JOIN order_orderitem ON product_product.id = order_orderitem.product_id GROUP BY product_product.id")
  with open("test.csv", "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=",")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(cursor)
  dirpath = os.getcwd() + "/test.csv"
except Error as e:
  print(e)
finally:
  conn.close()