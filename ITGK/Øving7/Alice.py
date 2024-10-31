f = open("./Alice in Wonderland.txt", "r")

alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols = "\"'.,!?;:-"

def remove_symbols(text):
    for k in text:
        if k in symbols:
            text = text.replace(k, "")
    return text.lower()

formatted = remove_symbols(f.read())

def countWords(file):
    d = {}
    f = open(file, "r")
    unformatted = f.read()
    formatted = remove_symbols(unformatted)
    words = formatted.split()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d
k = countWords("./Alice in Wonderland.txt")
print(k.sort())
