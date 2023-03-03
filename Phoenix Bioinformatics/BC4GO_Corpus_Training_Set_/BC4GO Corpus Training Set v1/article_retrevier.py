from requests_html import HTMLSession
import requests
from requests.exceptions import ConnectionError

import os


s = HTMLSession()

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}


path = "C:\\Users\\Steven\\Documents\\GitHub\\phoenixbio\\Phoenix Bioinformatics\\BC4GO_Corpus_Training_Set_\\BC4GO Corpus Training Set v1"
os.chdir(path)
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))



file = open('inputs.txt','r')
ids = file.readlines()
for pmc in ids:
    try:
        pmcid = pmc.strip()
        base_url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/'
        r = s.get(base_url + pmcid + '/', headers=headers, timeout=5)
        print(r)
        pdf_url = 'https://www.ncbi.nlm.nih.gov' + r.html.find('a.int-view', first=True).attrs['href']
        print(pdf_url)
        r = s.get(pdf_url,stream=True)
        with open(pmcid + '.pdf','wb') as f:
            for chunk in r.iter_content(chunk_size = 1024):
                if chunk:
                    f.write(chunk)

    except ConnectionError as e:
        #pass
        #out = open('ConnectionError_pmcids.txt','a')
        #out.write(pmcid + '\n')
        print(e)