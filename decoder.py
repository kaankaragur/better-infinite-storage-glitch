from PIL import Image
import json
import base64
import numpy as np
import ast

loc = input("[IN] Enter the PNG location for decoding: ")

print("[PROG] Loading Decode Data...")
loaded_data = None
with open("DecodeAssignment.json", "r") as json_file:
    loaded_data = json.load(json_file)
print("[PROG] Gathering Data...")


base64text = ""
image = Image.open(loc)
width, height = image.size
notWarned = True

for y in range(height):
    for x in range(width):
        if str(image.getpixel((x,y))) == "(0, 0, 0)":
            continue
        try:
            base64text += loaded_data[str(image.getpixel((x,y)))][0]
        except:
            if notWarned == True:
                print("[WARN] Inaccurate pixel detected, program will use experimental mode. (It's normal for video decoders)\n     Also, it can be slower, and mistakes are expected.")
                notWarned = False
            distances = [np.linalg.norm(np.array(image.getpixel((x,y))) - np.array(array[1],dtype=np.int32)) for array in loaded_data]
            closest_index = np.argmin(distances)
            for i, var in enumerate(loaded_data):
                if i == closest_index:
                    base64text += loaded_data[var][0]
                    break


print("[]")
decodedData = base64.b64decode(base64text.encode('utf-8'))
with open("decoded_file.png", "wb") as decoded_file:
    decoded_file.write(decodedData)
print("[DONE] File is saved to the current directory.")
