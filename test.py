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
    return (1920,currentY)

print(calculateResolution(200000))