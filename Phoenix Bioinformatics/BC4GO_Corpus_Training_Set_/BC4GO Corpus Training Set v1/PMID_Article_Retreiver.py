# This code uses Biopython to retrieve lists of articles from pubmed
# you need to install Biopython first.

# If you use Anaconda:
# conda install biopython

# If you use pip/venv:
# pip install biopython

# Full discussion:
# https://marcobonzanini.wordpress.com/2015/01/12/searching-pubmed-with-python/

from Bio import Entrez

def search(query):
    Entrez.email = 'your.email@example.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='20',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'your.email@example.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

if __name__ == '__main__':
    results = search('phyb') # or any query you like
    id_list = results['IdList'] # list of UIDs
    chunk_size = 50 # whatever you like   
    for chunk_i in range(0, len(id_list), chunk_size):
        chunk = id_list[chunk_i:chunk_i + chunk_size]
        try: 
            papers = fetch_details(chunk)
            for i, paper in enumerate(papers['PubmedArticle']):
                print(papers)
        except: # occasionally a chunk might annoy your parser
            pass