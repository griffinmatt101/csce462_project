#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter,time,datetime
import pywapi

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
    clock.pack(anchor=NE,pady=.1)
    tick("", clock)

    ##########################################################################################

    #DATE ####################################################################################
    the_date = datetime.date.today().strftime('%A') + ', ' + datetime.date.today().strftime('%B') + " " + datetime.date.today().strftime('%d')
    input_date = tkinter.Label(root,text=the_date,font=('verdana',31,'bold'),fg='white',bg='black')
    input_date.pack(anchor=NE,pady=.5)

    ##########################################################################################

    #WEATHER #################################################################################
    noaa = pywapi.get_weather_from_noaa('KCLL')
    #noaa_cond = noaa['weather']

    noaa_cond = 'Mostly Cloudy' #test case
    print (noaa_cond)

    hour = int(datetime.datetime.now().strftime('%H'))
#    hour = 22 #test case
    hour_day = (hour >= 7 and hour < 20)
    compliment = ""
    if('Mostly Cloudy' in noaa_cond):
        if(hour_day): #daytime
            img = PhotoImage(file='cloud_sun.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)
            compliment = "Be the ray of sunshine today!"
        else:
            img = PhotoImage(file='cloud_moon.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)

    elif('Windy' in noaa_cond):
        if(hour_day):
            img = PhotoImage(file='windy_day.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)
        else:
            img = PhotoImage(file='windy_night.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)


    elif('Fair' in noaa_cond or 'Clear' in noaa_cond):
        if(hour_day):
            img = PhotoImage(file='bright_sun.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)
            #panel.pack(side=TOP,anchor=W)
        else:
            img = PhotoImage(file='moon.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)

    elif('A Few Clouds' in noaa_cond):
        if(hour_day):
            img = PhotoImage(file='cloud_sun.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)
        else:
            img = PhotoImage(file='cloud_moon.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)

    elif('Partly Cloudy' in noaa_cond):
        if(hour_day):
            img = PhotoImage(file='cloud_sun.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)
        else:
            img = PhotoImage(file='cloud_moon.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)

    elif('Overcast' in noaa_cond):
        img = PhotoImage(file='cloudy.png')
        panel = tkinter.Label(root,image=img,fg='white',bg='black')
        panel.place(x=0,y=0)

    elif('Fog' in noaa_cond): 
        img = PhotoImage(file='fog.png')
        panel = tkinter.Label(root,image=img,fg='white',bg='black')
        panel.place(x=0,y=0)

    elif('Thunderstorm' in noaa_cond):
        if(hour_day):
            img = PhotoImage(file='thunder_sun.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)
        else:
            img = PhotoImage(file='thunder_moon.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)

    elif('Rain' in noaa_cond or 'Drizzle' in noaa_cond):
        if(hour_day):
            img = PhotoImage(file='rain_sun.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)
        else:
            img = PhotoImage(file='rain_moon.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)

    else:
        if(hour_day):
            img = PhotoImage(file='bright_sun.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)
        else:
            img = PhotoImage(file='moon.png')
            panel = tkinter.Label(root,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)


    noaa_temp = noaa['temp_f']
    temp_display = tkinter.Label(root,text=noaa_temp + ' F',font=('verdana',60,'bold'),fg='white',bg='black')
    #temp_display.pack(anchor=W)
    temp_display.place(x=256,y=15)

    weather_com = pywapi.get_weather_from_weather_com('77840','imperial')
    today_data = weather_com['forecasts'][0]
    temp_high_display = tkinter.Label(root,text=today_data['high'],font=('verdana',40,'bold'),fg='white',bg='black')
    temp_low_display = tkinter.Label(root,text=today_data['low'],font=('verdana',40,'bold'),fg='white',bg='black')
    high_low_diff = tkinter.Label(root,text="/",font=('verdana',60,'bold'),fg='white',bg='black')
    temp_high_display.place(x=305,y=135)
    temp_low_display.place(x=410,y=155)
    high_low_diff.place(x=380,y=130)

    tomorrow_data = weather_com['forecasts'][1]
    tomorrow = "Tomorrow: " + tomorrow_data['day']['text'] + ". High of " + tomorrow_data['high'] + " F"
    tomorrow_display = tkinter.Label(root,text=tomorrow, font=('verdana',20,'bold'),fg='white',bg='black')
    tomorrow_display.place(x=0, y=270)

    compliment_label = tkinter.Label(root,text=compliment,font=('DejaVu Serif',40,'italic bold'),fg='white',bg='black')
    compliment_label.pack(side=BOTTOM,anchor=S)
    #lookupString.place(x=305,y=240)
    # city_display = tkinter.Label(root,text='College Station, TX',font=('verdana',30,'bold'),fg='white',bg='black')
    # city_display.place(x=0,y=325)

    ##########################################################################################

    root.mainloop()

if __name__ == "__main__":
    main()
