# Restaurant Menu Program Part 3 (Tkinter integration)

import tkinter as tk
from tkinter import *

# main window
root = tk.Tk()
root.geometry('500x500')
root.title('Restaurant At the Edge of the Universe')

# Title bar
titleFrame = Frame(root, bg = '#132A13', bd = 5, relief = RAISED, width = 500,
                   height = 50)
titleFrame.propagate(0)
titleFrame.pack(side = TOP)

# Title Label
lblTitle = Label(titleFrame, bg = '#132A13', fg = 'cornsilk', width = 40,
                 height = 2, text = 'Restaurant at The Edge of the Universe',
                 font = 'arial 16 bold')
lblTitle.pack()

# mainframe
mainFrame = Frame(root, bg = '#588157', bd = 5, relief = RAISED, width = 500,
                  height = 450)
mainFrame.pack(side = TOP)
