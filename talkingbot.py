import pyttsx3
import speech_recognition as sr
from translate import Translator
import random
import json
import nltk
from nltk.stem import WordNetLemmatizer
import wikiAPI
jsonfile = "chat.json"
lemmatizer = WordNetLemmatizer()
global question
question = False
with open(jsonfile, "r") as f:
    contents = json.load(f)

engine = pyttsx3.init()

def formulate_res(sentence: str) -> str:
    global question
    tag_categories = ["greeting", "bye", "yes","no","maybe", "positive","negative", "logan", "intro", "question", "bot"]
    print(sentence)
    for category in tag_categories:
        tags = contents[category]["tag"]
        responses = contents[category]["responses"]
        if question == True:
            question = False
            r = wikiAPI.search_wikipedia(sentence)
            if not r:
                return "It doesnt appear that I have information on that right now"
            else:
                return r + 'If you have any more questions, just say, I have a question, or can i ask something '
        else:
            for tag, response in zip(tags, responses):
                if tag in sentence:


                    if tag in contents["intro"]["tag"]:
                        name = sentence.replace("this is ", "").replace("say hi to ", "")
                        r =  random.choice(responses) + name
                    else:
                        r =  random.choice(responses)
                        question = True if r in contents["question"]["responses"] else False
                    return r
    return "Sorry, I didn't quite catch that"

def say(text: str) -> None:
    engine.say(text)
    engine.runAndWait()

'''engine.say('hello little dumpling')
engine.runAndWait()'''

def listen() -> str:
    r = sr.Recognizer()
    with sr.Microphone(1) as source:
        listen = r.listen(source)
        text = r.recognize_google(listen)
        return text
        
while True:

    #try:
    words = listen()
    response = formulate_res(words)
    say(response)
    '''
    except:
        print('Nothing is being said')
'''