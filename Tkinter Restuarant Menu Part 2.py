# Restaurant Menu Program Part 3 (Tkinter integration)

import tkinter as tk
from tkinter import *
from tkmacosx import Button

# main window
root = tk.Tk()
root.geometry('1000x500')
root.title('Restaurant At the Edge of the Universe')

# Title bar
titleFrame = Frame(root, bg = '#132A13', bd = 5, relief = GROOVE, width = 1000,
                   height = 50)
titleFrame.propagate(0)
titleFrame.pack(side = TOP)

# Title Label
lblTitle = Label(titleFrame, bg = '#132A13', fg = 'cornsilk', width = 40,
                 height = 2, text = 'Restaurant at The Edge of the Universe',
                 font = 'arial 16 bold')
lblTitle.pack()

# mainframe
mainFrame = Frame(root, bg = '#588157', bd = 5, relief = RAISED, width = 1000,
                  height = 450)
mainFrame.propagate(0)
mainFrame.pack(side = TOP)

##############################################################################

appFrame = Frame(mainFrame, bg = 'green', bd = 5, relief = SUNKEN, width = 250,
                  height = 450)
appFrame.propagate(0)
appFrame.pack(side = LEFT)

lblApp = Label(appFrame, bg = 'green', fg = 'white', width = 15, height = 2,
               text = 'Appetizers', font = 'Consolas 16 bold')
lblApp.pack(side = TOP)

btnApp1 = Button(appFrame,
                 bg = 'blue',
                 fg = 'white', width = 100, height = 50,
                 highlightbackground = 'black',
                 text = 'Galaxy Fries', font = 'consolas 12 bold',
                 wraplength = 50)
btnApp1.pack(side = TOP)

entApp = Entry(appFrame, width = 10, font = 'consolas 12', text = '')
entApp.place(x = 10, y = 200)

##############################################################################

entFrame = Frame(mainFrame, bg = 'blue', bd = 5, relief = SUNKEN, width = 250,
                  height = 450)
entFrame.pack(side = LEFT)

##############################################################################

desFrame = Frame(mainFrame, bg = 'pink', bd = 5, relief = SUNKEN, width = 250,
                  height = 450)
desFrame.pack(side = LEFT)

##############################################################################

drinkFrame = Frame(mainFrame, bg = 'orange', bd = 5, relief = SUNKEN, width = 250,
                  height = 450)
drinkFrame.pack(side = LEFT)

##############################################################################

root.mainloop()
