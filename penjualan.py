import tkinter as tk
from tkinter import *
from tkinter import CENTER, ttk
import widget
import sql


class PENJUALAN(tk.Frame):
     def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent,relief=tk.SUNKEN)
          self.controller = controller
          self.sqlExecute = sql.SQL()
          self.lbl_judul = widget.WIDGET(self,0)
          self.lbl_judul.Label_Judul("PENJUALAN")
          self.spasi = widget.WIDGET(self,1)
          for i in range(6):
               self.spasi.spasi()
          self.lbl_input = widget.WIDGET(self,2)
          self.lbl_input.Label("Kode Barang")
          self.lbl_input.Label("Nama Pembeli")
          tk.Label(self, text="...", fg="green", font="arial 10 bold",relief=tk.SUNKEN,width=20).grid(row=2,column=2,sticky="EW")
          self.entri_input = widget.WIDGET(self,3)
          self.varKode = tk.StringVar()
          self.varNama = tk.StringVar()
          self.entri_input.Entri(self.varKode)
          self.entri_input.Entri(self.varNama)
          self.entri_input.Tombol(lambda:self.ExecuteQueri(),"Kirim")
          self.whitespace = widget.WIDGET(self,4)
          self.whitespace.spasi()
          self.ruang = widget.WIDGET(self,5)
          self.varDay = tk.StringVar()
          self.ruang.Label("Terjual")
          self.ruang.Entri(self.varDay)
          self.ruang.Tombol(lambda:self.table("custom"),"Tampilkan")
          self.table()
     def table(self,hari = "semua"):
          style = ttk.Style()
          style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Arial', 11)) # Modify the font of the body
          style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
          style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
          myTable = ttk.Treeview(self,style='mystyle.Treeview',height=20)
          myTable['columns'] = ('c1','c2','c3','c4')
          myTable.column("#0",width=0, stretch=NO)
          myTable.column('c1',anchor=CENTER, width=30)
          myTable.column('c2',anchor=CENTER, width=80)
          myTable.column('c3',anchor=CENTER, width=120)
          myTable.column('c4',anchor=CENTER, width=80)
          # heading
          myTable.heading("#0",text="",anchor=CENTER)
          myTable.heading("c1",text="Id Tr",anchor=CENTER)
          myTable.heading("c2",text="tanggal",anchor=CENTER)
          myTable.heading("c3",text="barang",anchor=CENTER)
          myTable.heading("c4",text="pembeli",anchor=CENTER)
          if hari == "semua":
               hasil = self.sqlExecute.stmt_with_return("SELECT terjual.tanggal_jual,barang.nama_barang,terjual.nama_pembeli FROM terjual,barang WHERE terjual.kode_barang=barang.kode_barang")
          elif hari == "sekarang":
               hasil = self.sqlExecute.stmt_with_return("SELECT terjual.tanggal_jual,barang.nama_barang,terjual.nama_pembeli FROM terjual,barang WHERE terjual.kode_barang=barang.kode_barang and terjual.tanggal_jual = date('now')")
          elif hari == 'custom':
               if len(self.varDay.get()) < 9:
                    hasil = self.sqlExecute.stmt_with_return("SELECT terjual.tanggal_jual,barang.nama_barang,terjual.nama_pembeli FROM terjual,barang WHERE terjual.kode_barang=barang.kode_barang")
               else:
                    hasil = self.sqlExecute.stmt_with_return(f"SELECT terjual.tanggal_jual,barang.nama_barang,terjual.nama_pembeli FROM terjual,barang WHERE terjual.kode_barang=barang.kode_barang and terjual.tanggal_jual = '{self.varDay.get()}'")
          for i in range(len(hasil)):
               num = len(hasil)
               myTable.insert(parent='',index='end',iid=i,text='',values=(f'{num-i}',f'{hasil[-(i+1)][0]}',f'{hasil[-(i+1)][1]}',f'{hasil[-(i+1)][2]}'))
          myTable.grid(row=6,column=0,columnspan=3,sticky="NESW")
     def ExecuteQueri(self):
          if len(self.varKode.get()) > 2 and len(self.varNama.get()) > 2:
               kode_barang = self.sqlExecute.stmt_with_return("SELECT kode_barang FROM barang")
               if self.varKode.get() in str(kode_barang): 
                    queri = f"INSERT INTO terjual VALUES (date('now'),'{self.varKode.get()}','{self.varNama.get()}')"
                    self.sqlExecute.stmt_not_return(queri)
                    before = self.sqlExecute.stmt_with_return(f"SELECT tersedia from stok WHERE kode_barang = '{self.varKode.get()}'")
                    if str(self.varKode.get())[0] == "P":
                         pass
                    else:
                         self.sqlExecute.stmt_not_return(f"UPDATE stok SET tersedia = {before[0][0] - 1} WHERE kode_barang = '{self.varKode.get()}'")
                    tk.Label(self, text="Berhasil...", fg="green", font="arial 10 bold",relief=tk.SUNKEN,width=20).grid(row=2,column=2,sticky="EW")
                    self.kosong()
                    self.table()
               else:
                    tk.Label(self, text="Kode salah..", fg="red", font="arial 10 bold",relief=tk.SUNKEN,width=20).grid(row=2,column=2,sticky="EW")
          else:
               tk.Label(self, text="Periksa input..", fg="red", font="arial 10 bold",relief=tk.SUNKEN,width=20).grid(row=2,column=2,sticky="EW")
     def kosong(self):
          self.varKode.set("")
          self.varNama.set("")


