import os

path = 'C:/Users/Senya/Downloads/test/1.txt, C:\\Users\\Senya\\Downloads\\test\\2.txt, C:\\Users\\Senya\\Downloads\\test\\3.txt'
print(os.getcwd())
fileContent = []
filesInDirectory = path.split(", ")
for file in filesInDirectory:
    with open(f'{file}') as f:
        fileContent.append(f.readlines())
flag = True
j = 0
# out = []
# while flag:
#     out.append([j + 1, []])
#     for i in range(len(fileContent)):
#         if fileContent[i][j:j + 1] != []:
#             out[j][1].append([i+1, fileContent[i][j]])
#         else:
#             out[j][1].append([i+1, ""])
#     if j < max(map(len, fileContent))-1:
#         j +=1
#     else:
#         flag = False
#
# for i in range(len(out)):
#    print(out[i])
out = {}
while flag:
    out.update({j + 1: {}})
    for i in range(len(fileContent)):
        if fileContent[i][j:j + 1] != []:
            out[j+1].update({i+1: fileContent[i][j]})
        else:
            out[j+1].update({i+1: ""})
    if j < max(map(len, fileContent))-1:
        j +=1
    else:
        flag = False

print(out)

import json
data = {
    "configFile": "config",
    "configurationID": "ID",
    "configurationData": {"mode": "mode", "path": "path"},
    "out": out
}


# Запись словаря в .json-файл
with open("data.json", "w") as json_file:
    json.dump(data, json_file)