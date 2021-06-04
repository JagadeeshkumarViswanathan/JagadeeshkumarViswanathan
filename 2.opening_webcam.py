import cv2

cam = cv2.VideoCapture(0)

count = 5

while cam.isOpened():

    ret, img = cam.read()

    cv2.imshow("Test", img)

    if not ret:
        break

    k=cv2.waitKey(1)

    while count!=0:
        print("Image " + str(count) + "saved")
        file = 'D:\Studies\Project Motion detection/img' + str(count) + '.jpg'
        cv2.imwrite(file, img)
        count -= 1
    print("Close")
    break


cam.release
cv2.destroyAllWindows
