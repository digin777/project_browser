import requests as req
import urllib as ulb
from tkinter import *
from tkinter import ttk
class fsearch_bar(Frame):
	def __init__(self,master=None):
		self.master=master
		super().__init__(master)
		self.config({"height":23})
		self.seach_box=Entry(self)
		self.seach_box.bind("<Key-Return>",self.search)
		self.seach_box.place(relx=0.001,rely=0,relwidth=0.88,relheight=0.98)
		self.seach_enbox=Entry(self)
		self.seach_enbox.place(relx=0.89,rely=0,relwidth=0.198,relheight=0.98)
	def search(self,event):
		try:
			url=self.seach_box.get()
			if not url.startswith(("http://","https://")):
				url="http://"+url
			res=req.get(url)
			print(res.text)
		except Exception as e:
			print(e)

class main_body(Frame):
	def __init__(self,master=None):
		super().__init__(master)
		self.addwidgets()
		self.pack(fill=BOTH,expand=True)
	def addwidgets(self):
		self.window=ttk.Notebook(self)
		self.fwindow=Frame(self.window)
		self.fpwindow=Frame(self.fwindow)
		self.fwindow.place(relx=0,rely=0,relwidth=1)
		self.window.add(self.fwindow,text="New Tab")
		self.window.pack(expand=True,fill=BOTH)
		self.search_bar=fsearch_bar(self.window)
		self.search_bar.place(relx=0,rely=0.035,relwidth=1)
		self.fpwindow.place(relx=0,rely=0.040,relwidth=1,relheight=1)
if __name__ == '__main__':
	root=Tk()
	root.geometry("800x500")
	root.minsize(300,520)
	app=main_body(root)
	app.mainloop()
