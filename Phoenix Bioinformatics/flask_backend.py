from split_article import split_article
from PmcidToText import *
from runner import get_similar_articles
from ammar import retrieve_docs_and_clean
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
CORS(app)

@app.route('/send-data', methods=['POST'])
def send_data():
    message = request.get_json().get('message')
    docs,main_df = retrieve_docs_and_clean()
    # Create Term-Document Matrix with TF-IDF weighting
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(docs)
    # Create a DataFrame
    df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names_out())
    pmcid=get_similar_articles(message,df,main_df)
    IdScrape(pmcid)
    path = r"C:\Users\ammar\OneDrive\Desktop\phoenixbio\Phoenix Bioinformatics\PDFs/"+pmcid+".pdf"
    text = convert_pdf_to_txt(path)

    modified_message = split_article(text)
    return jsonify({'message': modified_message})

if __name__ == '__main__':
    app.run(debug=True)
