import tkinter as tk
import penjualan
import kelola_barang
import widget
import statistik


class Aplikasi(tk.Tk):
     def __init__(self, *args, **kwargs):
          tk.Tk.__init__(self, *args, **kwargs)
          frameMenu = tk.Frame(self)
          frameMenu.grid(row=0,column=0,sticky="NS")
          MENU(parent=frameMenu,controller=self).grid(row=0,column=0)
          frameSide = tk.Frame(self)
          frameSide.grid(row=0,column=1)
          self.frames = {}
          for page in (penjualan.PENJUALAN,statistik.STATISTIK,kelola_barang.KELOLA_TOKO):
               nama = page.__name__
               frame = page(parent=frameSide,controller=self)
               self.frames[nama] = frame
               frame.grid(row=0,column=0,rowspan=10,sticky="NESW")
          self.show_frame("PENJUALAN")
     def show_frame(self, name_page):
          frame = self.frames[name_page]
          frame.tkraise()


class MENU(tk.Frame):
     def __init__(self, parent, controller):
          tk.Frame.__init__(self, parent,relief=tk.SUNKEN)
          self.controller = controller
          self.judul = widget.WIDGET(self,0)
          self.judul.Label("MENU")
          tk.Button(self,text="STATISTIK",bg="lightgreen",font="arial 10 bold",width=15,relief=tk.SUNKEN,command=lambda:self.ganti("STATISTIK")).grid(row=1,column=0)
          tk.Button(self,text="KELOLA TOKO",bg="lightgreen",font="arial 10 bold",width=15,relief=tk.SUNKEN,command=lambda:self.ganti("KELOLA_TOKO")).grid(row=2,column=0)
          tk.Button(self,text="PENJUALAN",bg="lightgreen",font="arial 10 bold",width=15,relief=tk.SUNKEN,command=lambda:self.ganti("PENJUALAN")).grid(row=3,column=0)
          tk.Button(self,text="EXIT",bg="red",font="arial 10 bold",width=15,relief=tk.SUNKEN,command=self.quit).grid(row=4,column=0)
     def ganti(self,nama_page):
          self.controller.show_frame(nama_page)

                                   


if __name__ == "__main__":
     APP = Aplikasi()
     lebar = APP.winfo_screenwidth()
     tinggi = APP.winfo_screenheight()
     APP.geometry(f"{lebar-66}x{tinggi}")
     APP.mainloop()