from uagents import Agent, Context, Model
import requests
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from uagents.setup import fund_agent_if_low

import tkinter as tk

sw = list(STOP_WORDS)

agent = Agent(
        name="jdm",
        port=8000,
        seed="jdm secret phrase",
        endpoint=["http://127.0.0.1:8000/submit"],
    )

fund_agent_if_low(agent.wallet.address())
def clean_jd(jd):
   ''' a function to create a word cloud based on the input text parameter'''
   ## Clean the Text
   # Lower
   cleaned = jd.lower()
   # remove punctuation
   cleaned = re.sub(r'[^\w\s]', '', cleaned)
   # remove trailing spaces
   cleaned = cleaned.strip()
   # remove numbers
   cleaned = re.sub('[0-9]+', '', cleaned)
   #print(clean_jd)
   # tokenize
   cleaned = word_tokenize(cleaned)
   #print(clean_jd)
   # remove stop words
   cleaned = [w for w in cleaned if not w in sw]
   return(cleaned)


def get_resume_score(text):
  cv = CountVectorizer(stop_words='english')
  #cv = TfidfVectorizer(stop_words="english")
  count_matrix = cv.fit_transform(text)
  #Print the similarity scores
  print("\nSimilarity Scores:")

  #get the match percentage
  matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
  matchPercentage = round(matchPercentage, 2) # round to two decimal

  # print("Your resume matches about "+ str(matchPercentage)+ "% of the job description.")
  return matchPercentage

def resume_score(jd,resumes):
    cl = clean_jd(jd)
    score={}
    for i in resumes.keys():
        resume_cleaned = clean_jd(resumes[i])
        t = [cl,resume_cleaned]
        s = get_resume_score(t)
        score[i]=s
    score = sorted(score)
    return score[0:2]
class Request(Model):
    message_jd: dict
    message_resume:dict

@agent.on_message(model=Request)
async def handle_message(ctx:Context,msg:Request):
    jd_dict = msg.message[0]
    res_dict = msg.message[1]
    res_jds = {}


    for i in jd_dict.keys():
        k = resume_score(jd_dict[i], res_dict)
        res_jds[i] = k
    window = tk.window()
    for i in res_jds.keys():
        s = "For Job Description {} , {} resumes are shortlisted".format(i, res_jds[i])
        lab = tk.label(window,text=s)
        lab.pack(pady=10)
    window.mainloop()





