import tkinter as tk
import menu

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container1 = tk.Frame(self)
        container1.grid(row=0,column=0)
        container = tk.Frame(self)
        container.grid(row=0,column=1)
        self.frames = {}
        for F in (menu.MENU,side2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0,column=0,sticky='NESW')
        menuSide = side1(parent=container1,controller=self)
        self.frames['side1'] = menuSide
        menuSide.grid(row=0,column=0,sticky='NESW')
        self.show_frame("MENU")
    def sideMenu(self):
        self.show_frame("side1")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



class side1(tk.Frame):
     def __init__(self,parent, controller):
          tk.Frame.__init__(self, parent)
          self.controller = controller
          tk.Button(self,text="This Frame side1",font="arial 10 bold",command=lambda:self.controller.show_frame("side2")).grid(row=0,column=0)
          tk.Button(self,text="container1",font="arial 10 bold",command=lambda:self.controller.show_frame("MENU")).grid(row=1,column=0)
          tk.Label(self,text="container1",font="arial 10 bold").grid(row=2,column=0)
          tk.Label(self,text="container1",font="arial 10 bold").grid(row=3,column=0)
          for i in range(4,10):
              tk.Label(self,text=f"Label {i+4}",font="arial 10 bold").grid(row=i,column=0)


class side2(tk.Frame):
     def __init__(self,parent, controller):
          tk.Frame.__init__(self, parent)
          self.controller = controller
          tk.Label(self,text="This Frame side2",font="arial 10 bold").grid(row=0,column=0)


if __name__ == '__main__':
    APP = Application()
    lebar = APP.winfo_screenwidth()
    tinggi = APP.winfo_screenheight()
    print(lebar, tinggi)
    APP.geometry(f"{lebar-66}x{tinggi}")
    APP.title("Hello Dunia")
    APP.mainloop()