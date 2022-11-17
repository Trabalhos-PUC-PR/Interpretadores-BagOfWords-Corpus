# ANDRE LUIZ KOVALSKI

# Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de 
# linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função 
# que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta 
# url. Duas condições são importantes:  
# a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 
# 1000 palavras.  
# b) O texto desta página deverá ser transformado em um array de senteças.  
 
# Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca 
# Spacy. 

from bs4 import BeautifulSoup
import requests
import re

urls = [
    'https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1',
    'https://en.wikipedia.org/wiki/Natural_language_processing',
    'https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP',
    'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/',
    'https://www.ibm.com/cloud/learn/natural-language-processing'
]

docSents = []

for url in urls:
    html = requests.get(url)
    soup = (BeautifulSoup(html.text, "html.parser"))

    doc = []
    for script in soup(["script", "style"]):
        script.decompose()

    text = re.sub(r"[\n\t]", "", soup.get_text())

    # https://stackoverflow.com/a/25736082
    for sentencas in re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)", text):
        doc.append(sentencas)
    docSents.append(doc)

for sents in docSents:
    print(sents)
