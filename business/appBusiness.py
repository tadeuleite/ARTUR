from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from service.appService import appService

class ResponseIa:
    def __init__(self, response, countPrincipalWords):
        self.response = response
        self.countPrincipalWords = countPrincipalWords

class appBusiness(object): 

    def processAI(input):
        Stopwords = set(stopwords.words('portuguese'))
        
        palavras = word_tokenize(input)
        responses = appService.get_responses()

        palavrasSemStopWord = []
        for palavra in palavras:
            if palavra not in Stopwords:
                palavrasSemStopWord.append(palavra)

        respostaMaisAcertiva = []

        for response in responses:
            countPrincipalWords = 0
            for palavra in palavrasSemStopWord:
                if palavra.lower() in response[0].lower():
                    countPrincipalWords = countPrincipalWords + 1
            if countPrincipalWords >= (palavrasSemStopWord.__len__() / 2):
                respostaMaisAcertiva.append(ResponseIa(response, countPrincipalWords))
            
        respostaMaisAcertiva.sort(reverse=True, key=lambda respostaMaisAcertiva: respostaMaisAcertiva.countPrincipalWords)
        return respostaMaisAcertiva
        
