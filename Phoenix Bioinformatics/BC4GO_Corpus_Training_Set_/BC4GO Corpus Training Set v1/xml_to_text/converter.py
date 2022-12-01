'''
This program converts xml to txt and takes out all the tags\
'''

import xml.etree.ElementTree as ET 
import os 

#Set the path to where the folder is located
path = "C:\\Users\\Steven\\Documents\\GitHub\\phoenixbio\\Phoenix Bioinformatics\\BC4GO_Corpus_Training_Set_\\BC4GO Corpus Training Set v1\\xml_to_text"
os.chdir(path)

#New file creation
f = open("12213836.txt", "w")

#Setting up XML file
mytree = ET.parse("12213836.xml")
myroot = mytree.getroot()
i = 1

while True:
    for x in myroot[3][i]: #myroot[document][passages]
        #Trying to get just text: (prints out none, despite there being text)
        #art = x.get('text')
        #print(art)
        f.write(x.text + '\n')
        print(x.text)
        i +=1

for y in myroot.findall('passage'):
    item = y.find('passage').text
    print(item)


