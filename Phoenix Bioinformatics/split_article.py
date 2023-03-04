from summarizer import summarizer
from nltk import word_tokenize
import nltk
nltk.download('punkt')



def summarize(chunked_article):
  summary = summarizer(chunked_article)
  return summary

def split_article(Article):
  """
  Split article into chunks and sends it to the gpt 3 summarizer and outputs the final string which is summarized
  parameters: article
  return: string
  """
  #Maximum sequence length 
  K = 800
  #Total number of tokens in Document
  N = len(word_tokenize(Article))
  words = word_tokenize(Article)
  #Let I be the number of sequences of K tokens or less in Document
  paddingSize = 50
  I = (N//K)
  i =0
  chunks = [""] * (I + 1)
  
  while i < N:
    # Padding start
    if i != 0:
      if i % K == 0:
        counter = paddingSize
        while counter > 0:
          chunks[i//K] += words[i-counter] + " "
          counter = counter - 1



    chunks[i//K] += " " + words[i]
    
    # Padding end
    if i % K == K-1 and i<N-paddingSize:
        counter = 1
        while counter <= paddingSize:
          chunks[i//K] += words[i+counter] + " "
          counter = counter + 1

    i += 1
  master_string = ""

  for i in range(len(chunks)):
    
    temp = summarize(chunks[i])

    master_string += temp + "\n"

  
  return master_string

#print(split_article(""))