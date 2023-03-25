
import sys
import nltk
import aiml
import time
import pandas as pd
import sklearn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.sem import Expression
from nltk.inference import ResolutionProver
from string import punctuation

read_expr = Expression.fromstring

kernel = aiml.Kernel()
kernel.learn("fileList.aiml")
kernel.respond("LEARN AIML")

def loadAimlFiles():
    kernel.bootstrap(learnFiles="fileList.aiml")
    time.sleep(1)

def loadNLTKFiles():
    try:
        nltk.data.find('stopwords')
        nltk.data.find('wordnet')
        nltk.data.find('punkt')
        nltk.data.find('averaged_perceptron_tagger')
    except LookupError:
        nltk.download('wordnet')
        nltk.download('stopwords')
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
    finally:
        time.sleep(1)

def loadKBFile():
    kb = []
    data = pd.read_csv('kb.csv', header=None)
    [kb.append(read_expr(row))for row in data[0]]
    return kb

def getUserInput():
    print("\nStart message with '$' to execute a command")
    try:
        userInput = input("User: ")
        return userInput
    except (KeyboardInterrupt, EOFError):
        print("Terminating...")

def checkForUnknownInput(response):
    unknownInput = 'Unknown Input'

    if response == unknownInput:
        return True
    else:
        return False

def displayHelp():
    helpFile = 'chatbot_help.txt'
    try:
        with open(helpFile,'r') as file:
            print(file.readlines)
    except FileNotFoundError:
        print(f"Unable to locate: {helpFile}")

def parseUserInput(userInput, KB):

    responseAgent = 'aiml'
    if responseAgent == 'aiml':
        response = kernel.respond(userInput)

    if response[0] == '#':
        params = response[1:].split('$')
        cmd = int(params[0])
        if cmd == 0:
            kernel.saveBrain("chatbot_brain.brn")
        elif cmd == 1:
            successfulExit = input('Are you sure you want to exit? (Y/N): ')
            if successfulExit.lower() == 'y':
                sys.exit()
            elif successfulExit.lower() == 'n':
                pass
        elif cmd == 2:
            displayHelp()
        elif cmd == 3:
            object,subject=params[1].split(' is ')
            expr = read_expr(subject + '(' + object + ')')
            KB.append(expr)
            print(f"Bot: ok i will remember that {object}, is {subject}")
        elif cmd == 4:
            object,subject=params[1].split(' is ')
            expr = read_expr(subject + '(' + object + ')')
            answer = ResolutionProver().prove(expr, KB, verbose=True)
            if answer:
                print("Bot: Correct")
            else:
                print("It might not be true")
        elif cmd == 99:
            closestMatchToInput(userInput)
    else:
        print("Bot: ", response)

def penn2morphy(tag):
    tags = {'NN':'n', 'JJ':'a','VB':'v', 'RB':'r'}
    try:
        return tags[tag[:2]]
    except:
        return 'n'

def getFileContents():
    data = pd.read_csv('SecondDraft.csv')
    return data

def removeStopWords(text):
    engStopWords = set(stopwords.words('english'))
    puncStopWords = engStopWords.union(set(punctuation))
    puncRemoved = [word for word in text if word not in puncStopWords]
    return puncRemoved

def lemmatizedText(text):
    wnl = WordNetLemmatizer()
    lemmatizedUserInput = [wnl.lemmatize(word.lower(), pos=penn2morphy(tag))
                           for word, tag in text]
    return lemmatizedUserInput

def tokenizeTextWithTags(text):
    userInputTokens = pos_tag(word_tokenize(text))
    return userInputTokens

def closestMatchToInput(Input):
    sentences = getFileContents()
    tfidf = TfidfVectorizer()
    vectors = []
    userInput = lemmatizedText(tokenizeTextWithTags(Input))
    questions = sentences['Question']

    for line in questions:
        question = lemmatizedText(tokenizeTextWithTags(line))
        vectors.append(tfidf.fit_transform(question))
    
   cosine_similarity(userinput, vectors)




def main():
    loadNLTKFiles()
    loadAimlFiles()
    KB = loadKBFile()
    while True:
        userInput = getUserInput()
        parseUserInput(userInput, KB)

if __name__ == '__main__':
    main()