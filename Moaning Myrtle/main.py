# install & import necessary packages ('pip install pyttsx3', and 'pip install pyPDF2')
import pyttsx3
import PyPDF2
from tkinter.filedialog import *


# read name of pdf from user
book = askopenfilename()
# initialize with pdfReader and pass book name
pdfReader = PyPDF2.PdfFileReader(book)
# get no.of pages in pdf
pages = pdfReader.numPages

# read all the data from each page in pdf
for num in range(0, pages):
    page = pdfReader.getPage(num)
    # convert & extract text
    text = page.extractText()
    # initialize an object to parse text extracted
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()