#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter
import time

def tick(time_old, clock):
    # get the current local time from the PC
    time_now = time.strftime('%I:%M:%S')
    # if time string has changed, update it
    if time_now != time_old:
        time_old = time_now
        clock.config(text = time_now)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick, time_old, clock)

def date_tick(date_old,date):
    date_now = time.strftime('%m/%d/%Y/')
    if date_now != date_old:
        date_old = date_now
        date.config(text=date_now)
    date.after(20000000,date_tick,date_old,date)

def main():
    root = tkinter.Tk()
    root.geometry('1920x1080')

 #   back = tkinter.Label(root,bg='black')
 #   back.pack(fill=tkinter.BOTH,expand=1)

    clock = tkinter.Label(root,font=('times',35,'bold'),bg='black')
#    clock.place(x=1780,y=1)
    clock.pack(anchor=NE,pady=1)
    tick("", clock)

    date = tkinter.Label(root,font=('times',21,'bold'),bg='black')
    date.pack(anchor=NE,pady=1)
    date_tick("",date)

    root.mainloop()

if __name__ == "__main__":
    main()
