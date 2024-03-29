from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
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


def main():
    path = "C:\\Users\\Steven\\Documents\\GitHub\\phoenixbio\\Phoenix Bioinformatics\\BC4GO_Corpus_Training_Set_\\BC4GO Corpus Training Set v1\\PMC6746701.pdf"
    text = convert_pdf_to_txt(path)
    file1=open(r"C:\\Users\\Steven\\Documents\\GitHub\\phoenixbio\\Phoenix Bioinformatics\\BC4GO_Corpus_Training_Set_\\BC4GO Corpus Training Set v1\\PMC6746701.txt","w", encoding="utf-8")
    file1.writelines(text)

if __name__ == "__main__":
    main()

