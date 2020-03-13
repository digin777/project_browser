import requests as req
import urllib as ulb
from tkinter import *
from tkinter import ttk
from tab import *

class Browser(Frame):
	def __init__(self,master=None):
		super().__init__(master)
		self.addwidgets()
		self.pack(fill=BOTH,expand=True)
	def addwidgets(self):
		self.window=Tab(self)
		self.window.pack(expand=True,fill=BOTH)
if __name__ == '__main__':
	root=Tk()
	root.geometry("800x500")
	root.minsize(300,520)
	app=Browser(root)
	app.mainloop()
