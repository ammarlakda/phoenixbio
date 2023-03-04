import re
import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer



def retrieve_docs_and_clean():
  main_df = pd.read_csv(r'C:\Users\ammar\OneDrive\Desktop\phoenixbio\Phoenix Bioinformatics\IF Code\cleanedDatasets\phyb.csv')
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


docs,main_df = retrieve_docs_and_clean()

# Create Term-Document Matrix with TF-IDF weighting
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

# Create a DataFrame
df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names_out())

docs,_ = retrieve_docs_and_clean()
# Create Term-Document Matrix with TF-IDF weighting
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

# Create a DataFrame
df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names_out())


def get_similar_articles(q, df):
  print("query:", q)
  print("The following are articles with the highest cosine similarity values: ")
  q = [q]
  q_vec = vectorizer.transform(q).toarray().reshape(df.shape[0],)
  sim = {}
  for i in df.columns:
    sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
  
  sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
  
  for k, v in sim_sorted:
    if v != 0.0:
      #print("Similarity Value:", v)
      print(docs[k])
      print(k)
      print(main_df_temp[k])
      return


q1 = 'photoreceptor active in photomorphogenesis phyB'
main_df_temp=list(main_df['pmcid'])
get_similar_articles(q1, df)
print('-'*100)