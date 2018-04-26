#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
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
    root.geometry('1050x1680') 
    root.configure(background='black')
    root.attributes('-fullscreen',True)

    #CLOCK ###################################################################################
    clock = tkinter.Label(root,font=('verdana',100,'bold'),fg='white',bg='black')
    clock.pack(anchor=NE)
    tick("", clock)
    
    ##########################################################################################


    #NEWS ####################################################################################
    d = feedparser.parse('http://news.google.com/news?ned=us&output=rss')

   
    
    i=0
    for post in d.entries[1:6]:
        
        word = post.title
        source = word.split(" - ")
        wordlen = len(source)-1
        news_headline = source[0]
        print(len(news_headline))
        
        if(post == d.entries[1]):
            news_headline = "hello hi howdy this is a test to see if it works. e world to know it"
            if(len(news_headline)-1+len(source[1]) >= 110):
                subtract = len(source[1]) + 3
                news_headline = news_headline[:110-subtract] + "... - "
            news_headline = news_headline + ' - ' + source[1]
            line1 = news_headline[:35]
            
            line2 = news_headline[35:70]
            line3 = news_headline[70:]
            print(line1)
            print(line2)
            print(line3)
            headline_line1 = tkinter.Label(root,text=line1 +  '\n',font=('verdana',25),fg='white',bg='black')
            headline_line2 = tkinter.Label(root,text=line2 +  '\n',font=('verdana',25),fg='white',bg='black') 
            headline_line3 = tkinter.Label(root,text=line3 + '\n',font=('verdana',25),fg='white',bg='black')
            headline_line1.place(x=5,y=5)
            headline_line2.place(x=5, y=40)
            headline_line3.place(x=5, y=75)
        else:
            if(len(news_headline)-1 >= 75):
                news_headline = news_headline[:75 ] + "..."
            headline = tkinter.Label(root,text= str(i) + ". "+ news_headline[:78] + " - " + source[1] +  '\n',font=('verdana',15),fg='white',bg='black')
            headline.pack(side=TOP,anchor=W)
        i = i+ 1

    
    
    ##########################################################################################


    root.mainloop()

if __name__ == "__main__":
    main()
