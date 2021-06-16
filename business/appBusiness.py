# pega input
# stopword
# vê quantas palavras principais tem na response
# retorna response
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
class ResponseIa:
    def __init__(self, response, countPrincipalWords):
        self.response = response
        self.countPrincipalWords = countPrincipalWords
class appBusiness(object):
    
  
    def test(input):
        Stopwords = set(stopwords.words('portuguese'))
                
        palavras = word_tokenize(input)
        responses = [
        'a segunda via do boleto pode ser encontrada aqui', 
        'a segunda via da nota fiscal está aqui', 
        'a segunda cadeira está impressa na via', 
        'a segunda via da matricula pode ser encontrada via web']

        respostaMaisAcertiva = []

        for response in responses:
            countPrincipalWords = 0
            for palavra in palavras:
                if palavra in response and palavra not in Stopwords:
                    countPrincipalWords = countPrincipalWords + 1
            if countPrincipalWords >= 3:
                respostaMaisAcertiva.append(ResponseIa(response, countPrincipalWords))
            
        return respostaMaisAcertiva
