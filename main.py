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
    
def encodeArithmetic():
    #Done
    pass

def caesar():
    #Done
    pass

def fibonacci():
    #Done
    pass    
        
def encodeGeometric():
    #Done
    pass

def encodeTriangular():
    #Done
    pass

def encoding():
    pass
    
def encodeSymbols():
    pass
    
def encodeAlpha():
    #Why?
    pass

def encodeGibberish():
    #What was this supposed to be again?
    pass
    
def encodeHill():
    #https://www.geeksforgeeks.org/hill-cipher/
    pass