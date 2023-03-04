# import important modules
import numpy as np
import pandas as pd
# sklearn modules
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB # classifier 
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    plot_confusion_matrix,
)
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# text preprocessing modules
from string import punctuation 
# text preprocessing modules
from nltk.tokenize import word_tokenize
import nltk
# adding two more downloads based on warnings generated when cleaning text 
nltk.download('stopwords')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
import re #regular expression
# Download dependency
for dependency in (
    "brown",
    "names",
    "wordnet",
    "averaged_perceptron_tagger",
    "universal_tagset",
):
    nltk.download(dependency)
    
import warnings
warnings.filterwarnings("ignore")
# seeding
np.random.seed(123)
import pandas as pd
# import tensorflow and keras for padding 
import tensorflow as tf 
import keras as k
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
# load data from phyb_400 csv 
df_original = pd.read_csv("/Users/emilyjiang/Desktop/QMIND_Ciaran_Webscraping/PHYB_400.csv", index_col=0) 
df_original.iloc[:,-1] = df_original.iloc[:,-1].astype(str)
stop_words =  stopwords.words('english')
def text_cleaning(text, remove_stop_words=True, lemmatize_words=True):
    # Clean the text, with the option to remove stop_words and to lemmatize word
    # Clean the text
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text =  re.sub(r'http\S+',' link ', text)
    text = re.sub(r'\b\d+(?:\.\d+)?\s+', '', text) # remove numbers
        
    # Remove punctuation from text
    text = ''.join([c for c in text if c not in punctuation])
    
    # Optionally, remove stop words
    if remove_stop_words:
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
    
    # Optionally, shorten words to their stems
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer() 
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
    
    # Return a list of words
    return(text)
df_original["cleaned_data"] = df_original[df_original.columns[len(df_original.columns)-1]]
myTokenizer = Tokenizer(num_words=1000)
# tokenize the sentences (but using keras this time)
myTokenizer.fit_on_texts(df_original.iloc[:,-1])
sequences = myTokenizer.texts_to_sequences(df_original.iloc[:,-1])

# padding (make everything the same dimension by adding zeros to the front)
padded = pad_sequences(sequences, maxlen=len(df_original.iloc[:,-1][3].split(" ")))

# count number of "phyB" occurrences in cleaned text column 
df_original['count'] = df_original[df_original.columns[len(df_original.columns)-1]].map(lambda x: x.count("phyB"))
# df_original[df_original['count'] > 0]
df_original['label'] = sum([df_original['count'] > 3])
x = df_original["cleaned_data"] 
y = df_original.label.values 
x_train, x_valid, y_train, y_valid = train_test_split(x, y, 
test_size=0.30,
random_state=42, 
shuffle=True,
stratify=y,
)
phyB_classifier = Pipeline(steps=[
    ('pre_processing',TfidfVectorizer(lowercase=False)),
    ('naive_bayes',MultinomialNB())
])
phyB_classifier.fit(x_train, y_train) 
y_predict = phyB_classifier.predict(x_valid) 
accuracy_score(y_valid, y_predict)
import joblib
# import it to the webscraping folder
joblib.dump(phyB_classifier, '/Users/emilyjiang/Desktop/Webscraping')
