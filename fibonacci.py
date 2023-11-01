def fibonacci(x): #input MUST be a alphabetic string (symbols are ok?)
    sequence = {
     "a":"0", "b":"1", "c":"1","d":"2", "e":"3", "f":"5",
     "g":"8", "h":"13", "i":"21", "j":"34", "k":"55",
     "l":"89", "m":"144","n":"233","o":"377","p":"610",
     "q":"987", "r":"1597", "s":"2584", "t":"4181",
     "u":"6765", "v":"10946", "w":"17711", "x":"28657",
     "y":"46368", "z":"75025"
     }
    coded = []
    for i in x:
        if i == " ":
            coded.append("//")
        elif not i.isalpha():
            coded.append(i)
        else:
            y = sequence[i]
            coded.append(y)
    coded = ''.join(coded)
    return coded