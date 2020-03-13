from tkinter import *
from tkinter import ttk
import requests as req
import urllib as ulb
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
			self.master.rendering_engine(res)
		except Exception as e:
			self.load_errorpage()

	def load_errorpage(self):
		pass
