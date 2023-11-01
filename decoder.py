
sequence = {
     "0": "a", "1a": "b", "1b": "c", "2": "d", "3": "e", "5": "f",
     "8": "g", "13": "h", "21": "i", "34": "j", "55": "k",
     "89": "l", "144": "m", "233": "n", "377": "o", "610": "p",
     "987": "q", "1597": "r", "2584": "s", "4181": "t",
     "6765": "u", "10946": "v", "17711": "w", "28657": "x",
     "46368": "y", "75025": "z"
}

outputting = []

def decoder(input_string):
    for i in input_string.split(' '):
        if i in sequence:
            outputting.append(sequence[i])
        elif i == "//":
            outputting.append(' ')
        else:
            outputting.append(i)
    
    final = ''.join(outputting)
    print("Decoded: " + final)

toDecode = input("Enter coded message for decoding: ").lower()
decoder(toDecode)
