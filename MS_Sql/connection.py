
import sys
import pymssql
conn = pymssql.connect(server='DESKTOP-AFLQBQF', user='sa', password='Sivaram031*', database='testind_one')

cursur = conn.cursor()
cursur.execute("SELECT * FROM sravan_dataaa")

myresult = cursur.fetchall()
for x in myresult:
  print(x)

