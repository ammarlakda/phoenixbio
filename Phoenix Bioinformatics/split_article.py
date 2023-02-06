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

print(split_article("When committing a crime, the person doing it does not carefully think through the sequences. According to Maggie Koerth, “The interviews suggested that people trying to prevent crime don't always understand how people think when they are committing crimes.” The government officials only create fundamentals based on the aftermath of a crime. Although laws are created to prevent crime, it does not stand for the “what if “circumstances. The only thoughts on a criminal's mind at the instant of the action is how they will do it, if was premeditated. When a crime such as murder is off of impulse, something happens to trigger harmful activity; their only thoughts are why they are doing it. In either circumstance criminals will think of themselves as not apprehendable. As a result, criminals continue to transgress because they have no intent of getting caught so there is no need to think about consequences.The procedure leading up to capital punishment plays a huge role in how serious criminals take apprehension. In a criminal's mind, apprehension is not a problem because at least 30 percent of crimes go unsolved. According to New York Post, “A new FBI report found that roughly 40 percent of the nation's slayings went unsolved last year.” Meaning that over 6,000 criminals got away with crime. The serious crimes of people who really deserve the death penalty never get it.Capital punishment has become an useless source of punishment. “After more than 40 years of experimenting with capital punishment, it is time to recognize that we have found no way to narrow the death penalty so that it applies only to the “worst of the worst. “It also remains prone to terrible errors and unacceptable arbitrariness.”(Laurence H. Tribe) A Couple of errors would be wrongfully sentencing someone to death and too many retrials. Wrongful verdicts can cause the retrials which leads to turn overs. Retrials help free people who were sentenced to death on the wrong term. 'For cases whose outcomes are known, an astonishing 82 percent of retried death row inmates turned out not to deserve the death penalty; 7% were not guilty.'(Technical Errors Can Kill)In the early periods of the death penalty in Georgia a person would have been hung. Alice Riley was the first person executed in Georgia; she was hung for murder. These executions were free and the criminals were easily detected. The way the court system has improved and the new expenses have a great impact on the availability of performing executions now compared to earlier centuries. Not only is the death penalty useless, it's expensive. Sentencing death is least likely for first time offenders so they are more likely to be convicted of the most dangerous crimes. “The average cost of defending a trial in a federal death case is $620,932, about 8 times that of a federal murder case in which the death penalty is not sought.”(Death Penalty Information center) Researchers believe that because the death penalty is so expensive, they are least likely to sentence a person to it. This makes offenders more likely to consider enacting any crimes they feel necessary.Debt in the courtroom is increasing as criminal behavior expands. According to DPIC, “because of the high costs of pursuing death penalty cases, Georgia's public defender system has run out of funds. Most of state's 72 capital cases have been brought to a standstill. The judge in one recent high-profile case has put off jury selection until September 10 because of the funding crisis.” “Our current death penalty system does not “work” when two of three death verdicts are too flawed to serve their purpose, when most can't be salvaged and when the cost of each failed verdict is measured in hundreds of thousands of tax dollars, decades of time and untold anguish for victims needing closure.” During this period of contraction, criminals are becoming more defenseless. They are feeling as if the death penalty is collapsing. Over the years, Georgia has had a higher a higher rate of death sentences than every previous year. This is which causes the extreme debt and gap for murderers to get away with crime.In conclusion, the penal system, courts, corrections and police, has evolved over the years. The evolution of the courts has caused an disruption in deterrence of crime. The death penalty was proven non-deterrent based off of how criminals think today compared to the past century. Consequences are never considered right before committing a crime because there is not enough time to think. Apprehension has become harder over the years. Criminals are now fleeing and covering their tracks making it hard to detain them or know what law was actually violated. The debt of America has also become a problem in executions. It limits the amount of people who should actually be put on death row. As followed, these factors make criminals doubt they will experience death row."))