from tkinter import *
import locale,threading,time
import requests,json,traceback
import feedparser


news_country_code = 'us'

def __init__(self,parent,*args,**kwargs):
    Frame.__init__(self,parent,*args,**kwargs)
    self.config(bg='black')
    self.title='News Page'
    self.newsLbl = Label(self,text=self.title,font=('verdana',30,'bold'),bg='black')
    self.newsLbl.pack(side=TOP, anchor=W)
    self.headlinesContainer = Frame(self, bg="black")
    self.headlinesContainer.pack(side=TOP)
    self.headlines()

def main():
    root = tkinter.Tk()
    root.geometry('1920x1080')

    try:
        #for widget in self.headlinesContainer.winfo_children():
        #    widget.destroy()
        if news_country_code == None:
            headlines_url = "https://news.google.com/news?ned=us&output=rss"
        else:
            headlines_url = "https://news.google.com/news?ned=%s&output=rss" % news_country_code

        feed = feedparser.parse(headlines_url)

        for post in feed.entries[0:5]:
            #headline = NewsHeadline(self.headlinesContainer, post.title)
            headline = Label(root,text=post.title,font=('verdana',30,'bold'),bg='black')
            headline.pack(side=TOP, anchor=W)

    except Exception as e:

        traceback.print_exc()
        print ("Error: %s. Cannot get news." % e)

    self.after(600000, main())

    root.mainloop()

if '__name__' == '__main__':
    main()
