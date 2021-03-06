#!/usr/bin/python

import gi
# import gtk.gdk
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

        main_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 40)

        # Clock label
        self.label1 = Gtk.Label()
        self.label1.set_xalign(1)
        self.label1.set_yalign(0)

        # Another label
        self.label2 = Gtk.Label("Label 2")

        # @params:
        #   item: what to add to the box
        #   shouldExpand: expands it across the space
        #   shouldFill: fills imediate space given
        #
        main_box.pack_start(self.label1, True, True, 0)
        main_box.pack_end(self.label2, True, True, 0)
        # Add any new labels by main_box.pack_end(...)

        self.add(main_box)
        self.show_all()


    def update(self):
        self.label1.set_markup(time.strftime('<span foreground="white" font="28.5">%H:%M:%S</span>'))
        return True


def main():
    Gtk.main()

if __name__ == "__main__":
    clock = Clock()
    GObject.timeout_add(200, clock.update)
    main()


