import requests as req
import urllib as ulb
from tkinter import *
from tkinter import ttk
from searchbar import *
from bs4 import BeautifulSoup as bs
class Tab(ttk.Notebook):
	def __init__(self,master):
		super().__init__(master)
		self.master=master
		self.addwidgets()

	def addwidgets(self):
		self.fwindow=Frame(self)
		#self.fpwindow=Frame(self.fwindow,bg="white")
		self.fwindow.place(relx=0,rely=0,relwidth=1)
		self.add(self.fwindow,text="New Tab")
		self.search_bar=fsearch_bar(self)
		self.search_bar.place(relx=0,rely=0.035,relwidth=1)
		#self.fpwindow.place(relx=0,rely=0.040,relwidth=1,relheight=1)
		canvas = Canvas(self.fwindow,bg="white")
		scrollbary = Scrollbar(self, orient="vertical", command=canvas.yview)
		scrollbarx = Scrollbar(self, orient="horizontal", command=canvas.xview)
		self.mbody=Frame(canvas)
		self.mbody.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            ))
		canvas.create_window((0, 0), window=self.mbody, anchor="nw")
		canvas.configure(yscrollcommand=scrollbary.set)
		canvas.configure(xscrollcommand=scrollbarx.set)
		scrollbarx.pack(side="bottom", fill="x")
		scrollbary.pack(side="right", fill="y")
		canvas.place(relx=0,rely=0.040,relwidth=1,relheight=1)
	def rendering_engine(self,res):
		print("call d")
		self.rendering(res)
		if res.statuscode==200:
			self.rendering(res)
		else:
			self.rendering(res)

	def rendering(self,res):
		html_doc=res.text
		soup = bs(html_doc, 'html.parser')
		self.tab (self.fwindow, text = soup.title.string)
		body=soup.find('body')
		root_childs = [e.name for e in body.children if e.name is not None]
		x=self.finding_children(body.children)
		print(x)
	
	def finding_children(self,childrens):
		for child  in childrens:
			if child.children is not None:
				print("child")
				self.finding_children(child.children)
			else:
				if children.name=="input":
					if children["type"]=="text":
						return Entry()
					elif children["type"]=="button":
						return Button()

			
		

