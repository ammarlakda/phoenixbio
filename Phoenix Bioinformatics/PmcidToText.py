from requests_html import HTMLSession
import requests
from requests.exceptions import ConnectionError
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os


path = r"C:\Users\ammar\OneDrive\Desktop\phoenixbio\Phoenix Bioinformatics\PDFs"
os.chdir(path)



def IdScrape(pmcid):
    '''
    scrapes the ncbi database and downloads the pdf files
    parameters: the pmcid
    return: none
    '''
    s = HTMLSession()
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    try:
        print(pmcid)
        base_url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/'
        r = s.get(base_url + pmcid + '/', headers=headers, timeout=5)
        print(r)
        pdf_url = 'https://www.ncbi.nlm.nih.gov/' + r.html.find('a.int-view', first=True).attrs['href']
        print(pdf_url)
        r = s.get(pdf_url,stream=True)
        with open(pmcid + '.pdf','wb') as f:
            for chunk in r.iter_content(chunk_size = 1024):
                if chunk:
                    f.write(chunk)

    except ConnectionError as e:
        pass
        out = open('ConnectionError_pmcids.txt','a')
        out.write(pmcid + '\n')
        


def convert_pdf_to_txt(path):
    '''
    converts the pdf to a text file that has a lot of random characters (including \n) that we still need to remove
    parameters: path for where the id exists
    return: the text of the pdf
    '''
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


# def main():
#     id = 'PMC59487'
#     IdScrape(id)
#     path = r"C:\Users\ammar\OneDrive\Desktop\phoenixbio\Phoenix Bioinformatics\PDFs"+id+".pdf"
#     text = convert_pdf_to_txt(path)
#     f = open(id+".txt", "a")
#     f.write(text)
#     f.close()

# if __name__ == "__main__":
#     main()
