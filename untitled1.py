import pandas as pd

df=pd.read_csv("SEC_Raw_Data.csv")
df=df['Text'].tolist()

import en_core_web_lg
nlp = en_core_web_lg.load()

for i in df:
    doc=nlp(i)
    for X  in doc.ents:
        if X.label_=='ORG':
            if X.text not in ['SEC','THE SEC','THE SEC S',
                                         'SECURITIES AND EXCHANGE COMMISSION',
                                         'THE SECURITIES AND EXCHANGE COMMISSION']:
                if X.text.startswith not in ['SEC','THE SEC','THE SEC S',
                                         'SECURITIES AND EXCHANGE COMMISSION',
                                         'THE SECURITIES AND EXCHANGE COMMISSION']:
                    print(X.text)

import re
def new_search(text,n,se_word):
    '''Searches for text, and retrieves n words either side of the text, which are returned seperately'''
    word = r"\W*([\w]+)"
    groups = re.search(r'{}\W*{}{}'.format(word*n,se_word,word*n), text).groups()
    if groups!='None':
        return groups

for i in df:
    doc=nlp(i)
    for X in doc.ents:
        if X.label_=='DATE':
            try:
                arr=new_search(i,5,X.text)
                for j in arr:
                    if j not in ['LITIGATION','MODIFIED:','FILED:','SEC','THE SEC',
                                 'THE SECURITIES AND EXCHANGE COMMISSION',
                                 'SECURITIES AND EXCHANGE COMMISSION']:
                        print(X.text)
                        break
            except AttributeError:
                        break

for i in df:
    doc=nlp(i)
    for X in doc.ents:
        if X.label_=='PERSON':
            if X.text.startswith != "LR-25":
                print(X.text)

for i in df:
    doc=nlp(i)
    for X in doc.ents:
        if X.label_=='MONEY':
            print(X.text)

for i in df:
    doc=nlp(i)
    for X in doc.ents:
        if X.label_=='PERSON':
            arr=new_search(i,10,X.text)
            for j in arr:
                if j in ['SEC','THE SEC','SECURITIES AND EXCHANGE COMMISSION',
                             'THE SECURITIES AND EXCHANGE COMMISION']:
                    print(X.text)