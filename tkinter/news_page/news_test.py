#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk
import Tkinter,time,datetime
import sys
#import events
import feedparser
from subprocess import check_output


def tick(time_old, clock):
    # get the current local time from the PC
    time_now = time.strftime('%I:%M')
    # if time string has changed, update it
    if time_now != time_old:
        time_old = time_now
        clock.config(text = time_now)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick, time_old, clock)


def main():
    root = Tkinter.Tk()
    root.geometry('1920x1080')
    root.configure(background='black')
    root.attributes('-fullscreen',True)

    #CLOCK ###################################################################################
    clock = Tkinter.Label(root,font=('verdana',100,'bold'),fg="white",bg='black')
    clock.pack(anchor=NE)
    tick("", clock)
    
    ##########################################################################################

    #DATE ####################################################################################
    the_date = datetime.datetime.now().strftime('%m/%d')
    input_date = Tkinter.Label(root,text=the_date,font=('verdana',100,'bold'),fg="white",bg='black')
    input_date.place(x=0,y=0)
    
    ##########################################################################################

    #NEWS ####################################################################################
    img = ImageTk.PhotoImage(Image.open('news.png'))
    image = Tkinter.Label(root,image=img,bg='black')
    image.pack(anchor=N,side=RIGHT)


#    d = feedparser.parse('https://news.google.com/news/rss/?ned=us&gl=US&hl=en')
    d = feedparser.parse('http://news.google.com/news?ned=us&output=rss')

    count = 1
    i = 1
    for post in d.entries[1:6]:
        word = post.title
        source = word.split(" - ")
        wordlen = len(source)-1
        news_headline = source[0]
        news_source = source[1]
        if((len(news_headline)-1 + len(news_source)) >= 75):
            subtract = len(source[1]) + 3
            news_headline = news_headline[:75-subtract] + "..."
        headline = Tkinter.Label(root,text= str(i) + ". "+ news_headline + " - " + source[1] +  '\n',font=('verdana',14),fg='white',bg='black')
        headline.pack(side=TOP,anchor=W)
            
        i = i + 1
#print(post.title + "\n")
 #       headline = tkinter.Label(root,text=post.title + '\n',font=('verdana',17,'bold'),fg="white",bg='black')
                
  #      headline.pack(side=TOP,anchor=W)

    
    
    ##########################################################################################


    root.mainloop()

if __name__ == "__main__":
    main()

