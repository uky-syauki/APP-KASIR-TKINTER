import tkinter as tk
from tkinter import *
from tkinter import ttk
import sql
import widget


class KELOLA_TOKO(tk.Frame):
     def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent)
          self.controller = controller
          self.ExecuteSQL = sql.SQL()
          self.Rp = widget.Rp()
          self.lbl_judul = widget.WIDGET(self,0)
          self.lbl_judul.Label_Judul("KELOLA TOKO")
          self.ruang = widget.WIDGET(self,1)
          for i in range(6):
               self.ruang.spasi()
          self.varKode = tk.StringVar()
          self.varNama = tk.StringVar()
          self.varModal = tk.IntVar()
          self.varHarga = tk.IntVar()
          self.lbl_barang = widget.WIDGET(self,2)
          self.lbl_barang.Label("Kode Barang")
          self.lbl_barang.Label("Nama Barang")
          self.lbl_barang.Label("Modal")
          self.lbl_barang.Label("Harga Barang")
          self.lbl_barang.Label("")
          self.entri_barang = widget.WIDGET(self,3)
          self.entri_barang.Entri(self.varKode)
          self.entri_barang.Entri(self.varNama)
          self.entri_barang.Entri(self.varModal)
          self.entri_barang.Entri(self.varHarga)
          self.entri_barang.Tombol(lambda:self.ExecuteQueri("barang"),"DAFTARKAN")
          self.lbl_stok = widget.WIDGET(self,4)
          self.varkodeStok = tk.StringVar()
          self.varTambahStok = tk.IntVar()
          self.lbl_stok.Label("Kode Barang")
          self.lbl_stok.Label("Tambah Stok")
          self.lbl_stok.Label("")
          self.lbl_stok.Label("")
          self.lbl_stok.Label("")
          self.entri_stok = widget.WIDGET(self,5)
          self.entri_stok.Entri(self.varkodeStok)
          self.entri_stok.Entri(self.varTambahStok)
          self.entri_stok.Label("")
          self.entri_stok.Label("")
          self.entri_stok.Tombol(lambda:self.ExecuteQueri("stok"),"+STOK")
          self.whitespace = widget.WIDGET(self,6)
          self.whitespace.spasi()
          tk.Label(self,text="DAFTAR BARANG",font="arial 15 bold",relief=tk.SUNKEN).grid(row=7,column=0,columnspan=3,sticky="EW")
          self.tampilkan()
     def tampilkan(self,sts = "biasa"):
          style = ttk.Style()
          style.configure("mystyle1.Treeview", highlightthickness=0, bd=0, font=('Arial', 9)) # Modify the font of the body
          style.configure("mystyle1.Treeview.Heading", font=('Calibri', 12,'bold')) # Modify the font of the headings
          style.layout("mystyle1.Treeview", [('mystyle1.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
          myTable = ttk.Treeview(self,style='mystyle1.Treeview',height=20)
          myTable['columns'] = ('c1','c2','c3','c4','c5','c6')
          myTable.column("#0",width=0, stretch=NO)
          myTable.column('c1',anchor=W, width=20)
          myTable.column('c2',anchor=W, width=90)
          myTable.column('c3',anchor=W, width=160)
          myTable.column('c4',anchor=W, width=60)
          myTable.column('c5',anchor=W, width=60)
          myTable.column('c6',anchor=W, width=25)
          # heading
          myTable.heading("#0",text="",anchor=W)
          myTable.heading("c1",text="Id",anchor=W)
          myTable.heading("c2",text="kode barang",anchor=W)
          myTable.heading("c3",text="nama barang",anchor=W)
          myTable.heading("c4",text="modal",anchor=W)
          myTable.heading("c5",text="harga",anchor=W)
          myTable.heading("c6",text="stok",anchor=W)
          hasil = self.ExecuteSQL.stmt_with_return("SELECT barang.kode_barang,nama_barang,modal,harga_barang,stok.tersedia FROM barang,stok WHERE barang.kode_barang=stok.kode_barang")
          if sts == "cari":
               for i in range(len(hasil)):
                    if self.varCari.get() in hasil[i][1]:
                         myTable.insert(parent='',index='end',iid=i,text='',values=(f'{i+1}',f'{hasil[i][0]}',f'{hasil[i][1]}',f'Rp {self.Rp.Rupiah(hasil[i][2])}',f'Rp {self.Rp.Rupiah(hasil[i][3])}',f"{hasil[i][4]}"))
                    else:
                         pass
          else:
               for i in range(len(hasil)):
                    myTable.insert(parent='',index='end',iid=i,text='',values=(f'{i+1}',f'{hasil[i][0]}',f'{hasil[i][1]}',f'Rp {self.Rp.Rupiah(hasil[i][2])}',f'Rp {self.Rp.Rupiah(hasil[i][3])}',f"{hasil[i][4]}"))
          myTable.grid(row=8,column=0,columnspan=3,sticky="NESW")
          self.cari = widget.WIDGET(self,9)
          self.varCari = tk.StringVar()
          self.cari.Label("Cari Barang")
          self.cari.Entri(self.varCari)
          self.cari.Tombol(lambda:self.tampilkan("cari"),"Cari")
     def ExecuteQueri(self,table):
          if table == "barang":
               if len(self.varKode.get()) > 2 and len(self.varNama.get()) > 5 and self.varModal.get() > 100 and self.varHarga.get() > 500:
                    queriS = f"INSERT INTO {table} VALUES ('{self.varKode.get()}','{self.varNama.get()}',{self.varModal.get()},{self.varHarga.get()})"
                    self.ExecuteSQL.stmt_not_return(queriS)
                    self.ExecuteSQL.stmt_not_return(f"INSERT INTO stok VALUES ('{self.varKode.get()}',0)")
                    tk.Label(self, text="Berhasil..", fg="green", font="arial 10 bold",relief=tk.SUNKEN,width=20).grid(row=2,column=4,sticky="EW")
                    self.refres()
               else:
                    tk.Label(self, text="periksa input..", fg="red", font="arial 10 bold",relief=tk.SUNKEN,width=20).grid(row=2,column=4,sticky="EW")
          elif table == "stok":
               if len(self.varkodeStok.get()) > 2 and self.varTambahStok.get() > 0:
                    before = self.ExecuteSQL.stmt_with_return(f"SELECT tersedia from stok WHERE kode_barang = '{self.varkodeStok.get()}'")
                    queriS = f"UPDATE {table} SET tersedia = {before[0][0] + self.varTambahStok.get()} WHERE kode_barang = '{self.varkodeStok.get()}'"
                    self.ExecuteSQL.stmt_not_return(queriS)
                    tk.Label(self, text="Berhasil..", fg="green", font="arial 10 bold",relief=tk.SUNKEN,width=20).grid(row=4,column=4,sticky="EW")
                    self.refres()
               else:
                    tk.Label(self, text="periksa input..", fg="red", font="arial 10 bold",relief=tk.SUNKEN,width=20).grid(row=4,column=4,sticky="EW")
     def refres(self):
          self.tampilkan()
          self.varHarga.set(0)
          self.varKode.set("")
          self.varNama.set("")
          self.varModal.set(0)
          self.varkodeStok.set("")
          self.varTambahStok.set(0)
