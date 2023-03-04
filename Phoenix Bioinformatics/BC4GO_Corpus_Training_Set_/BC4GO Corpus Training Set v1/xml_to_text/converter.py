'''
This program converts xml to txt and takes out all the tags
'''

import xml.etree.ElementTree as ET 
from xml import etree 
import os 
import glob

#arr = os.listdir()
#print(arr)

#Set the path to where the folder is located
path = "C:\\Users\\Steven\\Documents\\GitHub\\phoenixbio\\Phoenix Bioinformatics\\BC4GO_Corpus_Training_Set_\\BC4GO Corpus Training Set v1\\xml_to_text"
os.chdir(path)
arr = []
for file in glob.glob("*.xml"):
    arr.append(file)
    print(arr)

#New file creation
#newfile = arr[0]
#f = open(str(newfile[:-3])+"txt", "w")

#Parsing XML file
mytree = ET.parse(arr[1])
myroot = mytree.getroot()

print(len(myroot))

for b in arr:
    btree = ET.parse(b)
    broot = btree.getroot()
    print(len(broot[3]))





def writeTxt(myroot,i):
    newfile = arr[i]
    f = open(str(newfile[:-3])+"txt", "w")

    for x in myroot.iter('text'):
        f.write(x.text)
    
    f.close()


z = len(myroot[3])
i=1
while z!=(i-1):
    if i < len(arr):
        writeTxt(myroot,i)
    i+=1



#Additional Test Code for when we need to convert the files differently

#f.close()
'''
def writeT ():
    z = len(myroot[3])
    i=1
    while z!=i:
        for x in myroot[3][i]: #myroot[document][passages]
            #Trying to get just text: (prints out none, despite there being text)
            #art = x.get('text')
            #print(art)
            f.write(x.text + '\n')
            print(x.text)
            i +=1
            if i == z:
                break

writeT()
'''




'''
for movie in myroot.iter("infon"):
    print(movie.attrib)

def writeTxt(myroot):
    for x in myroot.iter('text'):
        f.write(x.text)

#writeTxt(myroot)

for child in myroot:
    print(child.tag)

i = 1
#write to txt file
while True:
    for y in myroot[y]:
        for x in myroot[3][i]: #myroot[document][passages]
            #Trying to get just text: (prints out none, despite there being text)
            #art = x.get('text')
            #print(art)
            f.write(x.text + '\n')
            print(x.text)
            i +=1

'''