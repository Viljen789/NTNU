# f = open("Example.txt", "w")
# f.write("Hello World")
# f.close()

# f = open("Example.txt", "r")
# txt = f.read()
# print(txt)
# f.close()

# try:
#     f =open("example.txt", "r")
#     txt = f.read()
#     print(txt)
# except FileNotFoundError:
#     print("File not found")

# f = open("example.txt", "a+")
# f.write("\nPython is fun!")
# f.seek(0)
# txt = f.read()
# print(txt)
# f.close()

f = open("Numbers.txt", "w+")
f.truncate()
for i in range(10):
    f.write(f"{i}\n")
f.seek(0)
tot = 0
while(1):
    try:
        line = f.readline()
        tot+=int(line[:-1])
    except:
        break
print(tot)
f.close()

