import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot pairs
pairs = [
    (r"Hi|Hello|Hey", ["Hello! How can I help you today?", "Hi there! What can I do for you?"]),
    (r"What is your name?", ["I am a chatbot created using NLTK.", "I don't have a name, but you can call me Chatbot."]),
    (r"How are you?", ["I'm doing great! How about you?", "I'm good, thank you for asking!"]),
    (r"(.*) your favorite color?", ["I like all colors, but I think blue is calming."]),
    (r"(.*) (location|city|country)?", ["I am an AI chatbot and don't have a physical location."]),
    (r"quit", ["Goodbye! Have a great day!"]),
]

# Create a chatbot using the defined patterns
def chatbot():
    print("Chatbot: Hello! Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
