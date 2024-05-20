import os
import json

inp = input("Введите аргументы: ").split()
if len(inp) == 2:
    if os.path.exists(inp[0]) and (inp[1].isdecimal()) and (int(inp[1]) <= 5):
        config = inp[0]
        ID = inp[1]
    else:
        config = False
        ID = False
        print("Введенные параметры не валидны")
else:
    print("Введенные параметры не валидны")

if config and ID:
    with open(config) as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]

    for i in range(len(lines)):
        if "#id: " in lines[i] and lines[i].split(": ")[1] == ID:
            mode = lines[i+1].split(": ")[1]
            path = lines[i + 2].split(": ")[1]
    if mode == "dir":
        if os.path.exists(path):
            out = {}
            fileContent = []
            filesInDirectory = os.listdir(path)
            for file in filesInDirectory:
                with open(f'{path}/{file}') as f:
                    lines = f.readlines()
                    lines = [line.rstrip() for line in lines]
                    fileContent.append(lines)

            flag = True
            j = 0

            while flag:
                out.update({j + 1: {}})
                for i in range(len(fileContent)):
                    if fileContent[i][j:j + 1] != []:
                        out[j + 1].update({i + 1: fileContent[i][j]})
                    else:
                        out[j + 1].update({i + 1: ""})
                if j < max(map(len, fileContent)) - 1:
                    j += 1
                else:
                    flag = False

    elif mode == "files":
        filesInDirectory = path.split(", ")

        if map(os.path.exists, filesInDirectory):
            out = {}
            fileContent = []

            for file in filesInDirectory:
                with open(file) as f:
                    lines = f.readlines()
                    lines = [line.rstrip() for line in lines]
                    fileContent.append(lines)

            flag = True
            j = 0

            while flag:
                out.update({j + 1: {}})
                for i in range(len(fileContent)):
                    if fileContent[i][j:j + 1] != []:
                        out[j + 1].update({i + 1: fileContent[i][j]})
                    else:
                        out[j + 1].update({i + 1: ""})
                if j < max(map(len, fileContent)) - 1:
                    j += 1
                else:
                    flag = False

    data = {
        "configFile": config,
        "configurationID": ID,
        "configurationData": {"mode": mode, "path": path},
        "out": out
    }

    outputFileName = "data.json"
    with open(outputFileName, "w") as json_file:
        json.dump(data, json_file)

    print(f'Выходной файл: {os.getcwd()}/{outputFileName}')