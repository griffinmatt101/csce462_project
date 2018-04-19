#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter,time,datetime

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

    #CLOCK
    clock = tkinter.Label(root,font=('times',45,'bold'),bg='black')
    clock.pack(anchor=NE,pady=.1)
    tick("", clock)

    #DATE
    the_date = datetime.date.today().strftime('%A') + ', ' + datetime.date.today().strftime('%B') + " " + datetime.date.today().strftime('%d')
    input_date = tkinter.Label(root,text=the_date,font=('times',31,'bold'),bg='black')
    input_date.pack(anchor=NE,pady=.1)

    #WEATHER
#    img = PhotoImage(file='id10.gif')
#    panel = tkinter.Label(root,image=img,bg='black')
#    panel.place(x=0,y=0)
    

    root.mainloop()

if __name__ == "__main__":
    main()
