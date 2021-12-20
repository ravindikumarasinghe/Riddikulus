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


# import packages
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


# create object for qrcode
qrcode = pyqrcode.create(input("Hello master! What's your secret message: "))
qrcode.png("yourQRCode.png", scale=25)

decode_meaning = decode(Image.open("yourQRCode.png"))
print("The secret message: " + decode_meaning[0].data.decode("ascii"))