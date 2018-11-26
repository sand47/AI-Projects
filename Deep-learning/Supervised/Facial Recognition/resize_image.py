import glob
import cv2

folder_name = "example/*.jpg"
i = 0 
for img in glob.glob(folder_name):
    n= cv2.imread(img)
    m = cv2.resize(n,(640,480))
    name = str(i)
    cv2.imwrite("kannan/"+name+".jpg",m)
    i=i+1
    
