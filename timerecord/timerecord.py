# import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from time import strftime
from timer import Timer


def start():
    global t
    if t.StartTime is not None:
        messagebox.showerror('error', "A timer is still running,"
                             "please reset first!")
    t.start()
    txttimestart.set(t.StartTime.strftime("%m/%d/%Y, %H:%M:%S"))
    btstop.state(["!disabled"])
    btstart.state(["disabled"])


def stop():
    global t
    elapsetime = t.stop()
    txttimestop.set(t.StopTime.strftime("%m/%d/%Y, %H:%M:%S"))
    btstart.state(["!disabled"])
    btstop.state(["disabled"])
    print(elapsetime)
    filename = "timerlog.txt"
    strdescription = text1.get("1.0", "end-1c")
    elapsedtime = t.StopTime - t.StartTime
    elapsedtime_inmin = divmod(elapsedtime.total_seconds(), 60)
    str_entry = f"{txttimestart.get()} - {txttimestop.get()}: " \
                 f"{elapsedtime_inmin} {strdescription}\n"
    write_to_file(filename, str_entry)


def reset():
    global t
    t.reset()

    print(t.StartTime)
    resetscreen()


def resetscreen():
    txttimestop.set("")
    txttimestart.set("")
    btstart.state(["!disabled"])
    btstop.state(["disabled"])
    text1.delete(1.0, "end")


def write_to_file(file_name, strcontent):
    try:
        with open(file_name, 'a') as f_object:
            f_object.write(strcontent)
    except FileNotFoundError:
        print(f"Error: File {file_name} not found!")


# global t
t = Timer()
root = Tk()
root.title("Time Recorder")
root.geometry("500x250")
txttimestart = StringVar()
txttimestop = StringVar()
lbl_task = Label(root, text="Task")
lbl_task.grid(row=0, column=0, sticky=W, pady=2)
# entry widgets, used to take entry from user
text1 = Text(root, height=3, width=40)
text1.grid(row=0, column=1, pady=2, columnspan=2)

lbl_label1 = Label(root, text="Timer Start Time:")
lbl_label1.grid(row=1, column=0, sticky=W, pady=2)
lbl_starttime = Label(root, font=('calibri', 14, 'bold'), foreground='black',
                      textvariable=txttimestart)
lbl_starttime.grid(row=1, column=1, sticky=W, pady=2, columnspan=2)

lbl_label2 = Label(root, text="Timer Stop Time:")
lbl_label2.grid(row=2, column=0, sticky=W, pady=2)
lbl_stoptime = Label(root, font=('calibri', 14, 'bold'), foreground='black',
                     textvariable=txttimestop)
lbl_stoptime.grid(row=2, column=1, sticky=W, pady=2, columnspan=2)

btstart = Button(root, text="Start", command=start)
btstart.grid(row=3, column=0, sticky=W, pady=2)
btstop = Button(root, text="Stop", command=stop)
btstop.grid(row=3, column=1, sticky=W, pady=2)
btstop.state(["disabled"])

btreset = Button(root, text="Reset", command=reset)
btreset.grid(row=3, column=2, sticky=W, pady=2)

root.mainloop()
