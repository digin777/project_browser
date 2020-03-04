import requests as requests
import urllib as ulb
from tkinter import *
from tkinter import ttk
class fsearch_bar(Frame):
	def __init__(self,master=None):
		self.master=master
		super().__init__(master)
		self.seach_box=Entry(self,height=10)
		self.seach_box.place(relwidth=0.95,relheight=0.98)
		self.seach_enbox=Entry(self,height=10)
		self.seach_enbox.place(relwidth=0.05,relheight=0.98)
class main_body(Frame):
	def __init__(self,master=None):
		super().__init__(master)
		self.addwidgets()
		self.pack(fill=BOTH,expand=True)
	def addwidgets(self):
		self.search_bar=fsearch_bar(self)
		self.search_bar.pack(fill=X,expand=True)
if __name__ == '__main__':
	root=Tk()
	app=main_body(root)
	app.mainloop()
