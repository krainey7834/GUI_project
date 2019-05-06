# Kelsey Rainey
# Just a simple 4-function calculator made using tkinter

import tkinter as t


class Calculator:
    """Just a simple 4-function calculator using buttons"""
    def __init__(self, root):
        # this is literally the most inefficient way to create the buttons but I
        # forgot how Ms Hines told us to do the matrices
        w = 5
        h = 2

        # Create the frame to hold everything
        self.master = t.Frame(root)
        self.master.pack()

        # Frame for the label
        self.top = t.Frame(self.master)
        self.top.pack(side=t.TOP)

        self.bottom = t.Frame(self.master)
        self.bottom.pack(side=t.BOTTOM)

        # the label
        self.v = t.StringVar()
        self.label = t.Label(self.top, textvariable=self.v, height=h, width=20, bg="dark gray")
        self.label.pack(side=t.TOP)

        # Creates another frame to pack in a row of buttons
        self.signs = t.Frame(self.master)
        self.signs.pack(side=t.RIGHT)

        # Creates the buttons to pack in self.signs
        self.divide = t.Button(self.signs, text="/", height=h, width=w,
                               command=lambda m="/": self.change_label(m))
        self.divide.pack()

        self.multi = t.Button(self.signs, text="*", height=h, width=w,
                              command=lambda m="*": self.change_label(m))
        self.multi.pack()

        self.minus = t.Button(self.signs, text="-", height=h, width=w,
                              command=lambda m="-": self.change_label(m))
        self.minus.pack()

        self.add = t.Button(self.signs, text="+", height=h, width=w,
                            command=lambda m="+": self.change_label(m))
        self.add.pack()

        self.equal = t.Button(self.signs, text="=", height=h, width=w,
                              command=self.math)
        self.equal.pack()

        # Creates the frame for the next column
        self.second = t.Frame(self.master)
        self.second.pack(side=t.RIGHT)

        # Creates buttons for self.threes
        self.close_p = t.Button(self.second, text=")", height=h, width=w,
                                command=lambda m=")": self.change_label(m))
        self.close_p.pack()

        self.nine = t.Button(self.second, text="9", height=h, width=w,
                             command=lambda m="9": self.change_label(m))
        self.nine.pack()

        self.six = t.Button(self.second, text="6", height=h, width=w,
                            command=lambda m="6": self.change_label(m))
        self.six.pack()

        self.three = t.Button(self.second, text="3", height=h, width=w,
                              command=lambda m="3": self.change_label(m))
        self.three.pack()

        self.point = t.Button(self.second, text=".", height=h, width=w,
                              command=lambda m=".": self.change_label(m))
        self.point.pack()

        # Creates the frame for the third column
        self.third = t.Frame(self.master)
        self.third.pack(side=t.RIGHT)

        # Creates buttons and yeah you know the drill
        self.open_p = t.Button(self.third, text="(", height=h, width=w,
                               command=lambda m="(": self.change_label(m))
        self.open_p.pack()

        self.eight = t.Button(self.third, text="8", height=h, width=w,
                              command=lambda m="8": self.change_label(m))
        self.eight.pack()

        self.five = t.Button(self.third, text="5", height=h, width=w,
                             command=lambda m="5": self.change_label(m))
        self.five.pack()

        self.two = t.Button(self.third, text="2", height=h, width=w,
                            command=lambda m="2": self.change_label(m))
        self.two.pack()

        self.power = t.Button(self.third, text="^x", height=h, width=w,
                              command=lambda m="**": self.change_label(m))
        self.power.pack()

        # Creates the frame for the forth column
        self.forth = t.Frame(self.master)
        self.forth.pack(side=t.RIGHT)

        # Creates the buttons
        self.clear = t.Button(self.forth, text="Clear", height=h, width=w,
                              command=self.clear)
        self.clear.pack()

        self.seven = t.Button(self.forth, text="7", height=h, width=w,
                              command=lambda m="7": self.change_label(m))
        self.seven.pack()

        self.four = t.Button(self.forth, text="4", height=h, width=w,
                             command=lambda m="4": self.change_label(m))
        self.four.pack()

        self.one = t.Button(self.forth, text="1", height=h, width=w,
                            command=lambda m="1": self.change_label(m))
        self.one.pack()

        self.zero = t.Button(self.forth, text="0", height=h, width=w,
                             command=lambda m="0": self.change_label(m))
        self.zero.pack()

        # drop down menu for colors

        self.var = t.StringVar()
        self.var.set("black")

        self.menu = t.OptionMenu(self.bottom, self.var,
                                 "black", "fuchsia", "deep pink", "red",
                                 "crimson", "green", "blue", "indigo",
                                 "dark magenta", "purple", "orchid", "maroon",
                                 command=lambda v=self.var: self.change_color(v))
        self.menu.pack()
        self.root = root
        self.list = [self.menu, self.label, self.divide, self.multi, self.minus, self.add, self.equal, self.close_p,
                     self.nine, self.six, self.three, self.point, self.open_p, self.eight, self.five, self.two,
                     self.power, self.clear, self.seven, self.four, self.one, self.zero]

        for item in self.list:
            if item != self.label:
                item.configure(bg="white smoke")

    def change_label(self, value):
        # What I want this to do, is to add the buttons clicked to the label
        self.v.set(self.v.get() + value)

    def math(self):
        # this does the math when the user presses the equal button
        self.v.set(str(round(eval(self.v.get()), 5)))

    def clear(self):
        # clears the label
        self.v.set("")

    def change_color(self, v):
        for item in self.list:
            item.configure(fg=v)

def main():
    root = t.Tk()
    myapp = Calculator(root)
    root.mainloop()


main()

