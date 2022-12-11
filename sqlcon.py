import sqlite3

class DATABASE:
     def __init__(self,table):
          self.table = table
          open("data.db",'a')
          self.con = sqlite3.connect("data.db")
          self.cursor = self.con.cursor()
     def INSERT(self,*data):
          queri = f"INSERT INTO {self.table} VALUES {data}"
          print(queri)
          self.cursor.execute(queri)
     def SELECT(self,stmt):
          queri = f"SELECT {stmt} FROM {self.table}"
          print(queri)
          self.cursor.execute(queri)
          return self.cursor.fetchall()
     def SELECT_WHERE(self,stmt,kode,key):
          queri = f"SELECT {stmt} FROM {self.table} WHERE {kode}='{key}'"
          print(queri)
          self.cursor.execute(queri)
          return self.cursor.fetchall()
     def SELECT_UNION(self,stmt,join,kondisi):
          queri = f"SELECT {stmt} from {self.table},{join} WHERE {kondisi}"
          print(queri)
          self.cursor.execute(queri)
     def UPDATE(self,col,nilai,key):
          queri = f"UPDATE {self.table} SET {col}={nilai} WHERE kode_barang='{key}'"
          print(queri)
          self.cursor.execute(queri)
     def UPDATE_TAMBAH(self,col,nilai,key):
          before = self.SELECT_WHERE(col,"kode_barang",key)
          print(before[0][0])
          queri = f"UPDATE {self.table} SET {col}={nilai+before[0][0]} WHERE kode_barang='{key}'"
          print(queri)
          self.cursor.execute(queri)
          self.con.commit()




barang = DATABASE("barang")
terjual = DATABASE("terjual")
stok = DATABASE("stok")

stok.UPDATE_TAMBAH("tersedia",4,"KXL4D")