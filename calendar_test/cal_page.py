#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from PIL import Image, ImageTk
import tkinter
import time
import datetime
import sys
import events

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
    clock = tkinter.Label(root,font=('verdana',100,'bold'),fg='white',bg='black')
    clock.pack(anchor=NE)
    tick("", clock)
    
    ##########################################################################################

    #DATE ####################################################################################
    the_date = datetime.datetime.now().strftime('%m/%d')
    input_date = tkinter.Label(root,text=the_date,font=('verdana',100,'bold'),fg='white',bg='black')
    input_date.place(x=0,y=0)
    
    ##########################################################################################

    #GOOGLE CALENDAR #########################################################################
    img = ImageTk.PhotoImage(Image.open('calendar_image.png'))
    image = tkinter.Label(root,image=img,bg='black')
#    image = image.resize((250,250),Image.ANTIALIAS)
    image.pack(anchor=N,side=RIGHT)


    events.main(sys.argv)

    f = open('event_list.txt','r')
    line = f.readline()
    count = 1

    eventarray = []

    while line:
        eventarray.append(line)
        line = f.readline()
        count += 1

    event_len = len(eventarray)
    if(event_len > 4):
        for x in range(0,4):

            event_sub = eventarray[x]
            event_split = event_sub.split(' ')
            event_split_len = len(event_split)
            #EXAMPLE: ['2018-04-26T22:40:00-05:00', 'AVENGERS:', 'INFINITY', 'WAR\n']                                        ['2018-04-28', 'Kawhi', 'Leonard', 'Shoes!!!\n']

            event_date = event_split[0]
            event_date_len = len(event_date)

            if(not(event_date_len > 10)):

                event_date = event_date.split('-')
                event_date = event_date[1] + '/' + event_date[2]

                event_text = ''
                for x in range(1,event_split_len):
                    event_text = event_text + ' ' + event_split[x] + ' '

                event_text = event_date + ' - ' + event_text
                event1 = tkinter.Label(root,text=event_text,font=('verdana',20,'bold'),fg='white',bg='black')

                event1.pack(anchor=W)

            else:
                event_datetime = event_date.split('T')
                event_datetime_colon = event_datetime[1].split(':')
                edc_hour = int(event_datetime_colon[0])
                edc_setting = 'am'
                if edc_hour > 12:
                    edc_hour -= 12
                    edc_setting = 'pm'
                    
                event_datetime_colon = str(edc_hour) + ':' + event_datetime_colon[1] + edc_setting
#                print(event_datetime_colon)

                event_date = event_datetime[0].split('-')
                event_date = event_date[1] + '/' + event_date[2] + ' ' + event_datetime_colon

                event_text = ''
                for x in range(1,event_split_len):
                    event_text = event_text + ' ' + event_split[x] + ' '

                event_text = event_date + ' - ' + event_text


                event2 = tkinter.Label(root,text=event_text,font=('verdana',20,'bold'),fg='white',bg='black')
                event2.pack(anchor=W)

    else:
        event3 = tkinter.Label(root,text=eventarray,font=('verdana',20,'bold'),fg='white',bg='black')
        event3.pack(anchor=W)
                
    

    #event1 = tkinter.Label(root,text=eventarray[0],font=('verdana',20,'bold'),bg='black')
    #event1.pack(anchor=W)

#    event2 = tkinter.Label(root,text=eventarray[1],font=('verdana',20,'bold'),bg='black')
#    event2.pack(anchor=W)

#    print(eventarray)

#    event3 = tkinter.Label(root,text=eventarray[2],font=('verdana',20,'bold'),bg='black')
#    event3.pack(anchor=W)

#    event4 = tkinter.Label(root,text=eventarray[3],font=('verdana',20,'bold'),bg='black')
#    event4.pack(anchor=W)

     #########################################################################################


    root.mainloop()

if __name__ == "__main__":
    main()
