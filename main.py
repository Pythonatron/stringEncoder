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

def encodeArithmetic(x):
    #addition
    if x.isnumeric() == True:
        for y in x:
            pass
    else:
        input("Unable to process non-numeric chatacters.")
        pass

def encodeTriangular(x):
    #x5 = 5(5+1)/2 = 15
    #xN = N * ( N + 1 ) / 2 = Y
    z = x * (x + 1) / 2
    return z
    pass
    
def caesar_cipher():
    def shift_route():
       direction = input("Choose a shift direction (left or right): ").lower()
       if direction not in ("left", "right") or direction == "":
            print("Choose a valid direction.")
            shift_route()
       else:
            return direction
            
    def shift_size():
        adjust = input("Choose a number for shift change: ")
        if not adjust.isnumeric() or adjust == "":
            print("Choose from numbers only.")
            return shift_size()
        else:
            return int(adjust)
    
    direction = shift_route()
    n = shift_size()
    #print('n',n)
    #print('direction',direction)
    if direction ==  "right":
        new_letter = chr(((n % 26) + 97))
    else:
         new_letter = chr(((0 - n) % 26) + 97)
    #print('new letter',new_letter)
    return new_letter
  
#x = caesar_cipher()
#print('output letter',x)
  
            
def encodeHill():
    #https://www.google.com/search?q=hill%20cipher&client=firefox-b-1-m
    pass
