from PIL import Image
import json
import base64
import numpy as np
import glob
import ast
import os

loc = input("[IN] Enter the PNG location for decoding: ")

print("[PROG] Loading Decode Data...")
loaded_data = None
with open("decodeAssignment.json", "r") as json_file:
    loaded_data = json.load(json_file)
print("[PROG] Gathering Data...")

pattern = 'frame_*.png'
png_files = glob.glob(os.path.join(loc, pattern))


base64text = ""

currentFrame = 1
currentPixel = 1
inaccuratePixels = 0
for pngFile in png_files:
    image = Image.open(pngFile)
    width, height = image.size
    notWarned = True

    for y in range(height):
        for x in range(width):
            if str(image.getpixel( (x,y) ) ) == "(0, 0, 0)":
                continue
            try:
                base64text += loaded_data[str(image.getpixel((x,y)))][0]
                currentPixel += 1
            except:
                if notWarned == True:
                    print("[WARN] Inaccurate pixel detected, program will use experimental mode. (It's normal for video decoders)\n     Also, it can be slower, and mistakes are expected.")
                    notWarned = False
                distances = [np.linalg.norm(np.array(image.getpixel((x,y))) - np.array(array[1],dtype=np.int32)) for array in loaded_data]
                closest_index = np.argmin(distances)
                for i, var in enumerate(loaded_data):
                    if i == closest_index:
                        base64text += loaded_data[var][0]
                        inaccuratePixels += 1
                        currentPixel += 1
                        break
    currentFrame += 1 
    currentPixel = 0



byteBase64 = base64text.encode('utf-8')
decodedData = base64.b64decode(byteBase64 + b'==')
with open("decoded_file.png", "wb") as decoded_file:
    decoded_file.write(decodedData)
print("[DONE] File is saved to the current directory.")
