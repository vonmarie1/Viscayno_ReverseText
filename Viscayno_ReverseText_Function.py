def text(r):
    magic = ""
    for i in r:
        magic = i + magic
    return magic


while True:
    magic = input("Enter a text: ")

    if magic.isnumeric():
        print("Error Reported! Enter text only!")
    else:
        reversed = text(magic)
        print(reversed)
        break
