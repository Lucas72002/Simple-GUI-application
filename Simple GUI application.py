import tkinter as tk

#the folowing statement imports all the new Tkinter widgets. It's recommended to use the new (ttk) widgets instead of the old ones (tk) whenever they're available.

from tkinter import ttk

#by connvention the main window in Tkinter is called "root" or "main". A container (Window), is an instance of Tkinter's Tk class ("Tk" as the attribute of the object "tk"). 

root = tk.Tk()
root.resizable(False, False)
root.title("Simple GUI application")

#change the window size and location (window.geometry("widthxheight+/-x+/-y") where x is the window's horizontal and y vertical position from the right edge and bottom of the screen respectively).

root.geometry("600x400+50+50")
root.iconbitmap("icon.ico")

#place a label on the root window. "Root" is the parent window where you want to place the widget. "Text" is one or more keyword arguments that specify configurations of the widget ("Label" is this case). There are other ways to set the options of a widget e.g. dictionary index and config() method with keyword attributes.

message = tk.Label(root, text="Hello!", font="Helvetica, 20")

#the following positions the label on the main widow (otherwise the widget would be invisible). The "pack()" method arranges widgets aroud the edges of their containers.

message.pack()

#the following defines a function called button_clicked() and associate it with the command option of a button widget. Not all Tkinter widgets support the command option for event binding, for some the bind() method is required.

from tkinter.messagebox import showinfo

def button_clicked():
    showinfo(title="Information", message="Button clicked!")

#command binding allow you to associate a callback function with an event.

button = ttk.Button(root, text="Click Me!", command=button_clicked)
button.pack(ipadx=15, ipady=15)

#to add an image we first pass the path to the photo to the PhotoImage constructor, assign the PhtoImage object to the image option of the Label widget.

photo = tk.PhotoImage(file="Cursor.png")
image_label = ttk.Label(root, image=photo, padding=5)
image_label.pack()

#the mainloop() keeps the window visible on the screen. It waits for events and helps in updating the GUI (event-driven programming). Any code after the mainloop() will not run.

exit_button = ttk.Button(root, text="Exit", command=lambda: root.quit())
exit_button.pack(ipadx=5,ipady=5, expand=True)

root.mainloop()