#SUMMARIZER APPS

from django.apps import AppConfig

class SummaryappConfig(AppConfig):
    name = 'summaryapp'
    def summarizer(text):

            from nltk.corpus import stopwords
            from nltk.tokenize import word_tokenize,sent_tokenize
            from nltk.stem.snowball import SnowballStemmer
            import nltk
            import requests
            import json
            import re

            #text=request.json.get('text')   
            #text = request.get_json('text')
            #text=request.json.get('text')

            text=str(text)
            #text= re.sub(r"[[0-9]+]","",text)
            #text=re.sub(r'\([^)]*\)', '', text)
            #text= re.sub(r"\[","",text)
            text= re.sub(r"[\u2022,\u2023,\u25E6,\u2043,\u2219]\s\d\.\s[A-z]","\n", text)
            stemmer = SnowballStemmer("english")
            stopWords = set(stopwords.words("english"))
            words = word_tokenize(text)
            freqTable = dict()
            for word in words:
                word = word.lower()
                if word in stopWords:
                    continue
                word = stemmer.stem(word)
                if word in freqTable:
                    freqTable[word] += 1
                else:
                    freqTable[word] = 1

            sentences = sent_tokenize(text)
            sentenceValue = dict()

            for sentence in sentences:
                for word, freq in freqTable.items():
                    if word in sentence.lower():
                        if sentence in sentenceValue:
                            sentenceValue[sentence] += freq
                        else:
                            sentenceValue[sentence] = freq
            #print("\n\n",sentenceValue,"\n\n")#=======>
            sumValues = 0
            for sentence in sentenceValue:
                sumValues += sentenceValue[sentence]

            # Average value of a sentence from original text
            average = int(sumValues / len(sentenceValue))

            summary = {}
            key=1
            for sentence in sentences:
                if (sentence in sentenceValue) and (sentenceValue[sentence] > (1. * average)):
            #print(sentenceValue[sentence]," with avg= ",1.5 * average)#it was 1.2 initially
                    summary[key] = sentence
                    key+=1

            clean_10_summary={}
            key_num=1
            for sent in summary.keys():
                if len(summary[sent]) > 20:
                    clean_10_summary[key_num]=summary[sent]
                    key_num+=1
                    #if key_num==21:
                        #break     
                else:
                    continue
            return clean_10_summary
        


