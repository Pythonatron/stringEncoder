import math
def geometric(x): #multiply
    result = []
    mult = input("Choose multiplication: ")
    if not mult.isnumeric():
        print("Only numbers.")
        exit()
    else:
        for i in str(x).split():
            if i == "//":
                result.append(i)
                continue
            else:
                mult = int(mult)
                result.append(mult * int(i))
    result = ' '.join(map(str, result)).replace(".0", "")
    return result

print(geometric(15))