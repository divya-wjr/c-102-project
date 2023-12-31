import cv2
image=cv2.imread("solar-system.jpg")

cv2.putText(image,
            "Sun",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,0,200),
            2
            )

cv2.putText(image,
            "Mercury",
            (110,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            1
            )

cv2.putText(image,
            "Venus",
            (190,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            1
            )

cv2.putText(image,
            "Earth",
            (300,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            1
            )

cv2.putText(image,
            "Mars",
            (400,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            1
            )

cv2.putText(image,
            "Jupiter",
            (500,90),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            1
            )

cv2.putText(image,
            "Saturn",
            (720,110),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            1
            )

cv2.putText(image,
            "Uranus",
            (950,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            1
            )

cv2.putText(image,
            "Neptune",
            (1080,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            1
            )

print(image)
cv2.imshow("solarsystem",image)
cv2.waitKey(0)