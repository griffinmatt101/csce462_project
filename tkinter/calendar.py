#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter
import time
import datetime

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

 #   back = tkinter.Label(root,bg='black')
 #   back.pack(fill=tkinter.BOTH,expand=1)

    #CLOCK
    clock = tkinter.Label(root,font=('times',41,'bold'),bg='black')
    clock.pack(anchor=NE)
    tick("", clock)

    #DATE
    the_date = datetime.datetime.now().strftime('%m/%d')
    input_date = tkinter.Label(root,text=the_date,font=('times',41,'bold'),bg='black')
    input_date.place(x=0,y=0)

    root.mainloop()

if __name__ == "__main__":
    main()
