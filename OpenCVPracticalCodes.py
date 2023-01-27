#OpenCV Image Processing
#1 - Importing an image
#2 - Exporting an image
#3 - Opening Webcam and recording a video
#4 - Resizing and cropping an image
#5 - Figures and Text
#6 - Concatenation of the images
#7 - Perspective distortion
#8 - Blending images
#9 - Image thresholding
#10 - Blurring
#11 - Morphologic Operations
#12 - Gradiens
#13 - Histogram


#%% 1 - Importing an image
import cv2

img1 = cv2.imread("Sources\source.png", 0)

#Visualization of img1

cv2.imshow("First Image", img1)

k = cv2.waitKey(0) & 0xFF
print(k)

if k == 27:#27 number is for "Escape" Button
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("source_gray.png", img1)
    cv2.destroyAllWindows()


#%% 2 - Importing a video
import cv2
import time

videoName = "Sources\AnMP4File.mp4"

cap = cv2.VideoCapture(videoName)

#print("Width: ", cap.get(3))#To take the width of the video!
#print("Height: ", cap.get(4))#To take the height of the video!

if(cap.isOpened() == False):
    print("There is an error!")
    
while True:

    ret, frame = cap.read()
    
    if ret == True:
        time.sleep(0.01) #To set the Frame per Second (FPS)
        frame = cv2.resize(frame, (960, 540))
        cv2.imshow("An Intro Video", frame)
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release() #To stop the capture!
cv2.destroyAllWindows()


#%% 3 - Opening Webcam and recording a video
import cv2
cap = cv2.VideoCapture(0)

print("Width: ", cap.get(3), " - Width: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height: ", cap.get(4), " - Height: ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter("video_kaydi.mp4",cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("WebCam", frame)
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()        
writer.release()
cv2.destroyAllWindows()



#%% 4 - Resizing and cropping an image
import cv2

img = cv2.imread("Lenna.png")
print(img.shape)

#Resizing process
cv2.imshow("The Original Photo of Lenna", img)
imgResized = cv2.resize(img, (150, 150))
cv2.imshow("The Resized Photo of Lenna", imgResized)

#Cropping process
imgCropped = img[:100, :300] #[:HeightPixel, :WeightPixel]
cv2.imshow("CroppedImage", imgCropped)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


        
#%% 5 - Figures and Text
import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)

#For Line
cv2.line(img, (100, 100), (100, 300), (0, 255, 0), 3) #(image, start, end, color, thickness) with BGR(Blue-Green-Red) Mod
cv2.imshow("Black Image", img)

#For Rectangle
cv2.rectangle(img, (0,0), (256, 256), (255, 0, 0), cv2.FILLED) #(image, start, end, color)
cv2.imshow("Rectangle", img)

#For Circle
cv2.circle(img, (256, 256), 100, (0, 0, 255), cv2.FILLED) #(image, center, radius, color)
cv2.imshow("Circle", img)

#For Text
cv2.putText(img, "Kadir Tuna", (0, 0), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255)) #(image, text, start, font, thickness, color)
cv2.imshow("The Signature", img)

if cv2.waitKey(0) & 0xFF == 27: 
    cv2.destroyAllWindows()






