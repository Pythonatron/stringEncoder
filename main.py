import math

def startup():
    original = input("Input text to encoded : ").lower()
    if original.isnumeric() == True:
        print("Letters and symbols only please.")
        startup()
    else:
        return original

def encodingLevel():
    level = input("How encoded would you like your message to be? (levels: 1-5 (5 being highest)): ")
    if level == "" | level.isalpha == True:
        input("Please type a number.")
        encodingLevel()
    else:
        return level



def fibonacci():
    pass    
        
def encoding():
    pass
    
def encodeSymbols():
    pass
    
def encodeAlpha():
    pass

def encodeGibberish():
    #What was this supposed to be again?
    pass
    
def encodeGeometric():
    #multiply
    pass

def encodeArithmetic():
    #addition
    pass

def encodeTriangular():
    #x5 = 5(5+1)/2 = 15
    #xN = N * ( N + 1 ) / 2 = Y
    pass
       
def encodeHill():
    #https://www.google.com/search?q=hill%20cipher&client=firefox-b-1-m
    pass
