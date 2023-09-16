from sklearn.metrics.pairwise import cosine_similarity
import random
import string
import json
import copy
import numpy as np

def findCopy(t,v):
    for tvalue in t:
        if tvalue == v:
            return True
    else:
       return False
    
print("Assigning base64")
base64_characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + '+' + '/')

print("Assigning Colors")
colorValues = []
similarityList = []
lastestRandom = 0
for i in range(len(base64_characters)):
    goForBreak = False
    while True:
        if goForBreak == True:
            break
        randonRGB = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if findCopy(colorValues,randonRGB) == True:
            continue
        else:
            for colorT in colorValues:

                ## Experimental! Isn't added yet.
                numColorT = np.array(colorT)
                numOur = np.array(randonRGB)
                cosine_sim = cosine_similarity([numColorT], [numOur])[0][0]
                similarity = cosine_sim * 100
                if False:
                    break
                else:
                    print(f"[LOG] {str(randonRGB)} is saved out of {i}/63 with the similarity of {similarity}%")
                    colorValues.append(randonRGB)
                    similarityList.append(similarity)
                    goForBreak = True
                    lastestRandom = similarity
                    break
            if len(colorValues) == 0:
                print(f"[LOG] {str((255,255,255))} is saved out of {i}/63 with the similarity of 0%")
                colorValues.append(randonRGB)
                goForBreak = True
                break

sumsa = 0
for jj in similarityList:
    sumsa += jj

print(f"[DONE] Color Assignment is done.")
print("[DONE] Assignments are completed.")
data1 = {}
data2 = {}

colorValues1 = copy.copy(colorValues)
colorValues2 = copy.copy(colorValues)

for base64_character in base64_characters:
    data1[base64_character] = [base64_character,colorValues1[0]]
    colorValues1.pop(0)

    data2[str(colorValues2[0])] = [base64_character,colorValues2[0]]
    colorValues2.pop(0)

print("[SAV] Writing defaultAssignment.json")
with open("defaultAssignment.json", "w") as json_file:
    json.dump(data1, json_file)
print("[SAV] Writing decodeAssignment.json")
with open("decodeAssignment.json", "w") as json_file:
    json.dump(data2, json_file)