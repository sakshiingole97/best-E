import PyPDF2
from PIL import Image,ImageFilter
img = Image.open("C:\\Users\\Admin\\Downloads\\virat.jpg")
filter_image = img.filter(ImageFilter.BLUR)
filter_image.save("C:\\Users\\Admin\\Downloads\\virat.jpg","png")
print(img.format)

#2)
from PyPDF2
import PdfFileMerger, PdfFileReader
pdffile1= open("file1.pdf","rb")
pdffile2 = open("file2.pdf","rb")
pdfreader1 = PyPDF2.PdfFileReader(pdffile1)
pdfreader2 = PyPDF2.PdfFileReader(pdffile2)
pdfwriter = PyPDF2.PdfFileWriter()
for pagenum in range(pdfreader1.numPages):
    pageobj = pdfreader1.getPage()(pagenum)
    pdfwriter.addPage(pageobj)
for pagenum in range(pdfreader2.numPages):
    pageobj = pdfreader2.getPage(pagenum)
    pdfwriter.addPage(pageobj)
outputfile = open("MergedFiles.pdf","wb")
pdfwriter.write(outputfile)
outputfile.close()
pdffile1.close()
pdffile2.close()
pdffile3 = open("MergedFiles.pdf","rb")
pdfreader3 = PyPDF2.PdfFileReader(pdffile3)
print(pdfreader3)
pdffile3.close()
#3)
import mysql.connector
import requests
import MySQLdb
from bs4 import BeautifulSoup
mydb = mysql.connector.connect(
    host = "local",
    uesr="root",
    passwd="8639488740",
    database="myquotes"

)
dbms = mydb.cursor()
url = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports"
html_text = requests.get(url)
soup = BeautifulSoup(html_text.text,"html.parser")
print(soup.prettify())
