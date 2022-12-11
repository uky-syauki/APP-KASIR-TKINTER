import sqlite3

class SQL:
     def __init__(self):
          try:
               file = open("data.db","a")
          except:
               pass
          self.hubung = sqlite3.connect("data.db")
          self.cursor = self.hubung.cursor()
          print("Connection...")
     def stmt_not_return(self,queri):
          self.cursor.execute(queri)
          self.hubung.commit()
     def stmt_with_return(self, queri):
          self.cursor.execute(queri)
          hasil = self.cursor.fetchall()
          return hasil
               

