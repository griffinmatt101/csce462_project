import Tkinter as tk
from Tkinter import *
#from PIL import Image, ImageTk
import Tkinter,time,datetime
import sys
import events
import feedparser
import time
import sys
from subprocess import check_output
from DetectMotion import DetectMotion

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
        input_date = Tkinter.Label(self,text=the_date,font=('verdana',100,'bold'),fg="white",bg='black')
        input_date.place(x=0,y=0)

        clock = Tkinter.Label(self,font=('verdana',100,'bold'),fg="white",bg='black')
        clock.pack(anchor=NE)
        self.tick("", clock)
    

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.date()
        self.news()

    def news(self):
        # img = ImageTk.PhotoImage(Image.open('news.png'))
        # image = tkinter.Label(self,image=img,bg='black')
        # image.pack(anchor=N,side=RIGHT)


#    d = feedparser.parse('https://news.google.com/news/rss/?ned=us&gl=US&hl=en')
        d = feedparser.parse('http://news.google.com/news?ned=us&output=rss')

        for post in d.entries[1:5]:
            print(post.title + "\n")
            headline = Tkinter.Label(self,text=post.title + '\n',font=('verdana',17,'bold'),fg="white",bg='black')

            headline.pack(side=TOP,anchor=W)

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.date()
        self.cal()

    def cal(self):
 #       img = ImageTk.PhotoImage(Image.open('calendar_image.png'))
 #       image = Tkinter.Label(self,image=img,fg="white",bg='black')
 #       image.pack(anchor=N,side=RIGHT)

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

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.date()
       #label = tk.Label(self, text="This is page 3")
       #label.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    # main = MainView(root)
    # main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1920x1080")
    root.configure(background='black')
    root.attributes('-fullscreen',True)

    detectGesture = DetectMotion()

    p1 = Page1(root,bg='black')
    p2 = Page2(root,bg='black')
    p3 = Page3(root,bg='black')

    p1.place(x=0, y=0, relwidth=1, relheight=1)
    p2.place(x=0, y=0, relwidth=1, relheight=1)
    p3.place(x=0, y=0, relwidth=1, relheight=1)

    pages = []
    pages.append(p1)
    pages.append(p2)
    pages.append(p3)
    currentPage = 0

    pages[currentPage].show()
    
    while True:
        root.update()
        root.update_idletasks()
        gesture = detectGesture.detectMotion()
        if gesture=="left":
            print ("left")
            currentPage = (currentPage - 1) % 3
        elif gesture=="right":
            print ("right")
            currentPage = (currentPage + 1) % 3
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
