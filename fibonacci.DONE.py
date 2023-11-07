def fibonacci(x): #input MUST be a alphabetic string (symbols are ok?)
    sequence = {
     "a":"0", "b":"1a", "c":"1b","d":"2", "e":"3", "f":"5",
     "g":"8", "h":"13", "i":"21", "j":"34", "k":"55",
     "l":"89", "m":"144","n":"233","o":"377","p":"610",
     "q":"987", "r":"1597", "s":"2584", "t":"4181",
     "u":"6765", "v":"10946", "w":"17711", "x":"28657",
     "y":"46368", "z":"75025"
     }
    enc = []
    for i in x:
        if i == " ":
            enc.append("||")
        elif not i.isalpha():
            enc.append(i)
        else:
            y = sequence[i]
            enc.append(y)
    enc = ''.join(enc)
    return enc