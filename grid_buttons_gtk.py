# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="Kratki espresso")
        button2 = Gtk.Button(label="Produženi espresso")
        button3 = Gtk.Button(label="Macchiato")
        button4 = Gtk.Button(label="Cappucchino")
        button5 = Gtk.Button(label="Cappucchino sa čokoladom")
        button6 = Gtk.Button(label="Nes espresso")
        button7 = Gtk.Button(label="Nes macchiato")
        button8 = Gtk.Button(label="Nes cappucchino")
        button9 = Gtk.Button(label="Topla čokolada")
        button10 = Gtk.Button(label="Jača čokolada")
        button11 = Gtk.Button(label="Čokolada sa mlekom")
        button12 = Gtk.Button(label="Čaj")
        button13 = Gtk.Button(label="Mleko")
        button14 = Gtk.Button(label="Bela kafa")
        button15 = Gtk.Button(label="Prazna čaša")
        button16 = Gtk.Button(label="Kratki espresso sa čokoladom")

        grid.add(button1)
        grid.attach_next_to(button2, button1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3, button2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4, button3, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5, button4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button7, button6, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button8, button7, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button9, button1, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button10, button9, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button11, button10, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button12, button11, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button13, button12, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button14, button13, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button15, button14, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button16, button15, Gtk.PositionType.BOTTOM, 1, 1)

win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()