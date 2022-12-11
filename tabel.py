from tkinter import *
from  tkinter import ttk


ws  = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


my_game = ttk.Treeview(game_frame,style='mystyle.Treeview')

my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("player_id",anchor=CENTER, width=80)
my_game.column("player_name",anchor=CENTER,width=80)
my_game.column("player_Rank",anchor=CENTER,width=80)
my_game.column("player_states",anchor=CENTER,width=80)
my_game.column("player_city",anchor=CENTER,width=80)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("player_id",text="Id",anchor=CENTER)
my_game.heading("player_name",text="Name",anchor=CENTER)
my_game.heading("player_Rank",text="Rank",anchor=CENTER)
my_game.heading("player_states",text="States",anchor=CENTER)
my_game.heading("player_city",text="States",anchor=CENTER)

my_game.insert(parent='',index='end',iid=0,text='',
values=('1','Ninja','101','Oklahoma', 'Moore'), tags=('odd',))
my_game.insert(parent='',index='end',iid=1,text='',
values=('2','Ranger','102','Wisconsin', 'Green Bay'))
my_game.insert(parent='',index='end',iid=2,text='',
values=('3','Deamon','103', 'California', 'Placentia'))
my_game.insert(parent='',index='end',iid=3,text='',
values=('4','Dragon','104','New York' , 'White Plains'))
my_game.insert(parent='',index='end',iid=4,text='',
values=('5','CrissCross','105','California', 'San Diego'))
my_game.insert(parent='',index='end',iid=5,text='',
values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
my_game.insert(parent='',index='end',iid=6,text='',
values=('7','Deamon','103', 'California', 'Placentia'))
my_game.insert(parent='',index='end',iid=7,text='',
values=('8','Dragon','104','New York' , 'White Plains'))
my_game.insert(parent='',index='end',iid=8,text='',
values=('9','CrissCross','105','California', 'San Diego'))
my_game.insert(parent='',index='end',iid=9,text='',
values=('10','ZaqueriBlack','106','Wisconsin' , 'TONY'))
my_game.insert(parent='',index='end',iid=10,text='',
values=('11','Deamon','103', 'California', 'Placentia'))
my_game.insert(parent='',index='end',iid=11,text='',
values=('12','Dragon','104','New York' , 'White Plains'))
my_game.insert(parent='',index='end',iid=12,text='',
values=('13','CrissCross','105','California', 'San Diego'))
my_game.insert(parent='',index='end',iid=13,text='',
values=('14','ZaqueriBlack','106','Wisconsin' , 'TONY'))

my_game.tag_configure('odd', background='#E8E8E8')
my_game.tag_configure('even', background='#DFDFDF')

my_game.pack()

ws.mainloop()
