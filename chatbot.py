from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'A.R.T.U.R.',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Me desculpe, mas eu não entendi. Ainda estou aprendendo :(',
            'maximum_similarity_threshold': 0.90
        }
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training with Portugues Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    "chatterbot.corpus.portuguese.greetings",
    "chatterbot.corpus.portuguese.conversations",
    "training/saudacao.yml",
    "training/financeiro.yml",
    "training/documentacao.yml",
    "training/curso.yml"
)
