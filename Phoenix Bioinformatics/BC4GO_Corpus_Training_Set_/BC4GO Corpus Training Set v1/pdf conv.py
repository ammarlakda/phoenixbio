import PyPDF2
import os

path = "C:\\Users\\Steven\\Documents\\GitHub\\phoenixbio\\Phoenix Bioinformatics\\BC4GO_Corpus_Training_Set_\\BC4GO Corpus Training Set v1"
os.chdir(path)

#create file object variable
#opening method will be rb
pdffileobj=open('PMC6746701.pdf','rb')

#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfReader(pdffileobj)

#This will store the number of pages of this pdf file
x=len(pdfreader.pages)

#create a variable that will select the selected number of pages
pageobj=pdfreader.pages[x-1]

#(x+1) because python indentation starts with 0.
#create text variable which will store all text datafrom pdf file
text=pageobj.extract_text()

#save the extracted data from pdf to a txt file
#we will use file handling here
#dont forget to put r before you put the file path
#go to the file location copy the path by right clicking on the file
#click properties and copy the location path and paste it here.
#put "\\your_txtfilename"

file1=open(r"C:\\Users\\Steven\\Documents\\GitHub\\phoenixbio\\Phoenix Bioinformatics\\BC4GO_Corpus_Training_Set_\\BC4GO Corpus Training Set v1\\PMC6746701.txt","w", encoding="utf-8")
file1.writelines(text)



