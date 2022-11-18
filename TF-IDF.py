#  ANDRÉ LUIZ KOVALSKI

# Sua tarefa será gerar a matriz termo-documento usando TF-IDF por meio da aplicação das 
# fórmulas  TF-IDF  na  matriz  termo-documento  criada  com  a  utilização  do  algoritmo  Bag of 
# Words. Sobre o Corpus que recuperamos anteriormente. O entregável desta tarefa é uma 
# matriz termo-documento onde a primeira linha são os termos e as linhas subsequentes são 
# os vetores calculados com o TF-IDF. 
# 2. Sua tarefa será gerar uma matriz de distância, computando o cosseno do ângulo entre todos 
# os vetores que encontramos usando o tf-idf. Para isso use a seguinte fórmula para o cálculo 
# do  cosseno  use  a  fórmula  apresentada  em  Word2Vector  (frankalcantara.com) 
# (https://frankalcantara.com/Aulas/Nlp/out/Aula4.html#/0/4/2)  e  apresentada  na  figura  a 
# seguir:  
 
# O resultado deste trabalho será uma matriz que relaciona cada um dos vetores já calculados 
# com todos os outros vetores disponíveis na matriz termo-documento mostrando a distância 
# entre cada um destes vetores. 

import sklearn.feature_extraction.text as sk
from bagOfWords import countVector
from corpus import docSents
import pandas as pd
import numpy as np

sentences = []

for doc in docSents:
    allSentences = ""
    for sents in doc:
        allSentences += sents + " "
    sentences.append(allSentences)

vectorizer = sk.TfidfVectorizer()
vectors = vectorizer.fit_transform(sentences)
denselist = vectors.todense().tolist()
dataFrame = pd.DataFrame(denselist, columns=vectorizer.get_feature_names_out())
print("TF-IDF: ")
print(dataFrame)

for i in range(len(countVector)):
    for j in range(i+1, len(countVector)):
        cos = np.dot(countVector[i], countVector[j]) / (np.linalg.norm(countVector[i]) * np.linalg.norm(countVector[j]))
        print(f"Cosseno: {cos} [vetor {i} - vetor {j}]")