from requests_html import HTMLSession
import requests
from requests.exceptions import ConnectionError

import os

s = HTMLSession()

headers = {}



cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

file = open('inputs.txt','r')
ids = file.readlines()
for pmc in ids:
    try:
        pmcid = pmc.strip()
        base_url = 'https://www.ncbi.nlm.nhi.gov/pmc/articles'
        r = s.get(base_url + pmcid + '/', headers=headers, timeout=5)
        pdf_url = 'https://www.ncbi.nlm.nhi.gov' + r.html.find('a.int-view',first=True).attrs['href']
        r = s.get(pdf_url,stream=True)
        with open(pmcid + '.pdf','wb') as f:
            for chunk in r.iter_content(chunk_size = 1024):
                if chunk:
                    f.write(chunk)

    except ConnectionError as e:
        pass
        out = open('ConnectionError_pmcids.txt','a')
        out.write(pmcid + '\n')