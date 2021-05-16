from static.objects.BotResponse import BotResponse
from chatterbot.conversation import Statement, StatementMixin
from chatbot import chatbot
from flask import Flask, render_template, request, url_for
import json

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = chatbot.get_response(userText)
    objectResponse = BotResponse(response.confidence, response.text, response.in_response_to, response.conversation, response.tags)
    jsonResponse = json.dumps(objectResponse.__dict__, ensure_ascii=False).encode('utf8')
    return jsonResponse 


if __name__ == "__main__":
    app.run() 