class BotResponse:
    def __init__(self, confidence, text, in_response_to, conversation, tags):
        self.confidence = confidence
        self.text = text
        self.in_response_to = in_response_to
        self.conversation = conversation
        self.tags = tags