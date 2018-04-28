import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk
import Tkinter,time,datetime
import sys, random, pywapi
import events
import feedparser
from subprocess import check_output


#img = ImageTk.PhotoImage(Image.open('calendar_image.png'))


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

    def tick(self,time_old,clock):
        # get the current local time from the PC
        time_now = time.strftime('%I:%M')
        # if time string has changed, update it
        if time_now != time_old:
            time_old = time_now
            clock.config(text = time_now)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, self.tick, time_old, clock)

    def date(self):
        the_date = datetime.datetime.now().strftime('%m/%d')
        input_date = Tkinter.Label(self,text=the_date,font=('verdana',100,'bold'),bg='black')
        input_date.place(x=0,y=0)

        clock = Tkinter.Label(self,font=('verdana',100,'bold'),bg='black')
        clock.pack(anchor=NE)
        self.tick("", clock)

    def today_date(self):
        the_date = datetime.date.today().strftime('%A') + ', ' + datetime.date.today().strftime('%B') + " " + datetime.date.today().strftime('%d')
        input_date = Tkinter.Label(self,text=the_date,font=('verdana',31,'bold'),fg='white',bg='black')
        input_date.pack(anchor=NE,pady=.5)

        clock = Tkinter.Label(self,font=('verdana',100,'bold'),fg='white',bg='black')
        clock.pack(anchor=NE,pady=.1)
        self.tick("", clock)

    

