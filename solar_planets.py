import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(
    img,
    "SUN",
    (100, 75), 
    cv2.FONT_HERSHEY_COMPLEX,
    fontScale=1.5,
    color=(0, 0, 255)
)

cv2.putText(
    img,
    "MERCURY",
    (110, 188), 
    cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255, 255, 255)
)

cv2.putText(
    img,
    "VENUS",
    (187, 260), 
    cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255, 255, 255)
)

cv2.putText(
    img,
    "EARTH",
    (285, 265), 
    cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255, 255, 255)
)

cv2.putText(
    img,
    "MARS",
    (380, 180), 
    cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255, 255, 255)
)

cv2.putText(
    img,
    "JUPITER",
    (535, 50), 
    cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.75,
    color=(255, 255, 255)
)

cv2.putText(
    img,
    "SATURN",
    (700, 115), 
    cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.75,
    color=(255, 255, 255)
)

cv2.putText(
    img,
    "URANUS",
    (943, 140), 
    cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.75,
    color=(255, 255, 255)
)

cv2.putText(
    img,
    "NEPTUNE",
    (1087, 150), 
    cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.75,
    color=(255, 255, 255)
)

cv2.imshow("output", img)
cv2.imwrite("Solar_systemwithname.jpg", img)
cv2.waitKey(0)