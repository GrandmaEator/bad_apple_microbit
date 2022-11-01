import cv2, os
vidcap = cv2. VideoCapture('5x5.mp4')
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite(os.path.join(os.getcwd(), "imgs") + "\\%d.png" % count, image) # save frame as JPEG file.
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count = count + 1