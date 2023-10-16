import math

sym = [
    "¿","]",">","#","+","!","-",";",
    "_","<","&","$","=","~","(",":",
    "[","/","?","%","×","©","¡","§",
    "®"
]
alpha = [
    "a","b","c","d","e","f","g",
    "h","i","j","k","l","m","n",
    "o","p","q","r","s","t","u",
    "v","w","x","y","z"
    ]

def startup():
    original = input("Input text to encoded : ").lower()
    if original.isnumeric() == True:
        print("Letters and symbols only please.")
        startup()
    else:
        return original

def fibonacci(i):
    i = i - 1
    sqrtSC = math.sqrt(5)
    x = int(((1 + sqrtSC) ** i - (1 - sqrtSC) ** i) / (2**i * sqrtSC))
    return x
    
def encodingLevel():
    level = input("How encoded would you like your message to be? (levels: 1-5 (5 being highest)): ")
    if level == " " | level.isalpha == True:
        input("Please type a number.")
        encodingLevel()
    else:
        return level
        
def encoding():
    pass
    
def encodeSymbols():
    pass
    
def encodeAlpha():
    pass

def encodeGibberish():
    #Huh?
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
