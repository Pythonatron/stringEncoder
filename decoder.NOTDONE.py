output = []
seq = {
     "0": "a", "1a": "b", "1b": "c", "2": "d", "3": "e", "5": "f",
     "8": "g", "13": "h", "21": "i", "34": "j", "55": "k",
     "89": "l", "144": "m", "233": "n", "377": "o", "610": "p",
     "987": "q", "1597": "r", "2584": "s", "4181": "t",
     "6765": "u", "10946": "v", "17711": "w", "28657": "x",
     "46368": "y", "75025": "z"
}

def decoder(input):
    for i in input.split(' '):
        if i in seq:
            output.append(seq[i])
        elif i == "||":
            output.append(' ')
        else:
            output.append(i)
    final = ''.join(output)
    print("Decoded: " + final)

toDecode = input("Enter coded message for decoding: ").lower()
decoder(toDecode)
