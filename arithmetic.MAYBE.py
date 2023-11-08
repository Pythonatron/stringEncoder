def arithmetic(x):
    
    alph = {
        "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7",
        "h": "8", "i": "9", "j": "10", "k": "11", "l": "12", "m": "13", "n": "14",
        "o": "15", "p": "16", "q": "17", "r": "18", "s": "19", "t": "20", "u": "21",
        "v": "22", "w": "23", "x": "24", "y": "25", "z": "26"
        }
    
    print("Choose an additive number.")
    print("try to keep it relatively small.")
    print("... but it doesn't have to.")
    addval = int(input("Number: "))
    result = []
    
    x = x.lower()
    parts = str(x).split()
    for part in parts:
        if part.isnumeric():
            part = int(part)
            result.append(part + addval)
        else:
            outage = []
            for char in part:
                if char.isalpha():
                    outage.append(int(alph[char]) + addval)
            outage = " ".join(map(str, outage))
            result.append(outage)
    result = " || ".join(map(str, result))
    return result