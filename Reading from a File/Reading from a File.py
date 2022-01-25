

def attempt1():
    newlist = []
    with open("TextFile.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "").split(",")
            for item in line: newlist.append(item)
    print(newlist)

def attempt2():
    newstr = ""
    with open("TextFile.txt", "r") as file:
        for line in file:
            if line != "\n":
                newstr = newstr + line
        newstr = newstr.replace("\n", ",").split(",")
    print(newstr)

attempt2()


