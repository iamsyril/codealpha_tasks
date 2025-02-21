import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!",]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no problem.", "No worries, it happens.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!", "It was nice talking to you. Goodbye!",]
    ],
    [
        r"(.*) (good|great|fine|well)",
        ["That's great to hear!", "Awesome!",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"(.*) (age|old) ?",
        ["I'm just a program, so I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to assist you with whatever you need.",]
    ],
    [
        r"(.*) created you ?",
        ["I was created by you, using Python and NLTK.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I exist in the digital world, so I don't have a physical location.",]
    ],
    [
        r"how (.*) health (.*)",
        ["I'm a chatbot, so I don't have health, but thanks for asking!",]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm not connected to the internet, so I can't check the weather.",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!", "Glad to help!",]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase that?",]
    ],
]

chatbot = Chat(pairs, reflections)


print("Hi, I'm a chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Bye, take care. See you soon!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
