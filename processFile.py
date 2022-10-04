
def getAllProject():
    L = []
    f = open("database/nameProject.txt", "r")
    lines = f.readlines()
    for t,line in enumerate(lines):
        L.append(["",""])
        count = 0
        string = ""
        line = line.replace("\n","")
        for i in range(len(line)):
            if line[i] != "|":
                string += line[i]
            else:
                L[t][count] = string
                count += 1
                string = ""
            if i == len(line) - 1:
                L[t][count] = string
    L.reverse()
    f.close()
    return L
def getAllUrl(url):
    L = []
    url += "/user.txt"
    print(url)
    f = open(url, "r")
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        L.append(line)
    f.close()
    return L
def saveNewProject(dir):
    s = ""
    for i in range(len(dir) -1,-1,-1):
        if dir[i] == "/":
            break
        else:
            s =  dir[i] + s

    with open('database/nameProject.txt',"a") as f:
        f.write(s)
        f.write("|")
        f.write(dir)
        f.writelines("\n")
    f.close()
def changeForLine(url,string,index):
    url += "/user.txt"
    L = []
    f = open(url, "r")
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        L.append(line)
    if len(L) == 0:
        with open(url, "w") as f:
            f.write(string)
            f.write("\n")
    else:
        with open(url, "w") as f:
            for i in range(len(L)):
                if i != index:
                    f.write(L[i])
                    f.write("\n")
                else:
                    f.write(string)
                    f.write("\n")
    f.close()
def add(url,string):
    url += "/user.txt"
    with open(url, "a") as f:
        f.write(string)
        f.writelines("\n")
    f.close()