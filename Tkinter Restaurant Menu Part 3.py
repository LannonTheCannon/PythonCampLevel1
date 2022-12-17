import tkinter as tk
from tkinter import *

def getApp1():
    pass 

# main window
root = tk.Tk()
root.geometry('1000x500')
root.title('Restaurant At the Edge of the Universe')

# Title bar
titleFrame = Frame(root, bg = '#132A13', bd = 5, relief = RAISED, width = 1000,
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
mainFrame.pack(side = TOP)

##############################################################################

appFrame = Frame(mainFrame, bg = 'grey', bd = 5, relief = SUNKEN, width = 250,
                 height = 450)
appFrame.propagate(0)
appFrame.pack(side = LEFT)

appTitle = Label(appFrame, bg = 'grey', font = 'consolas 16 bold', text = 'Appetizers',
                 width = 20, height = 2)
appTitle.pack(side = TOP)

appItem1 = Button(appFrame, width = 5, height = 2, text = 'App Item 1',
                  font = 'Consolas 12 bold')
appItem1.pack(side = TOP)

appItem2 = Button(appFrame, width = 5, height = 2, text = 'App Item 1',
                  font = 'Consolas 12 bold')
appItem2.pack(side = TOP)

appItem3 = Button(appFrame, width = 5, height = 2, text = 'App Item 1',
                  font = 'Consolas 12 bold')
appItem3.pack(side = TOP)

appItem4 = Button(appFrame, width = 5, height = 2, text = 'App Item 1',
                  font = 'Consolas 12 bold')
appItem4.pack(side = TOP)

appItem5 = Button(appFrame, width = 5, height = 2, text = 'App Item 1',
                  font = 'Consolas 12 bold')
appItem5.pack(side = TOP)

##############################################################################

entFrame = Frame(mainFrame, bg = 'grey', bd = 5, relief = SUNKEN, width = 250,
                 height = 450)
entFrame.pack(side = LEFT)

##############################################################################

desFrame = Frame(mainFrame, bg = 'grey', bd = 5, relief = SUNKEN, width = 250,
                 height = 450)
desFrame.pack(side = LEFT)

##############################################################################

drinkFrame = Frame(mainFrame, bg = 'grey', bd = 5, relief = SUNKEN, width = 250,
                 height = 450)
drinkFrame.pack(side = LEFT)

##############################################################################

root.mainloop()
