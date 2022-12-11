import tkinter as tk

class WIDGET:
     def __init__(self,induk,baris,colom=0):
          self.frame = induk
          self.baris = baris
          self.colom = colom
     def spasi(self):
          tk.Label(self.frame,text="",width=20).grid(row=self.baris,column=self.colom,sticky="NESW")
          self.colom += 1
     def Label_Judul(self,tex):
          tk.Label(self.frame, text=tex,font="arial 20 bold",width=30).grid(row=self.baris,column=self.colom,columnspan=12,sticky="NESW")
          self.colom += 1
     def Label(self,tex):
          tk.Label(self.frame, text=tex, font="arial 10 bold",relief=tk.SUNKEN,width=20).grid(row=self.baris,column=self.colom,sticky="NESW")
          self.colom += 1
     def Entri(self,vatTex):
          tk.Entry(self.frame,textvariable=vatTex,font="arial 10 bold",relief=tk.SUNKEN,width=20).grid(row=self.baris,column=self.colom,sticky="NESW")
          self.colom += 1
     def Tombol(self,com,nama = "Execute"):
          tk.Button(self.frame,text=nama,font="arial 10 bold",bg="lightgreen",relief=tk.SUNKEN,command=com).grid(row=self.baris,column=self.colom,sticky="EW")
          self.colom += 1

class Rp:
     def __init__(self):
          pass
     def Rupiah(self,angka):
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