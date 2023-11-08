def triangular(x):
    result = []
    alf = {
        "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7",
        "h": "8", "i": "9", "j": "10", "k": "11", "l": "12", "m": "13", "n": "14",
        "o": "15", "p": "16", "q": "17", "r": "18", "s": "19", "t": "20", "u": "21",
        "v": "22", "w": "23", "x": "24", "y": "25", "z": "26"
        }

    def text_to_numeric(s):
        numeric_form = ""
        for char in s:
            if char.isalpha():
                numeric_form += alf[char]
            elif char.isnumeric():
                numeric_form += char
            else:
                numeric_form += char 
        return numeric_form

    parts = x.split()
    for part in parts:
        if part.isnumeric():
            tri = int(part) * (int(part) + 1) / 2
            result.append(int(tri))
        else:
            numeric_form = text_to_numeric(part)
            tri_parts = []
            for char in part:
                if char.isalpha():
                    char_tri = int(alf[char]) * (int(alf[char]) + 1) / 2
                    tri_parts.append(int(char_tri))
            tri_parts = " ".join(map(str, tri_parts))
            result.append(tri_parts)

    result = " ".join(map(str, result))
    return result