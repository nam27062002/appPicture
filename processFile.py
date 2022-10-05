
def getAllProject():
    L = []
    f = open("project.txt", "r")
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
    url += "/images.txt"
    f = open(url, "r")
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        L.append(line)
    f.close()
    return L
def saveFile(url,array):
    url += "/images.txt"
    with open(url, "w") as f:
        for i in array:
            f.write(i)
            f.write("\n")
    f.close()
def saveNewProject(dir):
    s = ""
    for i in range(len(dir) -1,-1,-1):
        if dir[i] == "/":
            break
        else:
            s =  dir[i] + s

    with open('project.txt',"a") as f:
        f.write(s)
        f.write("|")
        f.write(dir)
        f.writelines("\n")
    f.close()

