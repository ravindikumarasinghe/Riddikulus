# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# import tkinter
from tkinter import *
from tkinter.ttk import *

# import time format
from time import strftime
# create UI for clock
root = Tk()
root.title("Digital Clock")


# create function to get time
def time():
    string = strftime('%H : %M : %S %p')
    label.config(text = string)
    label.after(1000, time)     # time counts on every second


# label create
# "ds_digital" - font used
label = Label(root, font=("ds-digital", 125), background="black", foreground = "#00FFFF")
label.pack(anchor = "center")
time()      # call time function

mainloop()
