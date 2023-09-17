from PIL import Image
import base64
import json


def convert_base64(location):
    with open(location, "rb") as f:
        content = f.read()
        return base64.b64encode(content).decode("utf-8")

def calculateResolution(lenght):
    currentY = 1
    currentX = 0
    defStop = False
    for i in range(lenght):
        if currentX == 1920:
            currentY += 1
            if currentY == 1080:
                break
            currentX = 0
        currentX += 1
    return [1920,currentY]

inLoc = input("[IN] Please enter the location of file: ")
print("[PROG] Converting to Base64...")
base64data = convert_base64(inLoc)
with open("encodedbase64.txt", "w") as decoded_file:
    decoded_file.write(base64data)
print("[PROG] Importing Image Data...")
loaded_data = None
with open("defaultAssignment.json", "r") as json_file:
    loaded_data = json.load(json_file)
print("[PROG] Creating Image...")

breaked = False
frame_count = 0
currentCharacter = 0

while currentCharacter < len(base64data) or breaked == True:
    
    width = 1920#calculateResolution(len(base64data))[0]
    height = 1080#calculateResolution(len(base64data))[1]
    image = Image.new("RGB", (width, height), "black")
    for y in range(height):
        if breaked == True:
                break
        for x in range(width):
            if currentCharacter >= len(base64data):
                breaked = True
            if breaked == True:
                break
            try:
                image.putpixel((x,y),tuple(loaded_data[base64data[currentCharacter:currentCharacter+2]][1]))
                currentCharacter += 2
            except:
                image.putpixel((x,y),tuple(loaded_data[base64data[currentCharacter]][1]))
                print("[ERR] 2 Digit Not Found.")
                currentCharacter += 1
    image.save(f"encodedPhotos/frame_{frame_count:04d}.png")
    if not breaked:
        frame_count += 1
    else:
        break
print("[DONE] It's saved!")
