import re
import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from split_article import split_article
from PmcidToText import *
from runner import *
from flask import Flask, request, jsonify
from flask_cors import CORS



def retrieve_docs_and_clean():
  main_df = pd.read_csv(r'C:\code\QmindPheonix\phoenixbio\Phoenix Bioinformatics\IF Code\cleanedDatasets\phyb.csv')
  #df = df['abstract']
  # Clean Paragraphs
  col_list =  list(main_df["abstract"])

  documents_clean = []
  for d in col_list:
    if isinstance(d, str):
        document_test = re.sub(r'[^\x00-\x7F]+', ' ', d)
        document_test = re.sub(r'@\w+', '', document_test)
        document_test = document_test.lower()
        document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test)
        document_test = re.sub(r'[0-9]', '', document_test)
        document_test = re.sub(r'\s{2,}', ' ', document_test)
        documents_clean.append(document_test)

  return documents_clean, main_df






def get_similar_articles(q, df, main_df):
  docs,main_df = retrieve_docs_and_clean()
  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(docs)
  # Create a DataFrame
  df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names_out())
  q = [q]
  q_vec = vectorizer.transform(q).toarray().reshape(df.shape[0],)
  sim = {}
  for i in df.columns:
    sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
  
  sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
  
  for k, v in sim_sorted:
    if v != 0.0:
      #print("Similarity Value:", v)
      return main_df.loc[int(k)]

# docs,main_df = retrieve_docs_and_clean()
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(docs)
# # Create a DataFrame
# df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names_out())
# pmcid=get_similar_articles("phyb function in rice seedlings", df, main_df)
# pmc=pmcid['pmcid']
# IdScrape(pmc)
# path = r"C:\Users\19058\Documents\GitHub\phoenixbio\Phoenix Bioinformatics\PDFs/"+pmc+".pdf"
# text = convert_pdf_to_txt(path)
# print(text)
# print("-------------------------------------------------------")
# print(split_article(text))
# print("-------------------------------------------------------")