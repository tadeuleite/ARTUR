from typing import Text
from chatterbot import conversation
from chatterbot.conversation import Statement
from static.objects.BotResponse import BotResponse
from chatbot import chatbot
from flask import Flask, render_template, request
import json
import ftfy
# from business.appBusiness import appBusiness
import random

app = Flask(__name__)
app.static_folder = 'static'
defaultResposes = [
'Não entendi a sua pergunta', 'Me desculpe, mas eu não entendi. Ainda estou aprendendo :(', 'Pode repetir a sua pergunta de outra forma, por favor?',
'Não consegui entender o que você quis dizer com isso, desculpe', 'Acho que não entendi bem o que você quis dizer', 
'Ainda estou aprendendo, se importa em repetir a pergunta?'
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = chatbot.get_response(userText)
    previousState = chatbot.get_latest_response(response.conversation)
    respondeGenerate = chatbot.generate_response(response)
    chatbot.learn_response(response,  previousState)
    chatbot.storage.create(text=respondeGenerate.text,in_response_to=respondeGenerate.in_response_to,conversation=respondeGenerate.conversation,persona=respondeGenerate.persona)
    formatedResponse = ftfy.fix_text(response.text)
    objectResponse = BotResponse(response.confidence, formatedResponse, response.in_response_to, response.conversation, response.tags)
    if objectResponse.confidence < 0.8:
        # iaResult = appBusiness.startIA()

        # if iaResult.confidence < 0.8:
        n = random.randint(0, (defaultResposes.__len__() - 1))
        objectResponse.text = defaultResposes[n]

    jsonResponse = json.dumps(objectResponse.__dict__, ensure_ascii=False).encode('utf8')

    return jsonResponse 

if __name__ == "__main__":
    app.run() 
