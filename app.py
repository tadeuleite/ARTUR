from chatterbot.conversation import Statement, StatementMixin
from chatbot import chatbot
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    input_statement = Statement(userText)
    response =  chatbot.get_response(input_statement)
    # generatedResponse = chatbot.generate_response(input_statement)
    return str(response)

if __name__ == "__main__":
    app.run()