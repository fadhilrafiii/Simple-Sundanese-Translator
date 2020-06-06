import re
import parse
import sys
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('translator.html')

@app.route('/process', methods=['GET'])
def process():
    sentence = request.args.get('daribahasa')
    algoritma = request.args.get('algoritma')
    lang = request.args.get('selectedlanguage')
    return translator(sentence, algoritma, lang)

def borderfunction(string, i):
    M = len(string)
    border = [0 for i in range(M)]
    k = 1
    while (k<=M):
        for m in range(1, k+1):
            if(string[0:m] == string[k+1-m:k+1]):
                border[k] = len(string[0:m])
        k += 1
    
    return border[i]

def KMPSearch(string, text):
    N = len(text)
    M = len(string)
    i = 0
    j = 0
    while (i < N):
        if (text[i] == string[j]):
            if(j == M-1):
                if (text[i+2] == "=" and text[i-M] == "\n"):
                    return i+4
                else:
                    i += 1
                    j = 0
            else:
                i += 1
                j += 1
        elif (j > 0):
            j = borderfunction(string, j-1)
        else:
            i += 1


LO = []

def BMSearch(string, text):
    M = len(string)
    N = len(text)
    i = M-1
    j = M-1
    while (i <= N - 1):
        if (text[i] == string[j]):
            if j == 0 :
                if (text[i+M+1] == "="):
                    return i+M+3
                else:
                    j = M-1
                    i = i + M

            else:
                i -= 1
                j -= 1
        else:
            lo = LO[getIndex(text[i], listChar(text))]
            

            if lo != -999:
                i = i + M - getMin(j, lo + 1)
            else:
                i = i + M
                j = M-1
            
                

def getMin(A, B):
    if (A <= B):
        return A
    else:
        return B

def getIndex(A, B):
    found = False
    i = 0
    N = len(B)
    while (i < N and not found):
        if (B[i] == A):
            found = True
        else:
            i += 1
    
    if found:
        return i
    else:
        return -999


def isExist(A, B):
    N = len(B)
    i = 0
    found =False
    while (i < N and not found):
        if B[i] == A:
            found = True
        else:
            i += 1
        
    if (found):
        return True
    else:
        return False

def listChar(text):
    charList = []
    for letter in text:
        if not isExist(letter, charList):
            charList.append(letter)
    return charList

def buildLO(string, text):
    M = len(string)
    global LO
    for letter in listChar(text):
        found = False
        i = M-1
        while (i >= 0 and not found):
            if (letter == string[i]):
                found = True
            else:
                i -= 1
        if not isExist(i, LO):
            if (i >= 0):
                LO.append(i)
            else:
                LO.append(-999)
                
def Regex(string, text):
    M = len(string)
    x = re.search(string, text)
    i = x.start()
    if (text[i+M+1] == "="):
        return i+M+3

def translator(string, algoritma, lang):
    if (lang == "si"):
        file = open("sunda.txt","r")
    else:
        file = open("indonesia.txt", "r")
    content = file.read()
    
   
    arrOfWord = parse.parseSentence(parse.giveSpace(string))
    translate = []
    if (algoritma == "kmp"):
        for word in arrOfWord:
            if (word == "saya"):
                i = KMPSearch(word, content)
                if (i != None):
                    arti = ""
                    while(content[i] != '\n'):
                        arti += content[i]
                        i += 1
                    arti = re.sub("\s", " | ", arti)
                    arti += " teh"
                    translate.append(arti)
                else:
                    translate.append(word)

            else:  
                i = KMPSearch(word, content)
                if (i != None):
                    arti = ""
                    while(content[i] != '\n'):
                        arti += content[i]
                        i += 1
                    if(word == "kamu"):
                        arti += " teh"
                    translate.append(arti)
                else:
                    translate.append(word)
    elif (algoritma == "bm"):
        for word in arrOfWord:
            if (word == "saya"):
                buildLO(word, content)
                i = BMSearch(word, content)
                if (i != None):
                    arti = ""
                    while(content[i] != '\n'):
                        arti += content[i]
                        i += 1
                    arti = re.sub("\s", " | ", arti)
                    arti += " teh"
                    translate.append(arti)
                else:
                    translate.append(word)

            else:
                buildLO(word, content)  
                i = BMSearch(word, content)
                if (i != None):
                    arti = ""
                    while(content[i] != '\n'):
                        arti += content[i]
                        i += 1
                    if(word=="kamu"):
                        arti += " teh"
                    translate.append(arti)
                else:
                    translate.append(word)
            LO =[]
    else:
        for word in arrOfWord:
            if (word == "saya"):
                i = Regex(word, content)
                if (i != None):
                    arti = ""
                    while(content[i] != '\n'):
                        arti += content[i]
                        i += 1
                    arti = re.sub("\s", " | ", arti)
                    arti += " teh"
                    translate.append(arti)
                else:
                    translate.append(word)

            else: 
                i = Regex(word, content)
                if (i != None):
                    arti = ""
                    while(content[i] != '\n'):
                        arti += content[i]
                        i += 1
                    if(word=="kamu"):
                        arti += " teh"
                    translate.append(arti)
                else:
                    translate.append(word)



    sentence = ""
    for word in translate:
        sentence = sentence + word + " "

    return sentence      