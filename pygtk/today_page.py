#!/usr/bin/python

import gi
import gtk.gdk
import time
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk
from gi.repository import GObject


class Clock(Gtk.Window):
    def __init__(self):
        super(Clock,self).__init__()

        self.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0,0,0))

        self.set_size_request(1920,1080)
        self.set_title("TODAY")
        self.connect("destroy",Gtk.main_quit)

        self.label = Gtk.Label()
        self.label.set_xalign(1)
        self.label.set_yalign(0)

        self.add(self.label)
        self.show_all()


    def update(self): 
        self.label.set_markup(time.strftime('<span foreground="white" font="28.5">%H:%M:%S</span>'))
        return True


def main():
    Gtk.main()

if __name__ == "__main__":
    clock = Clock()
    GObject.timeout_add(200, clock.update)
    main()


