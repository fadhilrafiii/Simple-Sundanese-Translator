import eel
import re

@eel.expose
def giveSpace(text):
    text = re.sub(",", " ,", text)
    text = re.sub("\?", " ?", text)
    text = re.sub("\!", " !", text)
    text = re.sub("\.", " .", text)

    return text

def parseSentence(text):
    arrOfText = re.split('\s', text)
    return arrOfText
    
