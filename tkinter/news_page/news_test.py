#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from PIL import Image, ImageTk
import tkinter,time,datetime
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
    root = tkinter.Tk()
    root.geometry('1920x1080')
    root.configure(background='black')
    root.attributes('-fullscreen',True)

    #CLOCK ###################################################################################
    clock = tkinter.Label(root,font=('verdana',100,'bold'),bg='black')
    clock.pack(anchor=NE)
    tick("", clock)
    
    ##########################################################################################

    #DATE ####################################################################################
    the_date = datetime.datetime.now().strftime('%m/%d')
    input_date = tkinter.Label(root,text=the_date,font=('verdana',100,'bold'),bg='black')
    input_date.place(x=0,y=0)
    
    ##########################################################################################

    #NEWS ####################################################################################
    img = ImageTk.PhotoImage(Image.open('news.png'))
    image = tkinter.Label(root,image=img,bg='black')
    image.pack(anchor=N,side=RIGHT)


#    d = feedparser.parse('https://news.google.com/news/rss/?ned=us&gl=US&hl=en')
    d = feedparser.parse('http://news.google.com/news?ned=us&output=rss')

    count = 1
    for post in d.entries[1:5]:
        print(post.title + "\n")
        headline = tkinter.Label(root,text=post.title + '\n',font=('verdana',17,'bold'),bg='black')
                
        headline.pack(side=TOP,anchor=W)

    
    
    ##########################################################################################


    root.mainloop()

if __name__ == "__main__":
    main()

