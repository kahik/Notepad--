#colors and font settings
text_color = (0,255,0)
background_color = (0,0,0)
font_size = ('Consolas', 18)

#modules
import os
import time
import tkinter as tk
from tkinter import filedialog

#functions
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def open_file():
    global current_file
    file = filedialog.askopenfilename(initialdir=(os.getcwd()),
                                      title='Select a File',
                                      filetypes=[('Text or Python Files',
                                                 '.txt .py')])
    name = file[file.rfind('/')+1:len(file)]
    current_file = (file, name)
    root.title(name+' in Notepad --')
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        text.insert(tk.INSERT, line)

def save_file():
    global current_file
    new_text = text.get('1.0', 'end-1c')
    f = open(current_file[0],'w')
    f.write(new_text)
    f.close()
    root.title(current_file[1]+' is saved!')
    time.sleep(2)
    root.title(current_file[1]+' in Notepad --')

#tkinter setup
root = tk.Tk()
root.title('Notepad--')
root.geometry(f'800x400+100+100')

frame = tk.Frame(root)
text = tk.Text(frame, height=10000, width=10000, wrap='none',
               bg=rgb_to_hex(background_color),
               fg=rgb_to_hex(text_color),
               insertbackground=rgb_to_hex(text_color),
               font=(font_size))
current_file = ('', '')

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Open', command=lambda:open_file())
filemenu.add_command(label='Save', command=lambda:save_file())
filemenu.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

frame.pack()
text.pack()
root.config(menu=menubar)
root.mainloop()


