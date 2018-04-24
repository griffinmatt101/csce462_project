#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.font
import tkinter,time,datetime
import sys


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

    #DATE ####################################################################################
    the_date = datetime.datetime.now().strftime('%m/%d')
    input_date = tkinter.Label(root,text=the_date,font=('verdana',100,'bold'),fg='white',bg='black')
    input_date.place(x=0,y=0)

    
    ##########################################################################################

    compliment = tkinter.Label(root,text="You look beautiful today!",font=('DejaVu Serif',50,'italic'),fg='white',bg='black')
    compliment.pack(side=BOTTOM,anchor=S)

    root.mainloop()

if __name__ == "__main__":
    main()
