from bs4 import BeautifulSoup
import requests
from IPython.display import display
import pandas as pd

urlList = {
    "https://en.wikipedia.org/wiki/Natural_language_processing",
    "https://www.ibm.com/cloud/learn/natural-language-processing",
    "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP",
    "https://www.coursera.org/specializations/natural-language-processing",
    "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/"
}

def main():
    corpus = []
    for url in urlList:
        urlRequest = requests.get(url)
        contents = urlRequest.content
        text = BeautifulSoup(contents, 'html.parser').text
        docSents = []

        currentSent = ""
        for letter in text: 
            if(letter == "." or letter == "?" or letter == "!" or letter == ";" or letter == "\n"  or letter == "\t"):
                if(not(currentSent.isspace()) and len(currentSent) > 0):
                    docSents.append(currentSent)
                    currentSent = ""
                else:
                    currentSent = ""
            else:
                currentSent += letter
        corpus.append(docSents)
    
    ############################################################

    corpusWords = []

    for doc in corpus:
        docArray = []
        for sent in doc:
            words = sent.split(" ")
            docArray.append(words)
        corpusWords.append(docArray)
    
    ############################################################

    frequencia = {}

    for doc in corpusWords:
        for sent in doc:
            for words in sent:
                if words != "":
                    if words in frequencia.keys():
                        frequencia[words] += 1
                    else:
                        frequencia[words] = 1

    frequencia = sorted(frequencia.items(), key=lambda x:x[1])

    df = pd.DataFrame(frequencia)
    # displaying the DataFrame
    display(df)

    ############################################################

if (__name__ == "__main__"):
    main()