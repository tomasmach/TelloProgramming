import cv2
import numpy as np

cap = cv2.VideoCapture(0)
hsvVals = []
sensors = 3
threshold = 0.2
width, height = 480, 360
sensitivity = 3  # if number is high, less sensitive


def thresholding(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([hsvVals[0], hsvVals[1], hsvVals[2]])
    upper = np.array([hsvVals[3], hsvVals[4], hsvVals[5]])
    mask = cv2.inRange(hsv, lower, upper)
    return mask


def getContours(imgThres, img):
    contours, hierarchy = cv2.findContours(imgThres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    biggest = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(biggest)
    cx = x + w // 2
    cy = y + h // 2
    cv2.drawContours(img, biggest, -1, (255, 0, 255), 7)
    cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    return cx


def getSensorOutput(imgThresh, sensors):
    imgs = np.hsplit(imgThresh, sensors)
    totalPixels = (img.shape[1] // sensors) * img.shape[0]
    senOut = []
    for x, im in enumerate(imgs):
        pixelCount = cv2.countNonZero(img)
        if pixelCount > threshold * totalPixels:
            senOut.append(1)
        else:
            senOut.append(0)
        # cv2.imshow(str(x), im)
    # print(senOut)
    return senOut


def sendCommands(senOut, cx):
    ##Translation
    lr = (cx - width // 2) // sensitivity
    lr = int(np.clip(lr, -10, 10))

    if lr < 2 and lr >-2:
        lr = 0


while True:
    _, img = cap.read()
    img = cv2.resize(img, (width, height))
    # img = cv2.flip(img, 0) #Flipping image

    imgThresh = thresholding(img)
    cx = getContours(imgThresh, img)  ##Translation
    senOut = getSensorOutput(imgThresh, sensors)  ##Rotation
    sendCommands(senOut, cx)
    cv2.imshow("Output", img)
    cv2.imshow("Path", imgThresh)
    cv2.waitKey(1)
