import tkinter as tk
from tkinter import *
from tkinter import ttk
import widget
import sql

class STATISTIK(tk.Frame):
     def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          self.frameKanan = tk.Frame(self)
          self.frameKanan.grid(row=5,column=3)
          self.controller = controller
          self.sqlExecute = sql.SQL()
          self.judul = widget.WIDGET(self,0).Label_Judul("STATISTIK TOKO")
          self.spasi = widget.WIDGET(self,1)
          for i in range(7):
               self.spasi.spasi()
          self.refres = widget.WIDGET(self,2)
          self.refres.Tombol(lambda:self.tampilkan(),"Muat Ulang")
          self.tampilkan()
     def tampilkan(self):
          style = ttk.Style()
          style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Arial', 11)) # Modify the font of the body
          style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
          style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
          myTable = ttk.Treeview(self,style='mystyle.Treeview',height=30)
          myTable['columns'] = ('c1','c2','c3','c4')
          myTable.column("#0",width=0, stretch=NO)
          myTable.column('c1',anchor=CENTER, width=30)
          myTable.column('c2',anchor=CENTER, width=120)
          myTable.column('c3',anchor=CENTER, width=30)
          myTable.column('c4',anchor=CENTER, width=80)
          myTable.heading("#0",text="",anchor=CENTER)
          myTable.heading("c1",text="Id",anchor=CENTER)
          myTable.heading("c2",text="nama barang",anchor=CENTER)
          myTable.heading("c3",text="terjual",anchor=CENTER)
          myTable.heading("c4",text="total",anchor=CENTER)
          modal = self.sqlExecute.stmt_with_return("SELECT sum(barang.harga_barang-barang.modal) from barang,terjual where barang.kode_barang=terjual.kode_barang")
          hasil = self.sqlExecute.stmt_with_return("SELECT barang.nama_barang, sum(terjual.kode_barang+1) as total, sum(barang.harga_barang) as uang from terjual,barang where barang.kode_barang=terjual.kode_barang group by terjual.kode_barang")
          total_uang = 0
          for i in range(len(hasil)):
               myTable.insert(parent='',index='end',iid=i,text='',values=(f'{i+1}',f'{hasil[i][0]}',f'{hasil[i][1]}',f'{self.toString(hasil[i][2])}'))
               total_uang += hasil[i][2]
          myTable.grid(row=5,column=0,rowspan=30,columnspan=3,sticky="NESW")
          tk.Label(self.frameKanan,text=f"Total Uang : {self.toString(total_uang)}",font="arial 11 bold",relief=tk.SUNKEN,width=20).grid(row=5,column=3,sticky="NW")
          tk.Label(self.frameKanan,text=f"Keuntungan : {self.toString(modal[0][0])}",font="arial 11 bold",relief=tk.SUNKEN,width=20).grid(row=6,column=3,sticky="NW")
     def toString(self,angka):
          if angka <= 999999:
               smp1 = str(angka)[:-3]
               smp =smp1+ "."+str(angka)[-3:]
          elif angka > 999999 and angka <= 999999999:
               smp1 = str(angka)[-3:]
               smp2 = str(angka)[-6:-3]
               smp3 = str(angka)[:-6]
               smp = smp3+"."+smp2+"."+smp1
          elif angka > 999999999 and angka <= 999999999999:
               smp1 = str(angka)[-3:]
               smp2 = str(angka)[-6:-3]
               smp3 = str(angka)[-9:-6]
               smp4 = str(angka)[:-9]
               smp = smp4+"."+smp3+"."+smp2+"."+smp1
          else:
               smp = str(angka)
          return smp