class TodayPage1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.today_date()
        self.today()
        
    def today(self):
        noaa = pywapi.get_weather_from_noaa('KCLL')
        noaa_cond = noaa['weather']

        #noaa_cond = 'Thunderstorms' #test case
        print (noaa_cond)

        hour = int(datetime.datetime.now().strftime('%H'))
    #    hour = 22 #test case
        hour_day = (hour >= 7 and hour < 20)
        compliment_size = 40
        compliment_array = [('You look beautiful today!',50), ('You light up every room!',50),('You are a force of nature!',50), ("Lookin' good as always!", 50),("No one can do this better than you!",35),("#flawless",70)]
        compliment = ""
        if('Mostly Cloudy' in noaa_cond):
            if(hour_day): #daytime
                img = PhotoImage(file='cloud_sun.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.image = img
                panel.place(x=0,y=0)
                compliment = "Be the ray of sunshine today!"
            else:
                img = PhotoImage(file='cloud_moon.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)

        elif('Windy' in noaa_cond):
            compliment = "You blow me away!"
            compliment_size = 60
            if(hour_day):
                img = PhotoImage(file='windy_day.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)
            else:
                img = PhotoImage(file='windy_night.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)


        elif('Fair' in noaa_cond or 'Clear' in noaa_cond):
            if(hour_day):
                img = PhotoImage(file='bright_sun.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.image = img
                panel.place(x=0,y=0)
                #compliment = "You shine brighter than the sun!"
            else:
                img = PhotoImage(file='moon.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)
                compliment = "You shine brighter than the moon!"

        elif('A Few Clouds' in noaa_cond):
            if(hour_day):
                img = PhotoImage(file='cloud_sun.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)
                compliment = "Be the ray of sunshine today!"
            else:
                img = PhotoImage(file='cloud_moon.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)

        elif('Partly Cloudy' in noaa_cond):
            if(hour_day):
                img = PhotoImage(file='cloud_sun.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)
                compliment = "Be the ray of sunshine today!"
            else:
                img = PhotoImage(file='cloud_moon.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)

        elif('Overcast' in noaa_cond):
            img = PhotoImage(file='cloudy.png')
            panel = Tkinter.Label(self,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)
            compliment = "You are sunshine on a cloudy day!"

        elif('Fog' in noaa_cond): 
            img = PhotoImage(file='fog.png')
            panel = Tkinter.Label(self,image=img,fg='white',bg='black')
            panel.place(x=0,y=0)

        elif('Thunderstorm' in noaa_cond):
            compliment = "Your smile is striking!"
            compliment_size = 60
            if(hour_day):
                img = PhotoImage(file='thunder_sun.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)
            else:
                img = PhotoImage(file='thunder_moon.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)
                

        elif('Rain' in noaa_cond or 'Drizzle' in noaa_cond):
            if(hour_day):
                img = PhotoImage(file='rain_sun.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)
                compliment = "Fo' drizzle, you looking good today!"
                compliment_size = 35
            else:
                img = PhotoImage(file='rain_moon.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)
                compliment = "Fo' drizzle, you looking good today!"
                compliment_size = 35


        else:
            if(hour_day):
                img = PhotoImage(file='bright_sun.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)
            else:
                img = PhotoImage(file='moon.png')
                panel = Tkinter.Label(self,image=img,fg='white',bg='black')
                panel.place(x=0,y=0)


        noaa_temp = noaa['temp_f']
        temp_display = Tkinter.Label(self,text=noaa_temp + ' F',font=('verdana',60,'bold'),fg='white',bg='black')
        #temp_display.pack(anchor=W)
        temp_display.place(x=256,y=15)

        

        weather_com = pywapi.get_weather_from_weather_com('77840','imperial')
        today_data = weather_com['forecasts'][0]
        temp_high_display = Tkinter.Label(self,text=today_data['high'],font=('verdana',40,'bold'),fg='white',bg='black')
        temp_low_display = Tkinter.Label(self,text=today_data['low'],font=('verdana',40,'bold'),fg='white',bg='black')
        high_low_diff = Tkinter.Label(self,text="/",font=('verdana',60,'bold'),fg='white',bg='black')
        temp_high_display.place(x=305,y=135)
        temp_low_display.place(x=410,y=155)
        high_low_diff.place(x=380,y=130)
        
        today_condition_display = Tkinter.Label(self, text="Today: " + noaa_cond, font=('veranda',20,'bold'), fg='white', bg='black')
        today_condition_display.place(x=0, y=255)

        tomorrow_data = weather_com['forecasts'][1]
        tomorrow = "Tomorrow: " + tomorrow_data['day']['text'] + ". High of " + tomorrow_data['high'] + " F"
        tomorrow_display = Tkinter.Label(self,text=tomorrow, font=('verdana',20,'bold'),fg='white',bg='black')
        tomorrow_display.place(x=0, y=290)

        if(compliment == ""):
            random_compliment = random.randint(0,4)
            compliment = compliment_array[random_compliment][0]
            compliment_size = compliment_array[random_compliment][1]


        compliment_label = Tkinter.Label(self,text=compliment,font=('DejaVu Serif',compliment_size,'italic bold'),fg='white',bg='black')
        compliment_label.pack(side=BOTTOM, anchor=S, pady=30)
        #lookupString.place(x=305,y=240)
        # city_display = Tkinter.Label(self,text='College Station, TX',font=('verdana',30,'bold'),fg='white',bg='black')
        # city_display.place(x=0,y=325)
        

class CalPage2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.date()
        self.cal()

    def cal(self):
        img = ImageTk.PhotoImage(Image.open('calendar_image.png'))
        cal_image = Tkinter.Label(self,image=img,bg='black')
        cal_image.image = img
        cal_image.pack(anchor=N,side=RIGHT)


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
                    event1 = Tkinter.Label(self,text=event_text,font=('verdana',20,'bold'),fg='white',bg='black')

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


                    event2 = Tkinter.Label(self,text=event_text,font=('verdana',20,'bold'),fg='white',bg='black')
                    event2.pack(anchor=W)

        else:
            event3 = Tkinter.Label(self,text=eventarray,font=('verdana',20,'bold'),fg='white',bg='black')
            event3.pack(anchor=W)

class NewsPage3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.date()
        self.news()

    def news(self):
        img = ImageTk.PhotoImage(Image.open('news.png'))
        news_image = Tkinter.Label(self,image=img,bg='black')
        news_image.image = img
        news_image.pack(anchor=N,side=RIGHT)


#    d = feedparser.parse('https://news.google.com/news/rss/?ned=us&gl=US&hl=en')
        d = feedparser.parse('http://news.google.com/news?ned=us&output=rss')

        for post in d.entries[1:5]:
            print(post.title + "\n")
            headline = Tkinter.Label(self,text=post.title + '\n',font=('verdana',17,'bold'),bg='black')

            headline.pack(side=TOP,anchor=W)

class BlankPage4(Page):
    def __init__(self,*args,**kwargs):
        Page.__init__(self,*args,**kwargs)
        self.date()


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background='black')
    root.attributes('-fullscreen',True)

    p1 = TodayPage1(root,bg='black')
    p2 = CalPage2(root,bg='black')
    p3 = NewsPage3(root,bg='black')
    p4 = BlankPage4(root,bg='black')

    p1.place(x=0, y=0, relwidth=1, relheight=1)
    p2.place(x=0, y=0, relwidth=1, relheight=1)
    p3.place(x=0, y=0, relwidth=1, relheight=1)
    p4.place(x=0, y=0, relwidth=1, relheight=1)

    pages = []
    pages.append(p1)
    pages.append(p2)
    pages.append(p3)
    pages.append(p4)
    currentPage = 0

    pages[currentPage].show()
    
    while True:
        root.update()
        root.update_idletasks()
        gesture = detectGesture.detectMotion()
        if gesture=="left":
            print"left"
            currentPage = (currentPage - 1) % 4
        elif gesture=="right":
            print "right"
            currentPage = (currentPage + 1) % 4
        else:
            pass
        pages[currentPage].show()
'''
#    try:
#        print "Showing current page"
#        # pages[currentPage].show()
#        # p1.show()
#        print "Current page is showed"
#        while True:
#            # x = input("Tst: ")
#            # print "Detecting gesture"
#            gesture = detectGesture.detectMotion()
#            if gesture is not None:
#                if gesture=="left":
                    print "Left gesture"
                    # currentPage -= 1 
                    p2.show()
                elif gesture=="right":
                    print "Right gesture"
                    # currentPage += 1
                    p3.show()
                # pages[currentPage].show()
            # if x==2:
            #     p2.show()
            # elif x==3:
            #     p3.show()
            # else:
            #     p1.show()
    except KeyboardInterrupt:
        sys.exit()
#    root.mainloop()
'''
